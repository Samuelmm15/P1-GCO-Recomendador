# File name: recommendation_sytem.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates different elements for the prediction.

import numpy as np

from metrics.euclidean_distance import euclidean_distance
from metrics.cosine_distance import cosine_distance
from metrics.pearson_correlation import pearson_correlation
from finding_near_neighbors import finding_near_neighbors

def utility_matrix_conversor(lines_of_input_file):
  # Quitamos las dos primeras líneas de la lista del fichero de entrada.
  lines_of_input_file_without_two_first_lines = lines_of_input_file[2:]
  # Obtenemos la matriz de utilidad haciendo uso de numpy.
  utility_matrix = np.array(lines_of_input_file_without_two_first_lines)
  
  # Realizamos la conversión del caracter '-' a NaN.
  for i in range(utility_matrix.shape[0]):
    for j in range(utility_matrix.shape[1]):
        component = utility_matrix[i, j]
        if component == '-':
            utility_matrix[i, j] = np.nan
        else:
            utility_matrix[i, j] = float(component)
  
  # Convertimos la matriz de utilidad a una matriz de utilidad en flotante.
  utility_matrix = np.array(utility_matrix, dtype=float)
  
  return utility_matrix

def recommendation_system(lines_of_input_file, metrics, number_of_neighbours, type_of_prediction):
  utility_matrix = utility_matrix_conversor(lines_of_input_file)
  if metrics == 1:
    similarity_matrix = euclidean_distance(utility_matrix) # Se obtiene la matriz de similitud tras esto
  elif metrics == 2:
    similarity_matrix = pearson_correlation(utility_matrix) # Se obtiene la matriz de similitud tras esto
  elif metrics == 3:
    similarity_matrix = cosine_distance(utility_matrix) # Se obtiene la matriz de similitud tras esto
    
  # Para continuar se obtienen los vecinos más cercanos.
  near_neighbors = finding_near_neighbors(similarity_matrix, number_of_neighbours)

