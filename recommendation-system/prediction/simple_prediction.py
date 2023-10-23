# File name: simple_prediction.py
# Authors: Samuel Martín Morales, Aday Chocho Aisa
# Date: 14/10/2023
# Description: This file contains the implementation of the function that calculates the prediction using the simple prediction.

from prediction.finding_near_neighbors import finding_near_neighbors

import numpy as np

def simple_prediction(similarity_matrix, number_of_neighbours, utility_matrix, max_value, min_value):
    # Inicializamos la matriz de predicción con ceros.
    prediction_matrix = np.zeros(utility_matrix.shape)
    prediction_history = ""

    # Recorremos todas las entradas de la matriz de utilidad.
    for i in range(utility_matrix.shape[0]):
        for j in range(utility_matrix.shape[1]):
            # Si la entrada es NaN, realizamos la predicción.
            if np.isnan(utility_matrix[i, j]):
                numerator = 0
                denominator = 0
                # El numero de vecinos lo calculamos en este punto.
                near_neighbors = finding_near_neighbors(similarity_matrix, number_of_neighbours, i)
                # Recorremos los vecinos cercanos.
                for k in range(near_neighbors.shape[0]):
                    # Si el valor del vecino no es NaN, lo utilizamos para la predicción.
                    if not np.isnan(utility_matrix[near_neighbors[k], j]):
                        numerator += similarity_matrix[i, near_neighbors[k]] * utility_matrix[near_neighbors[k], j]
                        denominator += similarity_matrix[i, near_neighbors[k]]
                # Comprobamos que el denominador no sea cero.
                if denominator != 0:
                    if numerator / denominator > 1:
                        prediction_matrix[i, j] = 1
                    elif numerator / denominator < 0:
                        prediction_matrix[i, j] = 0
                    else:
                        prediction_matrix[i, j] = numerator / denominator
                else:
                    prediction_matrix[i, j] = 0
                if denominator != 0:
                    prediction_history += "Position (" + str(i) + "," + str(j) + ") => Neighbours: " + str(near_neighbors)
                    prediction_history += ", Prediction: " + str(min_value + ((numerator / denominator) * (max_value - min_value))) + "\n"
            # Si la entrada no es NaN, la copiamos a la matriz de predicción.
            else:
                prediction_matrix[i, j] = utility_matrix[i, j]

    for i in range(prediction_matrix.shape[0]):
        for j in range(prediction_matrix.shape[1]):
            prediction_matrix[i, j] = (prediction_matrix[i, j] * (max_value - min_value)) + min_value

    # Devolvemos la matriz de predicción.
    return prediction_matrix, prediction_history