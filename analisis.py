import pandas as pd

# Cargar gender_submission.csv
df = pd.read_csv('gender_submission.csv')

# Realizar una exploración inicial:

# Número de pasajeros y Número de columnas
filas, columnas = df.shape
print(f"Número de pasajeros (filas): {filas}")
print(f"Número de columnas: {columnas}\n")

# Variables disponibles
print("Variables disponibles:")
print(df.columns.tolist())
print()

