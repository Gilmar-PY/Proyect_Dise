import streamlit as st
import serial

# Reemplace 'COM3' con el puerto correcto que su Arduino está utilizando
arduino = serial.Serial('COM3', 9600)

def read_from_arduino(arduino):
    while True:
        data = arduino.readline().decode('utf-8')
        if data:
            return data

def main():
    st.title("Leyendo datos del Arduino")

    if st.button("Leer datos"):
        data = read_from_arduino(arduino)
        st.write(data)

if __name__ == "__main__":
    main()

import streamlit as st
st.write("hola mundo ")


