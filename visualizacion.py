import joblib
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import difflib

class PredictApp(): 
  def __init__(self):
    super().__init__()

    self.model = joblib.load('classifier.joblib')
    self.tokenizer = joblib.load('tokenizer.joblib')
    self.max_length = joblib.load('max_length.joblib')

  def process_code(self, text):
    text = text.lower()
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    return text
  
  def process_code2(self, text):
    punctuation = ["_", "-", ".", ":", ",", ";", "(", ")", "?", "¿", "¡", "!", '"', "{", "}", "[", "]", "+", "*", "=", "/", "%", "<", ">"]
    punctuation2 = ["{", "}"]
    
    for i in punctuation2:
        text = text.replace(i, " ")

    for i in punctuation:
        text = text.replace(i, " " + i + " ")
    
    text = text.lower()

    return text
  
  def predict_plagiarism(self, code1, code2):
    sequence_code1 = self.tokenizer.texts_to_sequences([code1])
    sequence_code2 = self.tokenizer.texts_to_sequences([code2])

    sequence_code1 = pad_sequences(sequence_code1, maxlen=self.max_length)
    sequence_code2 = pad_sequences(sequence_code2, maxlen=self.max_length)

    prediction = self.model.predict(sequence_code1 + sequence_code2)
    
    return prediction[0]
  
  def determine_plagiarism(self, predictions):
    if predictions == 1:
      return "Sí es plagio"
    else:
      return "No es plagio"
  
  def identify_plagiarized_segments(self, code1, code2):
    lines1 = code1.split('\n')
    lines2 = code2.split('\n')

    matcher = difflib.SequenceMatcher(None, lines1, lines2)
    match_blocks = matcher.get_matching_blocks()

    plagiarized_segments = []
    for match in match_blocks:
        start1, start2, length = match
        if length > 0:
            segment1 = lines1[start1:start1+length]
            segment2 = lines2[start2:start2+length]
            
            if not all(line.strip() == '' for line in segment1) and not all(line.strip() == '' for line in segment2):
                plagiarized_segments.append((segment1, segment2))

    return plagiarized_segments
