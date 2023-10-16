# File name: pearson_correlation.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates the pearson correlation.

import numpy as np
from scipy.stats import pearsonr

def pearson_similarity(row1, row2):
  # Obtención de los índices donde ambos usuarios tienen valores no nulos
  common_indices = np.logical_and(~np.isnan(row1), ~np.isnan(row2))
  
  # Si no hay valores en común se devuelve 0
  if not common_indices.any():
    return 0
  
  # Se realiza el cálculo de los coeficientes de Pearson solo para los valores que son comunes
  pearson, _ = pearsonr(row1[common_indices], row2[common_indices])
  return pearson

# Este es un sistema de cálculo de la medida de similitud entre usuarios.
def pearson_correlation(utility_matrix):
  number_of_users, number_of_items = utility_matrix.shape
  similarity_matrix = np.zeros((number_of_users, number_of_users))
  
  for i in range(number_of_users):
    for j in range(number_of_users):
      if i != j:
        similarity_matrix[i, j] = pearson_similarity(utility_matrix[i], utility_matrix[j])
  
  # Se rellena la diagonal principal de la matriz con 1 para indicar que la similitud entre un usuario y él mismo es 1.
  np.fill_diagonal(similarity_matrix, 1)
  # Se comprueba el resultado final
  print()
  print("Matriz de similitud basada en el coeficiente de Pearson:")
  print(similarity_matrix)
  
  