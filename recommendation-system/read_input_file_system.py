# File name: read_input_file_system.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: Main file of the project.

import os
import sys

def read_input_file(input_file):
  # Para comenzar comprobar que el fichero pasado como parámetro existe y tiene la extensión correcta, es decir, `.txt`
  if os.path.exists(input_file) and os.path.isfile(input_file):
    # Se obtiene la extensión del fichero para comprobar
    extension = os.path.splitext(input_file)[1]
    if extension != ".txt":
      print("The input file must be a `.txt` file.")
      sys.exit(1) # Salida del programa con error de tipo 1.
    else:
      try:
        with open(input_file, 'r') as file:
          # Se lee el conteniedo de cada línea del fichero y se almacena en una lista.
          lines = file.readlines()
          print()
          print("Would you like to see the content of the file? [y/n]")
          answer = input()
          if answer == "y":
            print()
            print("The content of the file is the following:")
            for line in lines:
              print(line)
      except FileNotFoundError:
        print(f"The file {input_file} doesn't exist.")
        sys.exit(1)
      except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        sys.exit(1)
        
      return lines
      
      
      
#   try:
#     with open(nombre_archivo, 'r') as archivo:
#         contenido = archivo.read()
#         print(contenido)
# except FileNotFoundError:
#     print(f"El archivo {nombre_archivo} no se encontró.")
# except Exception as e:
#     print(f"Ocurrió un error al leer el archivo: {str(e)}")