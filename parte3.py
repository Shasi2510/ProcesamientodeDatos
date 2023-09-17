from datasets import load_dataset
import pandas as pd

dataset = load_dataset("mstz/heart_failure")

df = pd.DataFrame(dataset)

#Separacion de Dataframe
df_perecieron = df[df["is_dead"] == 1]

df_noperecieron = df[df["is_dead"] != 1]


#Promedio de Edades
promedio_edades = df['Edad'].mean()

#Verificación de Datos
tipos_de_datos = df.dtypes

print(tipos_de_datos)

