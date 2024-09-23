
#Funcion para cargar datos  de archivos

import os
import pandas as pd

def cargar_archivos_txt(carpeta='data', archivos=['df_final_demo.txt', 'df_final_experiment_clients.txt', 'df_final_web_data_pt_1.txt', 'df_final_web_data_pt_2.txt'], delimiter='\,'):
    """
    Carga cuatro archivos .txt desde la carpeta especificada.

    Args:
        carpeta (str): Carpeta donde están almacenados los archivos .txt.
        archivos (list): Lista de nombres de archivos .txt a cargar.
        delimiter (str): Delimitador que separa los valores en los archivos. Por defecto, es tabulación '\t'.

    Returns:
        dict: Un diccionario con los nombres de archivos como claves y los DataFrames como valores.
    """
    datos = {}
    
    for archivo in archivos:
        ruta = os.path.join(carpeta, archivo)
        try:
            # Leer el archivo .txt en un DataFrame de pandas
            df = pd.read_csv(ruta, delimiter=delimiter)
            datos[archivo] = df
            print(f"Archivo {archivo} cargado correctamente.")
        except Exception as e:
            print(f"Error al cargar {archivo}: {e}")
    
    return datos

# Ejemplo de uso
# Cargar los archivos archivo1.txt, archivo2.txt, archivo3.txt y archivo4.txt desde la carpeta 'data'
archivos = ['df_final_demo.txt', 'df_final_experiment_clients.txt', 'df_final_web_data_pt_1.txt', 'adf_final_web_data_pt_2.txt']
datos = cargar_archivos_txt(carpeta='data', archivos=archivos, delimiter=',')  # Cambia el delimitador si es necesario

    