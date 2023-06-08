# Deteccion-de-Plagio
El plagio de software se considera como utilizar el código fuente de otra personasin su autorización y adjudicarse como propio.

Según el General Report on Software Piracypublicado en BSA (Business Software Alliance), elplagio de software causó pérdidas económicascerca de 46.3 mil millones de dólares en todo elmundo en 2019.

Principales consecuencias en el plagio de software:
- Viola los principios éticos de honestidad, integridad y respecto por lapropiedad intelectual
- Mala calidad y seguridad del software
- No hay competencia justa para los desarrolladores
- Pérdida económica

## Estado de arte
| Autores | Hechos relevantes | Precisión |
| ------- | ----------------- | --------- |
| Omi, Hossain, Islam y Mittra(2021) | DNN, SVM y LSTM | 96.7% |
| Bandara y Wijayarathna (2011) | Naïve Bayes Classifier, KNN yAdaBoost Meta-learning |(75% - 86)% |
| Ullah, Wang, Farhan, Habib yKhalid (2021) | PCA y MLR |(73% - 86)% |

## Objetivo
Determinar si dos códigos fuente escritos en Javacontienen plagio al determinar su similitudutilizando métodos matemáticos como primeraaproximación, y posteriormente refinar dichapredicción con el uso de Machine Learning y DeepLearning para obtener resultados más precisos.

### Objetivo específico
- Determinar el porcentaje de plagio que contiene un código de Java yposteriormente dictaminar un veredicto, evitando caer en falsospositivos (detectado como PLAGIO cuando NO lo es) al elevar elporcentaje de similitud a un 85% para considerar el par de códigos comoplagiados.
- Identificar los segmentos plagiados de los códigos.

## Flujo de trabajo
(Agregar ss)

## M0:TF-IDF
Es un método matemático que calcula los valores de frecuencia para cada término y compara los vectores resultantes utilizando la distancia del coseno.

(Agregar ss)

## M1: Regresión Logística

(Agregar ss)

## M2: RNN + LSTM

(Agregar ss)

## M3: CNN

(Agregar ss)

## M4: Random Forest Classifier

(Agregar ss)

| Métrica | Socre |
| ------- | ----- |
| Exactitud | 83.06% |
| Precisión | 100% |
| Recuperación | 36.73% |
| Puntuación F1 |53.73% |

## Comparación de los modelos
| Modelo | Accuracy |
| ------ | -------- |
| CNN | 84.15% |
| Random ForestClassifier | 83.03% |
| Regresión Logística | 79.82% |
| RNN + LSTM | 70.61% |

## Referencias
- F. Ullah, J. Wang, M. Farhan, M. Habib and S. Khalid, “Software plagiarism detection inmultiprogramming languages using machine learning approach” Concurrency ComputatPract Exper, vol. 33, no. 4, Feb 2021.
- U. Bandara and G. Wijayarathna, “A Machine Learning Based Tool for Source CodePlagiarism Detection”, International Journal of Machine Learning and Computing, vol. 1, no.4, Oct 2011.
- A. M. Omi, M. Hossain, M. N. Islam and T. Mittra, "Multiple Authors Identification fromSource Code Using Deep Learning Model," 2021 International Conference on Electronics,Communications and Information Technology (ICECIT), pp. 1-4, Dec 2021. "Homepage | BSA | The Software Alliance" [Online]. 
- Homepage | BSA | The SoftwareAlliance. Available: https://www.bsa.org/















