# File name: simple_prediction.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates the prediction using the simple prediction.

import numpy as np

def simple_prediction(similarity_matrix, near_neighbors, utility_matrix):
  # Se realiza el cáclulo de la predicción haciendo uso de la predicción simple.
  prediction_matrix = np.zeros(utility_matrix.shape)
  
  for i in range(utility_matrix.shape[0]):
    for j in range(utility_matrix.shape[1]):
      if np.isnan(utility_matrix[i, j]):
        numerator = 0
        denominator = 0
        for k in range(near_neighbors.shape[0]):
          if not np.isnan(utility_matrix[near_neighbors[k, 0], j]):
            numerator += similarity_matrix[i, near_neighbors[k, 0]] * utility_matrix[near_neighbors[k, 0], j]
            denominator += similarity_matrix[i, near_neighbors[k, 0]]
        # Se comprueba que el denominador no sea cero.
        if denominator != 0:
          prediction_matrix[i, j] = numerator / denominator
        else:
          prediction_matrix[i, j] = 0
      else:
        prediction_matrix[i, j] = utility_matrix[i, j]
  
  # Se comprueba el resultado de la predicción.
  # print()
  # print("The prediction matrix is the following:")
  # print(prediction_matrix)
  # print()
  
  return prediction_matrix