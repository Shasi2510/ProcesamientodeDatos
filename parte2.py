from datasets import load_dataset
import pandas as pd

dataset = load_dataset("mstz/heart_failure")

df = pd.DataFrame(dataset)

#Separacion de Dataframe
df_perecieron = df[df["is_dead"] == 1]

df_noperecieron = df[df["is_dead"] != 1]


#Promedio de Edades
promedio_edades = df['Edad'].mean()

#Hombres y Mujeres Fumadores
promedio_fumadores = df.groupby('Genero', 'Fumador').mean()
print(promedio_fumadores)