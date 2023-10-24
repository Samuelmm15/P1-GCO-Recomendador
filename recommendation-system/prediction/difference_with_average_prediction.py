# File name: difference_with_average_prediction.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates the prediction using the difference with the average.
# Copyright (c) 2023 Samuel Martín Morales y Aday Chocho Aisa. All rights reserved.

# LIBRARIES
import numpy as np

# FILES IMPORTS
from prediction.finding_near_neighbors import finding_near_neighbors

##
  # @brief Implements the function that calculates the prediction using the difference with the average.
  #
  # @param similarity_matrix the similarity matrix.
  # @param number_of_neighbours the number of neighbours that the user wants to use to calculate the prediction.
  # @param utility_matrix the utility matrix.
  # @param max_value the maximum value of the utility matrix.
  # @param min_value the minimum value of the utility matrix.
  # @return The prediction matrix and the prediction history.
#
def difference_with_the_average(similarity_matrix, number_of_neighbours, utility_matrix, max_value, min_value):
  prediction_matrix = np.zeros(utility_matrix.shape)
  prediction_history = ""
  
  for i in range(utility_matrix.shape[0]):
    for j in range(utility_matrix.shape[1]):
      if np.isnan(utility_matrix[i, j]):
        numerator = 0
        denominator = 0
        near_neighbors = finding_near_neighbors(similarity_matrix, number_of_neighbours, i) # Calculate the near neighbours
        for k in range(near_neighbors.shape[0]):
          if not np.isnan(utility_matrix[near_neighbors[k], j]):
            numerator += similarity_matrix[i, near_neighbors[k]] * (utility_matrix[near_neighbors[k], j] - np.nanmean(utility_matrix[near_neighbors[k], :]))
            denominator += similarity_matrix[i, near_neighbors[k]]
        # Comprobates if the denominator is 0
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