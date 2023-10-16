# File name: cosine_distance.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates the cosine distance.

import numpy as np

def cosine_distance_similarity(row1, row2):
  dot_product = np.dot(row1, row2)
  norm_row1 = np.linalg.norm(row1) # Norma euclídea, se refiere a la extensión de este vector en el espacio.
  norm_row2 = np.linalg.norm(row2)
  return dot_product / (norm_row1 * norm_row2)

def cosine_distance(lines_of_input_file):
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
  
  # Se obtienen las dimensiones de la matriz de utilidad.
  number_of_elements, number_of_users = utility_matrix.shape
  
  # Inicializamos la matriz de similitud con ceros.
  similarity_matrix = np.zeros((number_of_elements, number_of_elements))
  
  # A partir de este punto se realiza el cálculo de la matriz de similitud.
  for i in range(number_of_elements):
    for j in range(number_of_elements):
      similitarity = cosine_distance_similarity(utility_matrix[i], utility_matrix[j])
      similarity_matrix[i, j] = similitarity
      similarity_matrix[j, i] = similitarity
      
  # Se comprueba como resulta la matriz de similitud.
  print(similarity_matrix)
