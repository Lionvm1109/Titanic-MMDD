
# Analisis de datos del Titanic

## Descripcion del proyecto

Este proyecto consiste en realizar un analisis exploratorio de datos de los pasajeros del Titanic utilizando Python.

El objetivo es conocer las caracteristicas de los pasajeros e identificar posibles relaciones entre sus datos y la supervivencia durante el hundimiento del barco.

Para realizar el analisis se utiliza el dataset `train.csv`, obtenido de la competencia Titanic de Kaggle.

## Objetivo

Analizar y procesar los datos de los pasajeros del Titanic mediante herramientas de Python, utilizando las librerias Pandas y Matplotlib para obtener informacion, realizar calculos y representar los resultados mediante graficas.

## Herramientas utilizadas

- Python
- Pandas
- Matplotlib
- Visual Studio Code
- Git y GitHub

## Dataset

El proyecto utiliza el archivo `train.csv`, que contiene informacion de 891 pasajeros y 12 variables.

Entre las principales variables se encuentran:

| Variable | Descripcion |
|---|---|
| PassengerId | Identificador del pasajero |
| Survived | Supervivencia: 0 = No, 1 = Si |
| Pclass | Clase del pasajero |
| Name | Nombre del pasajero |
| Sex | Sexo del pasajero |
| Age | Edad del pasajero |
| SibSp | Hermanos o conyuges a bordo |
| Parch | Padres o hijos a bordo |
| Ticket | Numero del boleto |
| Fare | Tarifa pagada |
| Cabin | Cabina del pasajero |
| Embarked | Puerto de embarque |

Fuente del dataset:

https://www.kaggle.com/c/titanic/data

## Analisis realizado

Durante el desarrollo del proyecto se realizaron las siguientes actividades:

1. Carga del dataset utilizando Pandas.
2. Exploracion de los primeros registros.
3. Identificacion del numero de pasajeros y columnas.
4. Revision de las variables disponibles y sus tipos de datos.
5. Identificacion de valores faltantes y calculo de porcentajes.
6. Deteccion de registros duplicados.
7. Obtencion de estadisticas descriptivas.
8. Analisis de la supervivencia de los pasajeros.
9. Analisis de las edades, cabinas y puertos de embarque.
10. Creacion de nuevas variables.
11. Comparacion de la supervivencia segun diferentes caracteristicas.
12. Representacion de resultados mediante graficas.

## Variables nuevas

Durante el procesamiento de los datos se crearon las siguientes variables:

### FamilySize

Representa el numero de integrantes de la familia que viajaban juntos, incluyendo al propio pasajero.

Formula:

FamilySize = SibSp + Parch + 1

### AgeGroup

Clasifica las edades de los pasajeros en cuatro categorias:

- Nino: de 0 a menos de 18 años.
- Joven: de 18 a menos de 30 años.
- Adulto: de 30 a menos de 60 años.
- Adulto mayor: 60 años o mas.

Los pasajeros sin edad registrada no reciben una categoria.

## Preguntas de analisis

El proyecto busca responder las siguientes preguntas:

- ¿Que porcentaje de pasajeros sobrevivio?
- ¿Como cambia la supervivencia entre hombres y mujeres?
- ¿Como cambia la supervivencia segun la clase del pasajero?
- ¿Que grupos de edad presentan mayor supervivencia?
- ¿Viajar solo o acompañado parece estar relacionado con la supervivencia?
- ¿Existe alguna relacion entre la tarifa pagada y la supervivencia?

## Graficas generadas

El programa utiliza Matplotlib para crear representaciones visuales de los datos, incluyendo:

- Grafica de valores faltantes.
- Histograma de edades.
- Grafica de pasajeros por puerto de embarque.
- Grafica de supervivencia.
- Grafica de porcentaje de supervivencia.
- Grafica del tamaño de las familias.
- Grafica de supervivencia por sexo, clase, edad y acompañamiento.
- Grafica de tarifa promedio segun supervivencia.

## Instalacion y ejecucion

### 1. Clonar el repositorio

```bash
git clone URL_DE_TU_REPOSITORIO
```

Entrar a la carpeta del proyecto:

```bash
cd Titanic-MMDD
```

### 2. Crear un entorno virtual

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

En Windows, utilizando PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar el programa

```bash
python analisis.py
```

## Estructura del proyecto

```text
Titanic-MMDD/
│
├── .venv/
├── analisis.py
├── train.csv
├── gender_submission.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## Resultados y conclusiones

El analisis permite observar diferencias en la supervivencia de los pasajeros segun sus caracteristicas.

Se estudian variables como el sexo, la clase, la edad, el acompañamiento familiar y la tarifa pagada para identificar patrones y diferencias en los porcentajes de supervivencia.

Los resultados obtenidos son descriptivos y permiten explorar asociaciones entre las variables, pero no demuestran por si mismos que una caracteristica haya causado la supervivencia.

## Autor

Proyecto academico de analisis y procesamiento de datos.

## Licencia y uso

Proyecto desarrollado con fines educativos, utilizando datos publicos de la competencia Titanic de Kaggle.