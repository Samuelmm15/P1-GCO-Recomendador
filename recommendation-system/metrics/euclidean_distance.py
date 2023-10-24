# File name: euclidean_distance.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This function contains the implementation of the function that calculates the euclidean distance.
# Copyright (c) 2023 Samuel Martín Morales y Aday Chocho Aisa. All rights reserved.

# LIBRARIES
import numpy as np

##
  # @brief Implements the function that calculates the euclidean distance between two users.
  #
  # @param row1 the first user.
  # @param row2 the second user.
  # @return The euclidean distance between the two users.
#
def euclidean_distance_similarity(row1, row2):
  return np.sqrt(np.sum((row1 - row2) ** 2))

##
  # @brief Implements the function that calculates the euclidean distance between all the users.
  #
  # @param utility_matrix the utility matrix.
  # @return The matrix with the euclidean distance between all the users.
#
def euclidean_distance(utility_matrix):
  number_of_users, number_of_elements = utility_matrix.shape
  similarity_matrix = np.zeros((number_of_users, number_of_users))
  
  for i in range(number_of_users):
    for j in range(number_of_users):
      if i == j:
        similarity_matrix[i, j] = 0
      else:
        common_users = np.logical_and(utility_matrix[i] > 0, utility_matrix[j] > 0)
        if np.any(common_users):
          similarity_matrix[i, j] = euclidean_distance_similarity(utility_matrix[i, common_users], utility_matrix[j, common_users])
        else:
          similarity_matrix[i, j] = np.inf
          
  # Fill the diagonal with 1 because represents the similarity with itself.        
  np.fill_diagonal(similarity_matrix, 1)
  
  return similarity_matrix