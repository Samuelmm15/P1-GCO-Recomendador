# File name: main.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: Main file of the project.

import os
# Esta librería sirve para poder gestionar de manera sencilla los argumentos pasados por línea de comandos.
import click
import sys
from read_input_file_system import read_input_file
from recommendation_system import recommendation_system

def initial_menu(i, m, n, t):
  print("Welcome to the recommendation system!")
  print()
  print("The introdiced data is the following:")
  print("Input file: " + str(i))
  print("Metrics: " + str(m))
  print("Number of neighbours: " + str(n))
  print("Type of prediction: " + str(t))
  # Para comenzar obtenemos el contenido del fichero de la matriz de utilidad.
  lines_of_input_file = read_input_file(i)
  recommendation_system(lines_of_input_file, m, n, t)
  
  
def help_menu():
  print("Welcome to the support menu!")
  print()
  print("To use the recommendation system, you must to use the following structure:")
  print()
  print("# python3 main.py -i <inputfile> -m <metrics> -n <number-of-neighbours> -t <type-of-prediction>")
  print()
  print("Where:")
  print("<inputfile> is the path to the input file that contains the utility matrix.")
  print("<metrics> is the metrics that you want to use to calculate the similarity between users.")
  print("  1. 'euclidean' for euclidean distance.")
  print("  2. 'pearson' for pearson correlation.")
  print("  3. 'cosine' for cosine similarity.")
  print("<number-of-neighbours> is the number of neighbours that you want to use to calculate the prediction.")
  print("<type-of-prediction> is the type of prediction that you want to use to calculate the prediction.")
  print("  1. 'simple' for simple prediction.")
  print("  2. 'difference' for difference with the average.")
  sys.exit(0) # Salida del programa con éxito.
  
# De esta manera se realiza la implementación del sistema de paso de parámetros por línea de comendos.
@click.command()
@click.option('-i', help='Path to the input file that contains the utility matrix.')
@click.option('-m', type=int, help='Metrics that you want to use to calculate the similarity between users.')
@click.option('-n', type=int, help='Number of neighbours that you want to use to calculate the prediction.')
@click.option('-t', type=int, help='Type of prediction that you want to use to calculate the prediction.')
@click.option('-h', help='Show the help menu.', is_flag=True)
def main(i, m, n, t, h):  # Este es la función principal del programa.
  if h:
    help_menu()
  elif i and m and n and t:
    if not os.path.isfile(i):
      print("The input file doesn't exist.")
      sys.exist(1) # Salida del programa con error de tipo 1.
    elif m == 1 or m == 2 or m == 3:
      if n > 0:
        if t == 1 or t == 2:
          initial_menu(i, m, n, t)
        else:
          help_menu()
      else:
        help_menu()
    else:
      help_menu()
  else:
    help_menu()

if __name__ == "__main__":
  main()
