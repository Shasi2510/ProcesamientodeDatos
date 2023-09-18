import requests


def solicitar_api(url):
    try:
        response = requests.get('https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv')

        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud: {e}")
        return None

df = solicitar_api

#Valores Faltantes
df['solicitar_api'].fillna('?', inplace=True)

#Valores Duplicados
df_cleaned = df.dropna()

#Valores atipicos y eliminación
# Calcular el rango intercuartil (IQR)
Q1 = df['solicitar_api'].quantile(0.25)
Q3 = df['solicitar_api'].quantile(0.75)
IQR = Q3 - Q1

# Definir los límites para detectar valores atípicos
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filtrar los valores atípicos
df_cleaned = df[(df['solicitar_api'] >= lower_bound) & (df['solicitar_api'] <= upper_bound)]

import pandas as pd

# Creción de Columna
def categorizar_edad(edad):
    if edad <= 12:
        return "Niño"
    elif 13 <= edad <= 19:
        return "Adolescente"
    elif 20 <= edad <= 39:
        return "Joven adulto"
    elif 40 <= edad <= 59:
        return "Adulto"
    else:
        return "Adulto mayor"

df['categoria_edad'] = df['edad'].apply(categorizar_edad)

print(df)


# Guarda el DataFrame en un archivo CSV.
df.to_csv('resultado.csv', index=False)

print("Datos guardados en resultado.csv")

