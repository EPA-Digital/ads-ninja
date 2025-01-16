import streamlit as st
import polars as pl
import plotly.express as px
import numpy as np
import pandas as pd



# Configuración de la página
st.set_page_config(
    page_title="Dashboard de Marketing",
    layout="wide"
)

# Título
st.title("Dashboard de Marketing")

# Crear datos de ejemplo
data = {
    'Fecha': pd.date_range('2024-01-01', '2024-01-31'),
    'Impresiones': np.random.randint(1000, 5000, 31),
    'Clics': np.random.randint(50, 200, 31),
    'Conversiones': np.random.randint(5, 20, 31),
    'Costo': np.random.uniform(100, 500, 31)
}

df = pl.DataFrame(data)

# Sidebar para filtros
st.sidebar.header("Filtros")
fecha_inicio = st.sidebar.date_input(
    "Fecha Inicio",
    df['Fecha'].min()
)
fecha_fin = st.sidebar.date_input(
    "Fecha Fin",
    df['Fecha'].max()
)

# Filtrar datos
df_filtrado = df.filter(
    (pl.col('Fecha') >= fecha_inicio) & 
    (pl.col('Fecha') <= fecha_fin)
)

# Métricas principales
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Impresiones", 
              f"{df_filtrado['Impresiones'].sum():,.0f}")
    
with col2:
    st.metric("Total Clics", 
              f"{df_filtrado['Clics'].sum():,.0f}")
    
with col3:
    st.metric("Total Conversiones", 
              f"{df_filtrado['Conversiones'].sum():,.0f}")
    
with col4:
    st.metric("Costo Total", 
              f"${df_filtrado['Costo'].sum():,.2f}")

# Gráficos
fig1 = px.line(df_filtrado.to_pandas(), 
               x='Fecha', 
               y=['Impresiones', 'Clics'], 
               title='Tendencia de Impresiones y Clics')
st.plotly_chart(fig1)

fig2 = px.scatter(df_filtrado.to_pandas(), 
                 x='Clics', 
                 y='Conversiones',
                 size='Costo',
                 title='Relación entre Clics y Conversiones')
st.plotly_chart(fig2)
