# File name: finding_near_neighbors.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates the near neighbors to a user.
# Copyright (c) 2023 Samuel Martín Morales y Aday Chocho Aisa. All rights reserved.

# LIBRARIES
import numpy as np

##
  # @brief Implements the function that calculates the near neighbors to a user.
  #
  # @param similarity_matrix the similarity matrix.
  # @param number_of_neighbours the number of neighbours that the user wants to use to calculate the prediction.
  # @param user the user.
  # @return The vector with the near neighbors.
#
def finding_near_neighbors(similarity_matrix, number_of_neighbours, user):
  user_neighbours = np.array(similarity_matrix[user])
  
  # The vector is sorted, selecting the necessary neighbors (considering that the own user is counted)
  near_neighbours = user_neighbours.argsort()[-number_of_neighbours -1:][::-1]

  # The own user is removed from the list of neighbors
  near_neighbours = np.delete(near_neighbours, 0)
  
  return near_neighbours
