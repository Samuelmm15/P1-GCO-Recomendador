# File name: difference_with_average_prediction.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates the prediction using the difference with the average.

from prediction.finding_near_neighbors import finding_near_neighbors

import numpy as np

def difference_with_the_average(similarity_matrix, number_of_neighbours, utility_matrix, max_value, min_value):
  # Se calcula la matriz resultante con la predicción, haciendo uso de la predicción basada en la diferencia con la media.
  prediction_matrix = np.zeros(utility_matrix.shape)
  prediction_history = ""
  
  for i in range(utility_matrix.shape[0]):
    for j in range(utility_matrix.shape[1]):
      if np.isnan(utility_matrix[i, j]):
        numerator = 0
        denominator = 0
        # El numero de vecinos lo calculamos en este punto.
        near_neighbors = finding_near_neighbors(similarity_matrix, number_of_neighbours, i)
        for k in range(near_neighbors.shape[0]):
          if not np.isnan(utility_matrix[near_neighbors[k], j]):
            numerator += similarity_matrix[i, near_neighbors[k]] * (utility_matrix[near_neighbors[k], j] - np.nanmean(utility_matrix[near_neighbors[k], :]))
            denominator += similarity_matrix[i, near_neighbors[k]]
        # Comprobamos que el denominador no sea cero
        if denominator != 0:
          if np.nanmean(utility_matrix[i, :]) + numerator / denominator > 1:
            prediction_matrix[i, j] = 1
          elif np.nanmean(utility_matrix[i, :]) + numerator / denominator < 0:
            prediction_matrix[i, j] = 0
          else:
            prediction_matrix[i, j] = (np.nanmean(utility_matrix[i, :]) + numerator / denominator)
        else:
          prediction_matrix[i, j] = 0
        if denominator != 0:
          prediction_history += "Position (" + str(i) + "," + str(j) + ") => Neighbours: " + str(near_neighbors)
          prediction_history += ", Prediction: " + str(min_value + ((np.nanmean(utility_matrix[i, :]) + numerator / denominator)* (max_value - min_value))) + "\n"
      else:
        prediction_matrix[i, j] = utility_matrix[i, j]

  for i in range(prediction_matrix.shape[0]):
    for j in range(prediction_matrix.shape[1]):
      prediction_matrix[i, j] = (prediction_matrix[i, j] * (max_value - min_value)) + min_value
        
  return prediction_matrix, prediction_history