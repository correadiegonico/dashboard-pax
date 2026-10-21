import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Pax Manager", page_icon="📊", layout="wide")

st.title("📊 Dashboard de Control - Pax Manager")
st.write("Bienvenido al panel centralizado de métricas, ingresos y conciliaciones.")

# Menú lateral para navegar entre las secciones del negocio
menu = st.sidebar.selectbox(
    "Seleccioná una sección",
    ["Inicio", "Ingresos Previstos", "Eficacia Comercial", "WOLF Histórico / Estimación", "Consultas Recibos"]
)

if menu == "Inicio":
    st.header("Vista General")
    st.info("Utiliza el menú lateral para navegar entre los diferentes módulos de análisis financiero y operativo.")
    
elif menu == "Ingresos Previstos":
    st.header("📈 Ingresos Previstos")
    st.write("Seguimiento de contratos, pasajeros, montos brutos y estados pendientes.")
    # Aquí cargaremos el archivo correspondiente más adelante

elif menu == "Eficacia Comercial":
    st.header("🎯 Eficacia Comercial")
    st.write("Volumen de ventas por región y revenue por pasajero.")

elif menu == "WOLF Histórico / Estimación":
    st.header("🐺 WOLF Histórico / Estimación")
    st.write("Depósitos bancarios netos de Pago Fácil (cronograma de liquidación: Martes y Jueves).")

elif menu == "Consultas Recibos":
    st.header("🧾 Consultas Recibos")
    st.write("Gestión de datos de recibos diarios para alimentar las proyecciones de ingresos.")


