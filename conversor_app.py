import streamlit as st

st.write("""
# Simples Conversor de Área 

Converte quilômetros quadrados para hectares

""")

# INPUT: área em km²
area_km2 = st.number_input("Área (km²):")

# Conversão
area_ha = area_km2 * 100

# Confere se botão foi pressionado
if(st.button('Converter')):
 
    # Print área em hectares
    st.text("Área: {} ha".format(area_ha))
