import streamlit as st

st.title("Bootcamp Data Analytics for oil and gas")
st.sidebar.title("Parametros")

modulos = st.sidebar.selectbox("Seleccion un modulo",["Introduccion a variables","Funciones"])

if modulos == "Introducion a variables":
    Pozo = "SPE-001"
    Petroleo_bppd = 1250
    Agua_bpd = 350.50
    Status = True
     
    st.write("Pozo")
    st.write("Petroleo_bppd")
    st.write("Agua_bpd")
    st.write("Status")

elif modulos == "Funciones":
    def calcular_caudal_vogel(caudal_maximo=1000, presion_yacimiento=3000, presion_fondo=200, decimales=2):
        """
            Calcula el caudal de petróleo utilizando el modelo de Vogel.
          
            Parámetros:
            caudal_maximo (float): Caudal máximo teórico del pozo, BPD.
            presion_yacimiento (float): Presión de yacimiento, psi.
            presion_fondo (float): Presión de fondo fluyente, psi.
            decimales (int): Número de decimales del resultado.
          
            Retorna:
            float: Caudal estimado de petróleo, BPD.
        """
          
        relacion_presion = presion_fondo/presion_yacimeinto
        caudal = caudal_maximo*(1-0.2*relacion_presion-0.8*(relacion_presion**2))
        return round(caudal, decimales)

    caudal_maximo = st.number_input("Ingrese el caudal maximo")
    presion_yacimiento = st.number_input("Ingrese presion de yacimiento")
    presion_fondo = st.number_input("Ingrese la presion de fondo")
    decimales = st.slider("Ingrese decimales para su calculo")

