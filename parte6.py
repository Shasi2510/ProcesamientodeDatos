import pandas as pd
import requests
from io import StringIO
import sys

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

#Categorizar en grupos
df['category'] = df['category'].astype('category')
df['category'] = df['category'].cat.codes

# Exporte un csv resultante
df.to_csv('output.csv', index=False)