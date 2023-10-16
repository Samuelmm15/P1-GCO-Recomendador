# File name: recommendation_sytem.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates different elements for the prediction.

from metrics.euclidean_distance import euclidean_distance
from metrics.cosine_distance import cosine_distance
from metrics.pearson_correlation import pearson_correlation

def recommendation_system(lines_of_input_file, metrics, number_of_neighbours, type_of_prediction):
  if metrics == 1:
    euclidean_distance(lines_of_input_file) # Se obtiene la matriz de similitud tras esto
  elif metrics == 2:
    pearson_correlation(lines_of_input_file) # Se obtiene la matriz de similitud tras esto
  elif metrics == 3:
    cosine_distance(lines_of_input_file) # Se obtiene la matriz de similitud tras esto

