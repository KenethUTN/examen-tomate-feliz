import serial
import time
from pymongo import MongoClient
from datetime import datetime

# --- CONEXIÓN SERIAL ---
ser = serial.Serial('COM3', 9600)  # Cambia COM3 si es necesario
time.sleep(2)

# --- CONEXIÓN MONGODB ---
client = MongoClient('mongodb://localhost:27017/')
db = client['tomate_feliz_db']
collection = db['invernadero_tomates']

print("Iniciando monitoreo...")

while True:
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print(f"Dato recibido: {line}")
            
            # Parsear: TEMP:25.5,HUM:65,AGUA:320,SUELO:45,LUZ:780
            datos = {}
            for item in line.split(','):
                key, value = item.split(':')
                datos[key.lower()] = float(value)
            
            # Agregar timestamp
            datos['timestamp'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            
            # Guardar en MongoDB
            collection.insert_one(datos)
            print("Guardado en MongoDB")
            
    except Exception as e:
        print(f"Error: {e}")
    
    time.sleep(1)
