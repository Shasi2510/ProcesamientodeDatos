import numpy as np
import plotly.graph_objects as go
import requests
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

url = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'
def download_csv(url):
    response = requests.get(url)
    data = response.json()

    with open('data.csv', 'w') as file:
        file.write(response.text)

df = pd.DataFrame('data')

df = df.drop(['DEATH_EVENT', 'age'], axis=1)



# Datos de ejemplo
x = np.array(['age'])
y = np.array(['age'])

# Crear la matriz X con una columna de unos para el término de intersección
X = np.column_stack((np.ones(len(x)), x))

# Calcular los coeficientes de regresión utilizando la ecuación matricial
beta = np.linalg.inv(X.T @ X) @ X.T @ y

# Calcular los valores predichos
y_pred = X @ beta

# Graficar los datos y la línea de regresión
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Datos'))
fig.add_trace(go.Scatter(x=x, y=y_pred, mode='lines', name='Regresión lineal'))
fig.show()

#Comparación de Edades
print ('Edades Reales', y)
print ('Edades Predichas', y_pred)

#Error Cuadratico
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio: ", mse)
