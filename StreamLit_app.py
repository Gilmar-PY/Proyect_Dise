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
      

####

#####################################################################################################################
#### grafica para elsensor de Ph 
import streamlit as st
import serial
import time
import matplotlib.pyplot as plt
import numpy as np

# Configuración de la interfaz de Streamlit
st.title("Lectura de datos desde Arduino")

# Configura el puerto serie para leer los datos de Arduino
arduino = serial.Serial('/dev/ttyACM0', 9600)  # Asegúrate de seleccionar el puerto correcto
time.sleep(2)  # Espera a que se establezca la conexión Serial

# Listas para almacenar el tiempo y los datos del sensor
x = []
y = []

# Crea una figura vacía
fig, ax = plt.subplots()

# Contenedor para mostrar la imagen
imagen = st.empty()

# Índice para el tiempo
i = 0

# Lee los datos del puerto serie
while True:
    if arduino.inWaiting() > 0:
        # Lee una línea de datos del puerto serie y la decodifica
        dato = arduino.readline().decode().rstrip()

        # Actualiza la gráfica
        x.append(i)
        y.append(float(dato))
        i += 1
        ax.clear()
        ax.plot(x, y)
        ax.set_xlabel('Tiempo')
        ax.set_ylabel('Valor del sensor pH')

        # Actualiza la imagen en Streamlit
        imagen.pyplot(fig)

        # Espera un poco antes de leer los siguientes datos
        plt.pause(0.01)
############################################
'''pinterpretacion:
En la gráfica que estás generando en Streamlit, el eje X representa el tiempo y 
el eje Y representa los valores leídos del sensor de pH.

Si tienes tres mediciones de pH (pH1, pH2, pH3) que estás leyendo y graficando, cada una de ellas
sería una línea separada en la gráfica. Cada línea mostraría cómo cambia el valor de esa medida de pH específica con
el tiempo.Interpretar estos valores dependerá de los que estés tratando de lograr con tu proyecto. En general,
el pH es una medida de cuán ácida o básica es una solución. Un pH de 7 es 

neutro, valores inferiores a 7 son ácidos y valores superiores a 7 son básicos.
Por lo tanto, si estás graficando las lecturas de un sensor de pH en agua, por ejemplo, 
podrías estar interesado en ver si el pH se mantiene constante (lo que podría indicar agua limpia y estable)
o si fluctúa (lo que podría indicar contaminación o algún otro cambio en el agua).'''
########################################################################################################################
