'''codigo simplificado del turbidez de agua :

void loop() {
  float ValorSensor = analogRead(A0);
  float Voltaje = (ValorSensor) * (5 / 1024.0);
  float Turb = 194.23 * Voltaje + 44.038;
  Serial.println(Turb);
  delay(500);
}
'''

import streamlit as st
import serial
import matplotlib.pyplot as plt
import time

# Configuración de la interfaz de Streamlit
st.title("Lectura de datos desde Arduino")

# Configuración de la gráfica
fig, ax = plt.subplots()

# Listas para almacenar los datos de la gráfica
x = [i for i in range(50)]
y = [0 for _ in range(50)]

# Contenedor para mostrar la imagen
imagen = st.empty()

# Abrir el puerto serie
arduino = serial.Serial('COM3', 9600)

while True:
    if arduino.in_waiting > 0:
        # Lee una línea de datos del serial y la decodifica
        dato = arduino.readline().decode().rstrip()

        # Actualiza la gráfica
        y.append(float(dato))
        y.pop(0)
        ax.clear()
        ax.plot(x, y)
        ax.set_xlabel('Tiempo')
        ax.set_ylabel('Valor del sensor turbidez %')

        # Actualiza la imagen en Streamlit
        imagen.pyplot(fig)

        time.sleep(0.1)
