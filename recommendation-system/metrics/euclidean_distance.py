# File name: euclidean_distance.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This function contains the implementation of the function that calculates the euclidean distance.

import numpy as np

def euclidean_distance_similarity(row1, row2):
  return np.sqrt(np.sum((row1 - row2) ** 2))

def euclidean_distance(utility_matrix):
  # Se obtienen las dimensiones de la matriz de utilidad.
  number_of_elements, number_of_users = utility_matrix.shape
  
  # Se inicializa la matriz de similitud con ceros.
  similarity_matrix = np.zeros((number_of_elements, number_of_elements))
  
  # A partir de este punto se realiza el cálculo de la matriz de similitud.
  for i in range(number_of_elements):
    for j in range(number_of_elements):
      if i == j:
        similarity_matrix[i, j] = 0
      else:
        common_users = np.logical_and(utility_matrix[i] > 0, utility_matrix[j] > 0)
        if np.any(common_users):
          similarity_matrix[i, j] = euclidean_distance_similarity(utility_matrix[i, common_users], utility_matrix[j, common_users])
        else:
          similarity_matrix[i, j] = np.inf
          
  # Se comprueba como resulta la matriz de similitud.
  # print(similarity_matrix)
  
  return similarity_matrix