# File name: recommendation_sytem.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates different elements for the prediction.

import numpy as np

from metrics.euclidean_distance import euclidean_distance
from metrics.cosine_distance import cosine_distance
from metrics.pearson_correlation import pearson_correlation
from prediction.simple_prediction import simple_prediction
from prediction.difference_with_average_prediction import difference_with_the_average

def denormalization(lines_of_input_file, matrix):
  # Obtención de los valores máximo y mínimo del fichero de entrada.
  min_value = np.array(lines_of_input_file[0], dtype=float)
  max_value = np.array(lines_of_input_file[1], dtype=float)

  for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        matrix[i, j] = (matrix[i, j] * (max_value - min_value)) + min_value

  print()
  print(matrix)
  return matrix
  

def utility_matrix_conversor(lines_of_input_file):
  # Obtención de los valores máximo y mínimo del fichero de entrada.
  min_value = np.array(lines_of_input_file[0], dtype=float)
  max_value = np.array(lines_of_input_file[1], dtype=float)

  # Quitamos las dos primeras líneas de la lista del fichero de entrada.
  lines_of_input_file_without_two_first_lines = lines_of_input_file[2:]
  # Obtenemos la matriz de utilidad haciendo uso de numpy.
  original_utility_matrix = np.array(lines_of_input_file_without_two_first_lines)
            
  # Obtención de la matriz de utilidad para la realización de la predicción.
  for i in range(original_utility_matrix.shape[0]):
    for j in range(original_utility_matrix.shape[1]):
        element = original_utility_matrix[i, j]
        if element == '-':
            original_utility_matrix[i, j] = np.nan
        else:
            original_utility_matrix[i, j] = float(element)

# Convertimos la matriz de utilidad a una matriz de utilidad en flotante.
  original_utility_matrix = np.array(original_utility_matrix, dtype=float)

# Normalizamos las matrices.
  distance_utility_matrix = np.zeros(original_utility_matrix.shape)

  for i in range(original_utility_matrix.shape[0]):
    for j in range(original_utility_matrix.shape[1]):
        element = original_utility_matrix[i, j]
        if element != np.nan:
            distance_utility_matrix[i, j] = (element - min_value)/(max_value - min_value)
            original_utility_matrix[i, j] = (element - min_value)/(max_value - min_value)
            
  # Se realiza la eliminación de aquellas columnas que tengan algún elemento NaN para realizar las distancias.
  distance_utility_matrix = distance_utility_matrix[:, ~np.isnan(distance_utility_matrix).any(axis=0)]
  
  return distance_utility_matrix, original_utility_matrix

def recommendation_system(lines_of_input_file, metrics, number_of_neighbours, type_of_prediction):
  distance_utility_matrix, original_utility_matrix = utility_matrix_conversor(lines_of_input_file)
  if metrics == 1:
    similarity_matrix = euclidean_distance(distance_utility_matrix) # Se obtiene la matriz de similitud tras esto
  elif metrics == 2:
    similarity_matrix = pearson_correlation(distance_utility_matrix) # Se obtiene la matriz de similitud tras esto
  elif metrics == 3:
    similarity_matrix = cosine_distance(distance_utility_matrix) # Se obtiene la matriz de similitud tras esto
  
  # # Finalizamos con el cáclulo de la predicción.
  if type_of_prediction == 1:
    prediction_matrix = simple_prediction(similarity_matrix, number_of_neighbours, original_utility_matrix)
  elif type_of_prediction == 2:
    prediction_matrix = difference_with_the_average(similarity_matrix, number_of_neighbours, original_utility_matrix)
    
  # Para finalizar se vuelve a obtener la matriz original denormalizando la matriz
  denormalization(lines_of_input_file, prediction_matrix)

