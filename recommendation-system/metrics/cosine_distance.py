# File name: cosine_distance.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates the cosine distance.
# Copyright (c) 2023 Samuel Martín Morales y Aday Chocho Aisa. All rights reserved.

# LIBRARIES
import numpy as np

##
  # @brief Implements the function that calculates the cosine similarity between two users.
  #
  # @param row1 the first user.
  # @param row2 the second user.
  # @return The cosine similarity between the two users.
#
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

##
  # @brief Implements the function that calculates the cosine distance between all the users.
  #
  # @param utility_matrix the utility matrix.
  # @return The matrix with the cosine distance between all the users.
#
def cosine_distance(utility_matrix):
  number_of_users, number_of_items = utility_matrix.shape
  similarity_matrix = np.zeros((number_of_users, number_of_users))
  
  for i in range(number_of_users):
    for j in range(number_of_users):
      if i != j:
        similarity_matrix[i, j] = cosine_similarity(utility_matrix[i], utility_matrix[j])
  
  # Fill the diagonal with 1 because represents the similarity with itself.
  np.fill_diagonal(similarity_matrix, 1)
  
  return similarity_matrix
