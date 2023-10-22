# File name: finding_near_neighbors.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates the near neighbors to a user.

import numpy as np

def finding_near_neighbors(similarity_matrix, number_of_neighbours, user):
  # Se seleccionan el vector de vecinos segun el usuario.
  user_neighbours = np.array(similarity_matrix[user])
  
  # Se ordena el vector, seleccionando los vecinos necesarios (considerando que se cuenta al propio usuario)
  near_neighbours = user_neighbours.argsort()[-number_of_neighbours -1:][::-1]

  # Se elimina al propio usuario de la lista de vecinos
  near_neighbours = np.delete(near_neighbours, 0)
  
  return near_neighbours
