import serial

BAUDS = 9600

puerto_serial = serial.Serial('COM3', BAUDS)

while True:
    archivo = open('pruebaSerial1.csv', 'a')
    if puerto_serial.in_waiting > 0:
        datos_obtenidos = puerto_serial.readline().decode('utf-8', errors='ignore').rstrip()
        archivo.write(f'{datos_obtenidos}\n')
        print(datos_obtenidos)

    archivo.close()

    