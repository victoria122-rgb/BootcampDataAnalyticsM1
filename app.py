import streamlit as st

st.title("Bootcamp Data Analytics for oil and gas")
st.sidebar.title("Parametros")

modulos = st.sidebar.selectbox("Seleccion un modulo",["Introduccion a variables","Funciones", "POO"])

if modulos == "Introduccion a variables":
        Pozo = "SPE-001"
        Petroleo_bppd = 1250
        Agua_bpd = 350.50
        Status = True
       
        st.write("Pozo:", Pozo)
        st.write("Petroleo_bppd:", Petroleo_bppd)
        st.write("Agua_bpd:", Agua_bpd)
        st.write("Status:", Status)

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
          
        relacion_presion = presion_fondo/presion_yacimiento
        caudal = caudal_maximo*(1-0.2*relacion_presion-0.8*(relacion_presion**2))
        return round(caudal, decimales)

    caudal_maximo = st.number_input("Ingrese el caudal_maximo", min_value = 0, max_value = 5000, value = 1200)
    presion_yacimiento = st.number_input("Ingrese presion de yacimiento", min_value = 0, max_value = 9000, value = 3000)
    presion_fondo = st.number_input("Ingrese la presion de fondo", min_value = 0, max_value = 9000, value = 1500)
    decimales = st.slider("Ingrese decimales para su calculo", min_value = 0, max_value = 4, value = 2)
    caudal = calcular_caudal_vogel(caudal_maximo, presion_yacimiento, presion_fondo, decimales)
    st.write("El caudal es:", caudal)
elif modulos == "POO":
        class Pozo:
          def __init__(self, nombre, campo, petroleo, agua):
            self.nombre = nombre
            self.campo = campo
            self.petroleo = petroleo
            self.agua = agua
          def mostrar_informacion(self):
            st.write("Pozo:", self.nombre)
            st.write("Campo:", self.campo)
            st.write("Petroleo:", self.petroleo, "BPD")
            st.write("Agua:", self.agua, "BPD")
          def produccion_total(self):
            total_produccion = self.petroleo + self.agua
            return total_produccion
          def proyectar_produccion(self, dias):
            produccion_proyectada = (self.petroleo + self.agua) * dias
            return produccion_proyectada

        nombre_pozo = st.text_input("Ingrese el nombre del pozo")
        campo_pozo = st.text_input("Ingrese el campo del pozo")
        petroleo = st.number_input("Ingrese produccion de petroleo", min_value = 0, max_value = 5000, value = 1000)
        agua = st.number_input("Ingrese produccion de agua", min_value = 0, max_value = 5000, value = 200)

        pozo = Pozo(nombre_pozo,campo_pozo,petroleo,agua)
        st.write(pozo.mostrar_informacion())
        st.write(pozo.produccion_total())
        dias = st.number_input("Ingrese los dias a proyectar", min_value = 0, max_value = 365, value = 30)
        st.write(pozo.proyectar_produccion(dias))	
