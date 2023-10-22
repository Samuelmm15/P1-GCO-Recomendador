# File name: write_file_system.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that write the results of the program into a output file.

import numpy as np

def write_file_system(prediction_matrix, similarity_matrix, prediction_history):
  # Escribir el título en el archivo de salida
  with open("../results/output.txt", "w") as file:
    file.write("<< Prediction Matrix >>\n\n")
  
  # Escribir la matriz en el archivo de salida
  with open("../results/output.txt", "a") as file:
    np.savetxt(file, prediction_matrix, fmt='%-10.4f', delimiter="\t")

  # Escribir el título en el archivo de salida
  with open("../results/output.txt", "a") as file:
    file.write("\n\n<< User Similarity Matrix >>\n\n")
  
  # Escribir la matriz en el archivo de salida
  with open("../results/output.txt", "a") as file:
    np.savetxt(file, similarity_matrix, fmt='%-10.4f', delimiter="\t")

  # Escribir el título en el archivo de salida
  with open("../results/output.txt", "a") as file:
    file.write("\n\n<< Prediction History >>\n\n")

  # Escribir la matriz en el archivo de salida
  with open("../results/output.txt", "a") as file:
    file.write(prediction_history)