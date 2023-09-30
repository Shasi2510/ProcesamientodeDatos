import pandas as pd
import requests
from io import StringIO
import sys
import matplotlib.pyplot as plt

#Para obtener url
url = sys.argv[1]

try:
    response = requests.get(url)
    data = response.json()
except:
    print("Error")
    sys.exit()

#Convertir en DataFrame
df=pd.DataFrame(data)

# Crear subplots
plt.subplots(2, 2, figsize=(12, 8))

# Gráfica de torta para Anémicos
categorias = ['Cantidad de anémicos', 'Cantidad de diabéticos', 'Cantidad de fumadores', 'Cantidad de muertos']
valores = df['Edad']
plt.pie(valores, labels=categorias)

plt.show()