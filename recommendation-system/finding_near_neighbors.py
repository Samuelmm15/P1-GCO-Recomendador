# File name: finding_near_neighbors.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates the near neighbors to a user.

import numpy as np

def finding_near_neighbors(similarity_matrix, number_of_neighbours):
  # Realizamos el cáclulo de los vecinos más cercanos.
  near_neighbors = np.argsort(similarity_matrix)[::-1]
  
  # Seleccionamos los N vecinos más cercanos.
  near_neighbors = near_neighbors[1:number_of_neighbours+1]
  
  # Comprobamos los distintos resultados
  # print("Los vecinos más cercanos son: ", near_neighbors)
  
  return near_neighbors
  
