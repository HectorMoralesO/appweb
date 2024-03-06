import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import streamlit as st

        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
map_button = st.button('Construir mapa de árbol') # crear un botón construir mapa de árbol
box_button = st.button('Construir diagramas de caja y brazos') # crear otro botón construir diagramas de caja y brazos 
hist_button = st.button('Construir histograma') # crear otro botón construir histograma
scatter_button = st.button('Construir diagrama de dispersión') # crear otro botón construir diagrama de dispersión 
        
if map_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Los autos convertibles nuevos son los más caros.')
            
    # crear un mapa de árbol
    car_data_type_condition = car_data.dropna(subset=['price'])
    car_data_type_condition_price = car_data_type_condition.groupby(['type', 'condition']).mean().reset_index() # Agrupar datos por las variables "type" y "condition"
    fig = px.treemap(car_data_type_condition, path=[px.Constant("Tipos de carros por precio"), 'type', 'condition'], values='days_listed',
                  color='price',
                  color_continuous_scale='RdBu')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)



if box_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Pocos autos convertibles nuevos están en venta, lo cual contrasta con la cantidad de pickups nuevas.')
                
    # crear gráfico de caja y brazos
    
    car_new_coupe_price = car_data[(car_data["type"]=="coupe")  & (car_data["condition"]=="new")]["price"]
    car_new_convertible_price = car_data[(car_data["type"]=="convertible")  & (car_data["condition"]=="new")]["price"]
    car_new_pickup_price = car_data[(car_data["type"]=="pickup")  & (car_data["condition"]=="new")]["price"]
    car_new_truck_price = car_data[(car_data["type"]=="truck")  & (car_data["condition"]=="new")]["price"]

    x_data = ['Coupe', 'Pickup',
            'Truck', 'Convertible']


    y_data = [car_new_coupe_price,  car_new_pickup_price, car_new_truck_price, car_new_convertible_price]

    colors = ['rgba(93, 164, 214, 0.5)', 'rgba(255, 144, 14, 0.5)', 'rgba(44, 160, 101, 0.5)',
            'rgba(255, 65, 54, 0.5)']

    fig2 = go.Figure()

    for xd, yd, cls in zip(x_data, y_data, colors):
            fig2.add_trace(go.Box(
                y=yd,
                name=xd,
                boxpoints='all',
                jitter=0.5,
                whiskerwidth=0.2,
                fillcolor=cls,
                marker_size=2,
                line_width=1)
            )

    fig2.update_layout(
        title='Tipos de carros más caros',
        yaxis=dict(
            autorange=True,
            showgrid=True,
            zeroline=True,
            dtick=5,
            gridcolor='rgb(255, 255, 255)',
            gridwidth=1,
            zerolinecolor='rgb(255, 255, 255)',
            zerolinewidth=2,
        ),
        margin=dict(
            l=40,
            r=30,
            b=80,
            t=100,
        ),
        paper_bgcolor='rgb(243, 243, 243)',
        plot_bgcolor='rgb(243, 243, 243)',
        showlegend=False
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('La pickup con más anuncios es la ford f150 y tiene un precio promedio de $14,105.92.')
                
    # Histograma
    ford_f150_price = car_data[car_data["model"]=="ford f-150"]["price"]
    hist_data = [ford_f150_price]
    group_labels = ['Precio Ford f150']
    colors = ['#F66095']

    fig3 = ff.create_distplot(hist_data, group_labels, colors=colors, bin_size=1000)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig3, use_container_width=True)


if scatter_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Se observa una relación inversa entre las variables odómetro y precio. Además, no necesariamente los vehículos en mejores condiciones han sido utilizados en menor medida.')
                
    # Diagrama de dispersión
    ford_f150 = car_data[car_data["model"]=="ford f150"]
    fig4 = px.scatter(ford_f150, x="price", y="odometer", color="condition", trendline="ols")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig4, use_container_width=True)
