import streamlit as st
# Configuración de la interfaz de Streamlit
st. title ("Lectura de datos desde Arduino")
imagen=st.empty() ### contenedor para mostrar la imagen
 # Contenedor para mostrar la imagen
# Lee los datos del serial
while True:
  if arduino. in _waiting > 0
    # Lee una línea de datos del serial y la decodifica
    arduino.readline().decode().rstrip()
      # Actualiza la gráfica
  x. append(Len(x) 1)
  y. append (float (dato))
  ax. clear()
  ax.plot(x, y)
  ax.set xlabel('Tiempo',
  ax.set_ylabel('Valor de la humedad en %')
  #Actualiza la imagen en Streamlit
  imagen.pyplot(fig)
  plt. pause(0. 1)
st.write("hola mundo ")


