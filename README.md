# Proyecto_6
Proyecto sobre vehiculos en EEUU

Descripción del proyecto: 

Paso 1: se comenzo con los siguientes puntos.
El proyecto comenzo con un repositorio en github con readme y .gitignore.
Se creo una cuenta en render.com 
se creo un ambiente virtual proyecto_6_vehiculos
en este ambiente virtual se descargarón las librerias pandas, plotly.express, streamlit y nbformat.
Se clono el repositorio en VS code se configuro el interprete de python.
se agrego el archivo requirements con las librerias

Paso 2: Descarga de los archivos de datos
Se descargo el arvicho vehicles_us.csv y se coloco en el conjuto de datos del directorio del proyecto

Paso 3: EDA
Se creo un directorio llamado notebook en el directorio del proyecto
se creo un notebook llamado EDA.ipynb para interactuar con la data y plotly.express

Paso 4: Desarrollo del cuadro de mandos de la aplicación WEB
Se creo el archivo app.py en la raiz del directorio se importo las librerias pandas, streamlit y plotly.express
Se leyo el archivo vehicles_us.csv
Se creo 4 botones con encabezados, 2 histogramas  y 2 scatters con funciones st.write() y st.plotly_chart()


Objetivo del proyecto:

Desplegar la aplicación web en render desde el repositorio https://github.com/yonathanaes/Proyecto_6.git.
La pagina web se compone de 4 partes cada parte esta representada en botones que muestra un gráfico que representa datos de la venta de vehiculos.

Botones:
1. Construir histograma de kilometraje: Muestra la distribución del kilometraje, la mayoría de los vehículos tiene un kilometraje de 100k.
2. Construir histograma de año del modelo: Muestra la distribución del año del modelo, la mayoría de los vehículos son del año 2006 en adelante.
3. Construir gráfico de dispersión del año del modelo y precio: La dispersión del año del modelo y precio muestra la relación positiva a mayor año del modelo (reciente modelo) mayor precio.
4. Construir gráfico de dispersión del kilometraje y precio: La dispersión del kilometraje y precio muestra la relación negativa a mayor kilometraje(más usado) menor precio.

Conclución del proyecto:
El proyecto se trabajo en 4 pasos desde crear un repositorio, clonarlo en VCcode, crear un ambiente virtual donde pueda descargar mis librerias especificas para este proyecto y un trabajar con un interprete de python.
Esto me permitio importar librerias por ejemplo plotly.express para crear botones y graficos como histogramas, la libreria streamlit me permite desplegarlo localmente y posterior en la web mediante render.