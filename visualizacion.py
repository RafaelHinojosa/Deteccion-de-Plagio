import joblib
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

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
  
  def predict_plagiarism(self, code1, code2):
    sequence_code1 = self.tokenizer.texts_to_sequences([code1])
    sequence_code2 = self.tokenizer.texts_to_sequences([code2])

    sequence_code1 = pad_sequences(sequence_code1, maxlen=self.max_length)
    sequence_code2 = pad_sequences(sequence_code2, maxlen=self.max_length)

    prediction = self.model.predict(sequence_code1 + sequence_code2)
    
    return prediction[0]
  
  def determine_plagiarism(self, predictions):
    if predictions == 1:
      return "Sí es plagio."
    else:
      return "No es plagio."
