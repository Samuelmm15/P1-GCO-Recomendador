# File name: recommendation_sytem.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates different elements for the prediction.
# Copyright (c) 2023 Samuel Martín Morales y Aday Chocho Aisa. All rights reserved.

# LIBRARIES
import numpy as np
import sys

# FILES IMPORTS
from metrics.euclidean_distance import euclidean_distance
from metrics.cosine_distance import cosine_distance
from metrics.pearson_correlation import pearson_correlation
from prediction.simple_prediction import simple_prediction
from prediction.difference_with_average_prediction import difference_with_the_average
from write_file_system import write_file_system

##
  # @brief Implements the function that converts the utility matrix introduced by the input file into a float utility matrix.
  #
  # @param lines_of_input_file the different lines of the input file (utility matrix).
  # @return The float utility matrix without the missing columns, the original utility matrix, maximum value and minimum value.
#
def utility_matrix_conversor(lines_of_input_file):
  min_value = np.array(lines_of_input_file[0], dtype=float) # Min value of the utility matrix.
  max_value = np.array(lines_of_input_file[1], dtype=float) # Max value of the utility matrix.

  lines_of_input_file_without_two_first_lines = lines_of_input_file[2:]
  original_utility_matrix = np.array(lines_of_input_file_without_two_first_lines)
            
  # Utility matrix conversor to float.
  for i in range(original_utility_matrix.shape[0]):
    for j in range(original_utility_matrix.shape[1]):
        element = original_utility_matrix[i, j]
        if element == '-':
            original_utility_matrix[i, j] = np.nan
        else:
            original_utility_matrix[i, j] = float(element)

  original_utility_matrix = np.array(original_utility_matrix, dtype=float)
  distance_utility_matrix = np.zeros(original_utility_matrix.shape)

  for i in range(original_utility_matrix.shape[0]):
    for j in range(original_utility_matrix.shape[1]):
        element = original_utility_matrix[i, j]
        if element != np.nan:
            distance_utility_matrix[i, j] = (element - min_value)/(max_value - min_value) # Normalization of the utility matrix.
            original_utility_matrix[i, j] = (element - min_value)/(max_value - min_value)
            
  # Delete the columns that have NaN values.
  distance_utility_matrix = distance_utility_matrix[:, ~np.isnan(distance_utility_matrix).any(axis=0)]
  return distance_utility_matrix, original_utility_matrix, max_value, min_value

##
  # @brief Implements the function that had the menu that calculates the different elements needed for the prediction.
  #
  # @param lines_of_input_file the different lines of the input file (utility matrix).
  # @param metrics the metrics that the user wants to use to calculate the similarity between users.
  # @param number_of_neighbours the number of neighbours that the user wants to use to calculate the prediction.
  # @param type_of_prediction the type of prediction that the user wants to use to calculate the prediction.
  # @param file_name the name of the file of the input file that contains the utility matrix.
#
def recommendation_system(lines_of_input_file, metrics, number_of_neighbours, type_of_prediction, file_name):
  distance_utility_matrix, original_utility_matrix, max_value, min_value = utility_matrix_conversor(lines_of_input_file)
  if metrics == 1:
    similarity_matrix = euclidean_distance(distance_utility_matrix) # Se obtiene la matriz de similitud tras esto
  elif metrics == 2:
    similarity_matrix = pearson_correlation(distance_utility_matrix) # Se obtiene la matriz de similitud tras esto
  elif metrics == 3:
    similarity_matrix = cosine_distance(distance_utility_matrix) # Se obtiene la matriz de similitud tras esto
  
  # # Finalizamos con el cáclulo de la predicción.
  if type_of_prediction == 1:
    prediction_matrix, prediction_history = simple_prediction(similarity_matrix, number_of_neighbours, original_utility_matrix, max_value, min_value)
  elif type_of_prediction == 2:
    prediction_matrix, prediction_history = difference_with_the_average(similarity_matrix, number_of_neighbours, original_utility_matrix, max_value, min_value)
    
  # Se devuelve todo lo calculado a un fichero externo.
  write_file_system(prediction_matrix, similarity_matrix, prediction_history, metrics, number_of_neighbours, type_of_prediction, file_name)
  sys.exit(0) # Exit with success.

