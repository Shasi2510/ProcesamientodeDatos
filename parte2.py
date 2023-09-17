from datasets import load_dataset
import pandas as pd

dataset = load_dataset("mstz/heart_failure")

df = pd.DataFrame(dataset)

#Separacion de Dataframe
df_perecieron = df[df["is_dead"] == 1]

df_noperecieron = df[df["is_dead"] != 1]



# Función para calcular el promedio de las edades
def calcular_promedio(edades):
    sum_edades = sum(edades)
    cant_edades = len(edades)
    if cant_edades == 0:
        return 0  # Evitar la división por cero si no hay edades en el dataset
    promedio = sum_edades / cant_edades
    return promedio

# Calcular y imprimir el promedio de cada dataset
prom_dataset = calcular_promedio(dataset)


print("Promedio del dataset:", prom_dataset)

