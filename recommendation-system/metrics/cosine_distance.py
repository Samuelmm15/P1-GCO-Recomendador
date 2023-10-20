# File name: cosine_distance.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates the cosine distance.

import numpy as np
# Importamos la librería que nos permite calcular la similitud coseno.

def cosine_similarity(row1, row2):
  numerator = 0
  denominator1 = 0
  denominator2 = 0


  user1_average = row1.sum()/len(row1)
  user2_average = row2.sum()/len(row2)

  for i in range(len(row1)):
    numerator += (row1[i]) * (row2[i])

    denominator1 += (row1[i]) * (row1[i])
    denominator2 += (row2[i]) * (row2[i])

  return (numerator/(np.sqrt(denominator1) * np.sqrt(denominator2)))

def cosine_distance(utility_matrix):
  number_of_users, number_of_items = utility_matrix.shape
  similarity_matrix = np.zeros((number_of_users, number_of_users))
  
  for i in range(number_of_users):
    for j in range(number_of_users):
      if i != j:
        similarity_matrix[i, j] = cosine_similarity(utility_matrix[i], utility_matrix[j])
  
  # Se rellena la diagonal principal de la matriz con 1 para indicar que la similitud entre un usuario y él mismo es 1.
  np.fill_diagonal(similarity_matrix, 1)

  # Se comprueba el resultado final
  print()
  print(similarity_matrix)
  
  return similarity_matrix
  
  
  
  
  
  
  # # Inicializamos la matriz de similitud con ceros.
  #   similarity_matrix = np.zeros((utility_matrix.shape[0], utility_matrix.shape[0]))
    
  #   # Recorremos todas las combinaciones de vectores.
  #   for i in range(utility_matrix.shape[0]):
  #       for j in range(utility_matrix.shape[0]):
  #           # Calculamos el producto punto y las normas de los vectores.
  #           dot_product = np.dot(utility_matrix[i], utility_matrix[j])
  #           norm_i = np.linalg.norm(utility_matrix[i])
  #           norm_j = np.linalg.norm(utility_matrix[j])
            
  #           # Calculamos la similitud coseno y la almacenamos en la matriz de similitud.
  #           similarity_matrix[i][j] = dot_product / (norm_i * norm_j)
    
  # Comprobamos el resultado
  #print(similarity_matrix)
    
  #return similarity_matrix
