
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


# ==========================================
# 1. VALORES FALTANTES Y SUS PORCENTAJES
# ==========================================

print("\n===== VALORES FALTANTES =====")

faltantes = datos.isnull().sum()

print(faltantes)

print("\n===== PORCENTAJE DE VALORES FALTANTES =====")

porcentaje = datos.isnull().mean() * 100

print(porcentaje.round(2))


# ==========================================
# 2. REGISTROS DUPLICADOS
# ==========================================

print("\n===== REGISTROS DUPLICADOS =====")

duplicados = datos.duplicated().sum()

print("Cantidad de duplicados:", duplicados)


# ==========================================
# 3. ESTADISTICAS DESCRIPTIVAS
# ==========================================

print("\n===== ESTADISTICAS DESCRIPTIVAS =====")

print(datos.describe())

print("\n===== ESTADISTICAS DE TODAS LAS VARIABLES =====")

print(datos.describe(include="all"))



# CREAR VARIABLES NUEVAS


# 1. Crear la variable FamilySize
# Suma hermanos, pareja, padres e hijos, mas el pasajero

datos["FamilySize"] = datos["SibSp"] + datos["Parch"] + 1

print("\n===== TAMANO DE LA FAMILIA =====")
print(datos[["SibSp", "Parch", "FamilySize"]].head())


# 2. Crear categorias de edad

datos["AgeGroup"] = pd.cut(
    datos["Age"],
    bins=[0, 18, 30, 60, float("inf")],
    labels=["Nino", "Joven", "Adulto", "Adulto mayor"],
    right=False
)

print("\n===== CATEGORIAS DE EDAD =====")
print(datos[["Age", "AgeGroup"]].head())


# 3. Contar pasajeros por categoria de edad

print("\n===== CANTIDAD POR CATEGORIA =====")
print(datos["AgeGroup"].value_counts())


# 4. Contar pasajeros por tamano de familia

print("\n===== TAMANO DE FAMILIA =====")
print(datos["FamilySize"].value_counts().sort_index())







# ==========================================
# 4. ANALISIS DE SUPERVIVENCIA
# ==========================================

print("\n===== ANALISIS DE SUPERVIVENCIA =====")

sobrevivieron = (datos["Survived"] == 1).sum()

no_sobrevivieron = (datos["Survived"] == 0).sum()

print("Sobrevivieron:", sobrevivieron)

print("No sobrevivieron:", no_sobrevivieron)


# Calcular porcentajes

porcentaje_sobrevivientes = sobrevivieron / total * 100

porcentaje_no_sobrevivientes = no_sobrevivieron / total * 100

print("\nPorcentaje de sobrevivientes:",
      round(porcentaje_sobrevivientes, 2), "%")

print("Porcentaje de no sobrevivientes:",
      round(porcentaje_no_sobrevivientes, 2), "%")


# Crear tabla de resultados

resultados = pd.DataFrame({
    "Estado": ["Sobrevivieron", "No sobrevivieron"],
    "Cantidad": [sobrevivieron, no_sobrevivieron]
})

print("\n===== TABLA DE RESULTADOS =====")

print(resultados)


# ==========================================
# 5. ANALISIS DE EDAD (AGE)
# ==========================================

print("\n===== ANALISIS DE EDAD =====")

print("Edades faltantes:", datos["Age"].isnull().sum())

print("Edad promedio:", datos["Age"].mean())

print("Edad minima:", datos["Age"].min())

print("Edad maxima:", datos["Age"].max())

print("Mediana de edad:", datos["Age"].median())


# ==========================================
# 6. ANALISIS DE CABINAS (CABIN)
# ==========================================

print("\n===== ANALISIS DE CABINAS =====")

print("Cabinas faltantes:", datos["Cabin"].isnull().sum())

print("Cabinas registradas:", datos["Cabin"].notnull().sum())

print("\nCabinas mas frecuentes:")

print(datos["Cabin"].value_counts().head())


# ==========================================
# 7. ANALISIS DE PUERTOS (EMBARKED)
# ==========================================

print("\n===== ANALISIS DE EMBARKED =====")

print("Embarques faltantes:", datos["Embarked"].isnull().sum())

print("\nCantidad de pasajeros por puerto:")

print(datos["Embarked"].value_counts())

if not datos["Embarked"].dropna().empty:

    print("\nPuerto mas frecuente:")

    print(datos["Embarked"].mode()[0])


# ==========================================
# 8. GRAFICA DE VALORES FALTANTES
# ==========================================

print("\n===== GRAFICA DE VALORES FALTANTES =====")

faltantes_grafica = faltantes[faltantes > 0]

if not faltantes_grafica.empty:

    faltantes_grafica.plot(kind="bar")

    plt.title("Valores faltantes por variable")
    plt.xlabel("Variables")
    plt.ylabel("Cantidad de valores faltantes")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()

else:

    print("No hay valores faltantes.")


# ==========================================
# 9. GRAFICA DE EDADES
# ==========================================

datos["Age"].dropna().plot(
    kind="hist",
    bins=20,
    edgecolor="black"
)

plt.title("Distribucion de edades de los pasajeros")
plt.xlabel("Edad")
plt.ylabel("Cantidad de pasajeros")

plt.tight_layout()

plt.show()


# ==========================================
# 10. GRAFICA DE PUERTOS DE EMBARQUE
# ==========================================

datos["Embarked"].value_counts().plot(kind="bar")

plt.title("Pasajeros por puerto de embarque")
plt.xlabel("Puerto")
plt.ylabel("Cantidad de pasajeros")

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()


# ==========================================
# 11. GRAFICA DE SUPERVIVENCIA
# ==========================================

resultados.plot(
    kind="bar",
    x="Estado",
    y="Cantidad",
    legend=False
)

plt.title("Supervivencia de los pasajeros del Titanic")
plt.xlabel("Estado")
plt.ylabel("Cantidad de pasajeros")

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()


# ==========================================
# 12. GRAFICA DE PASTEL
# ==========================================

plt.pie(
    resultados["Cantidad"],
    labels=resultados["Estado"],
    autopct="%1.1f%%"
)

plt.title("Porcentaje de supervivencia")

plt.tight_layout()

plt.show()

