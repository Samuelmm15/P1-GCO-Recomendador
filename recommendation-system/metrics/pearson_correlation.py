# File name: pearson_correlation.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates the pearson correlation.

import numpy as np

def pearson_similarity(row1, row2):
  
  numerator = 0
  denominator1 = 0
  denominator2 = 0


  user1_average = row1.sum()/len(row1)
  user2_average = row2.sum()/len(row2)

  for i in range(len(row1)):
    numerator += (row1[i] - user1_average) * (row2[i] - user2_average)

    denominator1 += (row1[i] - user1_average) * (row1[i] - user1_average)
    denominator2 += (row2[i] - user2_average) * (row2[i] - user2_average)

  return (numerator/(np.sqrt(denominator1) * np.sqrt(denominator2)))
  

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
  print
  print(similarity_matrix)
  
  return similarity_matrix