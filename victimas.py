import pandas as pd
import requests

# URL base de la API
url = 'https://www.datos.gov.co/resource/uyyb-qiip.json'




# Realizar la solicitud a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()
    # Hacer algo con los datos, como imprimirlos
    print(data)
      # Convertir los datos a un DataFrame de pandas
    df = pd.DataFrame(data)  
      # Escribir el DataFrame en un archivo Excel
    ruta_archivo = "datos_victima.xlsx"
    df.to_excel(ruta_archivo, index=False, engine='openpyxl')
    print("Los datos se han exportado correctamente a", ruta_archivo)
    
else:
    # Imprimir un mensaje de error si la solicitud falló
    print('Error al obtener los datos. Código de estado:', response.status_code)
