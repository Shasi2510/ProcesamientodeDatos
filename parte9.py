import pandas as pd
import requests
import numpy as np
import plotly.graph_objects as go

url = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'
def download_csv(url):
    response = requests.get(url)
    data = response.json()

    with open('data.csv', 'w') as file:
        file.write(response.text)

df=pd.DataFrame('data')

df = df.drop(columns=['survived'])

array = df.values

death_events = df['DEATH_EVENT'].values

X_embedded = TSNE(
    n_components=3,
    learning_rate='auto',
    init='random',
    perplexity=3
).fit_transform(X)

# Generar datos aleatorios
np.random.seed(0)
n = 100  # Número de puntos de datos
x = np.random.randn(n)
y = np.random.randn(n)
z = np.random.randn(n)

# Agregar ruido a los datos
x += 5 * np.random.randn(n)
y += 5 * np.random.randn(n)
z += 5 * np.random.randn(n)

fig = go.Figure()  # Crear una figura vacía

# Añadir el trazado de dispersión 3D a la figura
fig.add_trace(go.Scatter3d(
    x=x, y=y, z=z,  # Datos de x, y y z
    mode='markers',  # Estilo de marcador
    marker=dict(
        size=5,  # Tamaño de los marcadores
        color=z,  # Variable z para la escala de colores
        colorscale='Viridis',  # Colormap para los colores de los marcadores
        opacity=0.8  # Opacidad de los marcadores
    )
))

# Personalizar el diseño de la gráfica
fig.update_layout(
    title='Gráfica de Dispersión 3D',  # Título de la gráfica
    scene=dict(
        xaxis_title='X',  # Etiqueta del eje x
        yaxis_title='Y',  # Etiqueta del eje y
        zaxis_title='Z'  # Etiqueta del eje z
    )
)

# Mostrar la gráfica
fig.show()

