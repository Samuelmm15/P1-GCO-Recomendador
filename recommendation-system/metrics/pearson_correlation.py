# File name: pearson_correlation.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates the pearson correlation.
# Copyright (c) 2023 Samuel Martín Morales y Aday Chocho Aisa. All rights reserved.

# LIBRARIES
import numpy as np

##
  # @brief Implements the function that calculates the pearson similarity between two users.
  #
  # @param row1 the first user.
  # @param row2 the second user.
  # @return The pearson similarity between the two users.
#
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
  
##
  # @brief Implements the function that calculates the pearson correlation between all the users.
  #
  # @param utility_matrix the utility matrix.
  # @return The matrix with the pearson correlation between all the users.
#
def pearson_correlation(utility_matrix):
  number_of_users, number_of_items = utility_matrix.shape
  similarity_matrix = np.zeros((number_of_users, number_of_users))
  
  for i in range(number_of_users):
    for j in range(number_of_users):
      if i != j:
        similarity_matrix[i, j] = pearson_similarity(utility_matrix[i], utility_matrix[j])
  
  # Fill the diagonal with 1 because represents the similarity with itself.
  np.fill_diagonal(similarity_matrix, 1)
  
  return similarity_matrix