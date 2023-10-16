# File name: read_input_file_system.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that obtains the different lines of the input file.

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
          # Se lee el conteniedo de cada línea del fichero y se almacena en una matriz dividiendo la entrada como elementos independientes.
          rows = []
          for line in file:
            rows.append(line.strip().split())
          print()
          print("Would you like to see the content of the file? [y/n]")
          answer = input()
          if answer == "y":
            print()
            print("The content of the file is the following:")
            for line in rows:
              print(line)
      except FileNotFoundError:
        print(f"The file {input_file} doesn't exist.")
        sys.exit(1)
      except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        sys.exit(1)
        
      return rows