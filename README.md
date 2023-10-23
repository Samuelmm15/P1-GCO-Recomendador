# Sistema de recomendación - Métodos de filtrado colaborativo

Este repositorio contiene la implementación de un sistema de recomendación que utiliza métodos de filtrado colaborativo. El sistema de recomendación se basa en la técnica de filtrado colaborativo, utilizando la similitud mediante distintas métricas que permiten calcular la similitud entre usuarios. El sistema de recomendación se encuentra implementado en [Python 3.11.5](https://www.python.org/downloads/release/python-3110/).

## 🏷️ Descripción del sistema de recomendación

La siguiente aplicación se trata de un sistema de recomendación basado en métodos de filtrado colaborativo. Dicho programa, obtiene una matriz de utilidad a partir
de un fichero de texto el cual contiene dicha matriz, la cual se encuentra incompleta y contiene valores desconocidos, los cuales se deben de predecir. Para ello, se
emplean distintos tipos de métricas que permiten calcular la similitud entre usuarios, que son representados mediante filas de la propia matriz de utilidad.

Una vez se tiene la matriz de similitud entre usuarios, se procede a predecir los valores desconocidos de la matriz de utilidad, para ello se emplean métodos de predicción que permiten predecir los valores desconocidos de la matriz de utilidad, teniendo en cuenta el número de vecinos cercanos al usuario que se desea predecir, 
para el cálculo de la predicción.

Dentro de la aplicación, se pueden encontrar distintos tipos de métricas y métodos de predicción, los cuales se pueden seleccionar mediante un sistema [`POSIX`](https://nullprogram.com/blog/2020/08/01/) instaurado
como paso de argumentos en la línea de ejecución del programa.

### Tipos de métricas

Las distintas métricas que se pueden usar para la ejecución del programa son las siguientes:

1. Distancia Euclídea.
2. Correlación de Pearson.
3. Distancia Coseno.

### Tipos de métodos de predicción

Los distintos métodos de predicción que se pueden usar para la ejecución del programa son los siguientes:

1. Predicción simple.
2. Diferencia con la media.

📌 Para más información sobre el funcionamiento del programa, el uso de los argumentos y la ejecución del mismo, se puede consultar el apartado de [Ejecución del programa](#ejecución-del-programa).

## 🔨 Instalación de dependencias

Para la instalación de las dependencias del programa, se debe de ejecutar el siguiente comando que permite instalar las dependencias necesarias para la ejecución del programa:

```bash
$ pip install -r requirements.txt
```

## ⚡️ Ejecución del programa

Para la ejecución del programa se debe de ejecutar el siguiente comando:

```bash
$ python main.py [-i] [<FILE-PATH>] [-m] [<TYPE-OF-METRIC>] [-n] [<NUMBER-OF-NEIGHBORS>] [-t] [<TYPE-OF-PREDICTION>]
```

Donde:

- `-i` es la ruta del fichero de entrada que contiene la matriz de utilidad.
- `m` es el tipo de métrica que se desea usar para el cálculo de la similitud entre usuarios. Se puede seleccionar entre la métrica 1, 2 o 3.
- `-n` es el número de vecinos cercanos que se desea usar para el cálculo de la predicción.
- `-t` es el tipo de método de predicción que se desea usar para el cálculo de la predicción. Se puede seleccionar entre el método 1 o 2.

📌 Para más información sobre el funcionamiento del programa, el tipo de métricas, el tipo de predicción, etc, realizar la ejecución del programa de la siguiente manera,
para poder visualizar la ayuda del programa:

```bash
$ python main.py -h
```

## Ejemplo de ejecución del programa

A continuación, se muestra un ejemplo de ejecución del programa:

https://github.com/Samuelmm15/P1-GCO-Recomendador/assets/72341631/c51576d2-337d-4dc7-9b6c-b200f8384988

## 📝 Licencia

Este proyecto se encuentra bajo la licencia Creative Commons Legal Code, para más información consultar el fichero [LICENSE](LICENSE).

## ✒️ Autores

- [Samuel Martín Morales](https://github.com/Samuelmm15)
- [Aday Chocho Aisa](https://github.com/alu0101437538)
