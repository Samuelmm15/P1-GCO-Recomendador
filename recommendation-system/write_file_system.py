# File name: write_file_system.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that write the results of the program into a output file.

import os
import numpy as np

# Cabe destacar que el formato de salida de los ficheros se basa principalmente en la siguiente estructura:
# metrics_number_of_neighbours_type_of_prediction_file_name_output.txt

def write_file_system(prediction_matrix, similarity_matrix, prediction_history, metrics, number_of_neighbours, type_of_prediction, file_name):
  file_name = os.path.basename(file_name) # Permite obtener el nombre del fichero, quitando la ruta de acceso.
  file_name = os.path.splitext(file_name)[0] # Permite obtener el nombre del fichero, quitando la extensión.
  output_file_name = f"../results/{str(metrics)}_{str(number_of_neighbours)}_{str(type_of_prediction)}_{str(file_name)}_output.txt"
  # Escribir el título en el archivo de salida
  with open(output_file_name, "w") as file:
    file.write("<< Prediction Matrix >>\n\n")
  
  # Escribir la matriz en el archivo de salida
  with open(output_file_name, "a") as file:
    np.savetxt(file, prediction_matrix, fmt='%-10.4f', delimiter="\t")

  # Escribir el título en el archivo de salida
  with open(output_file_name, "a") as file:
    file.write("\n\n<< User Similarity Matrix >>\n\n")
  
  # Escribir la matriz en el archivo de salida
  with open(output_file_name, "a") as file:
    np.savetxt(file, similarity_matrix, fmt='%-10.4f', delimiter="\t")

  # Escribir el título en el archivo de salida
  with open(output_file_name, "a") as file:
    file.write("\n\n<< Prediction History >>\n\n")

  # Escribir la matriz en el archivo de salida
  with open(output_file_name, "a") as file:
    file.write(prediction_history)