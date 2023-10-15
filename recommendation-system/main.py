# File name: main.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: Main file of the project.

import os
# Esta librería sirve para poder gestionar de manera sencilla los argumentos pasados por línea de comandos.
import click

def initial_menu(i, m, n, t):
  print("Welcome to the recommendation system!")
  print()
  print("The introdiced data is the following:")
  print("Input file: " + i)
  print("Metrics: " + m)
  print("Number of neighbours: " + n)
  print("Type of prediction: " + t)
  
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
  
# De esta manera se realiza la implementación del sistema de paso de parámetros por línea de comendos.
@click.command()
@click.option('-i', help='Path to the input file that contains the utility matrix.')
@click.option('-m', help='Metrics that you want to use to calculate the similarity between users.')
@click.option('-n', help='Number of neighbours that you want to use to calculate the prediction.')
@click.option('-t', help='Type of prediction that you want to use to calculate the prediction.')
@click.option('-h', help='Show the help menu.', is_flag=True)
def main(i, m, n, t, h):
  if h:
    help_menu()
  elif i and m and n and t:
    initial_menu(i, m, n, t)
  else:
    help_menu()

if __name__ == "__main__":
  main()
