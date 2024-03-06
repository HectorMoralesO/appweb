# Anuncios de venta de autos

Este proyecto consiste en una aplicación web que realiza un análisis exploratorio de un conjunto de datos de anuncios de venta de autos en los Estados Unidos. 

La aplicación proporciona diversas funcionalidades para visualizar y analizar los datos de vehículos, incluyendo la construcción de un mapa de árbol, diagramas de caja y brazos, histogramas y diagramas de dispersión.

En esta aplicación los usuarios pueden explorar diferentes aspectos de estos datos, como el precio, el odómetro, el tipo de vehículo y su condición.


## Funcionalidades

- Botón `Contruir mapa de árbol`: Permite visualizar la distribución de precios de diferentes tipos de vehículos por su condición.
- Botón `Contruir diagrama de caja y brazos`: Permite comparar los precios de diferentes tipos de vehículos mediante diagramas de caja y brazos interactivos.
- Botón `Contruir histograma`: Muestra la distribución de precios de vehículos específicos, como la camioneta Ford F150.
- Botón `Contruir diagrama de dispersión`: Explora la relación entre el precio y el odómetro del modelo Ford F150.


## Requisitos de instalación

Para ejecutar la aplicación web, debes tener instalados los siguientes modulos de Python:

- `pandas`
- `plotly`
- `numpy`
- `streamlit`


## Cómo ejecutar esta aplicación

1. Clona el repositorio de este proyecto en tu equipo.
2. Abre una terminal y navega hasta la ubicación de la carpeta `appweb`.
3. Ejecuta el siguiente comando en tu terminal: `streamlit run app.py`.
4. Acede a `http://0.0.0.0:10000/` en tu navegador.
