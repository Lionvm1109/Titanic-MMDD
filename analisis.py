
# Importar las librerias
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("train.csv")

# 5 registros
print("Primeros registros:")
print(datos.head())

# Informacion del archivo
print("\nInformacion del dataset:")
datos.info()

# Total de pasajeros
total = len(datos)

print("\nTotal de pasajeros:", total)