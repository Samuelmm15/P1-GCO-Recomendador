# File name: main.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: Main file of the project.

import os
# Esta librería sirve para poder gestionar de manera sencilla los argumentos pasados por línea de comandos.
import argparse

def initial_menu():
  print("Welcome to the recommendation system!")
  
def help_menu():
  print("Welcome to the support menu!")
  print("To use the recommendation system, you must to use the following structure:")
  print("# python3 main.py -i <inputfile> -m <metrics> -n <number-of-neighbours> -t <type-of-prediction>")
  print("Where:")
  print("<inputfile> is the path to the input file that contains the utility matrix.")
  print("<metrics> is the metrics that you want to use to calculate the similarity between users.")
  print("  - 'euclidean' for euclidean distance.")
  print("  - 'pearson' for pearson correlation.")
  print("  - 'cosine' for cosine similarity.")
  print("<number-of-neighbours> is the number of neighbours that you want to use to calculate the prediction.")
  print("<type-of-prediction> is the type of prediction that you want to use to calculate the prediction.")
  print("  - 'simple' for simple prediction.")
  print("  - 'difference' for difference with the average.")
  
def main():
  # Se crea el parser para poder gestionar los argumentos pasados por línea de comandos.
  parser = argparse.ArgumentParser(description="Recommendation system app")
  
  # Se añaden los argumentos que se pueden pasar por línea de comandos.
  parser.add_argument("-i")
  parser.add_argument("-m")
  parser.add_argument("-n")
  parser.add_argument("-t")
  # parser.add_argument("--help", action="store_true")
  
  # Se parsean los argumentos pasados por línea de comandos.
  args = parser.parse_args()
  
  if args.help:
    help_menu()

if __name__ == "__main__":
  main()
