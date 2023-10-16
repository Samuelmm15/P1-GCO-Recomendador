# File name: cosine_distance.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates the cosine distance.

import numpy as np
# Importamos la librería que nos permite calcular la similitud coseno.
from sklearn.metrics.pairwise import cosine_similarity

def cosine_distance(utility_matrix):
  # Manejar los valores NaN llenándolos con ceros, ya que la librería no permite el uso de nan.
  utility_matrix = np.nan_to_num(utility_matrix, nan=0)

  # Se realiza el cáclulo de la similitud haciendo uso de la distancia coseno.
  similarity_matrix = cosine_similarity(utility_matrix)
  
  # Se comprueba como resulta la matriz de similitud.
  print(similarity_matrix)

