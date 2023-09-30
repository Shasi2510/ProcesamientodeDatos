import requests
import matplotlib.pyplot as plt
import sys

url = sys.argv[1]

try:
    response = requests.get(url)
    data = response.json()
except:
    print("Error")
    sys.exit()

datos_anemicos = [data]
datos_diabeticos = [data]
datos_fumadores = [data]
datos_muertos = [data]

# Graficar histogramas
plt.hist([datos_anemicos, datos_diabeticos, datos_fumadores, datos_muertos], color=['orange', 'green', 'red', 'purple'], label=['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos'])
plt.xlabel('Edad')
plt.ylabel('Cantidad')
plt.title('Distribución de edades por enfermedad')
plt.legend()
plt.show()