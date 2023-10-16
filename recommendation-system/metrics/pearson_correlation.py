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
def pearson_correlation(lines_of_input_file):
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
  
  