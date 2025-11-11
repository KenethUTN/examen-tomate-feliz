# 1. Sensores a Utilizar (10 pts)

## Lista de Sensores Seleccionados

| Sensor | Modelo Real | Función en el Invernadero | Justificación |
|--------|-------------|----------------------------|---------------|
| **DHT11** | Módulo negro de 3 pines | Mide **temperatura** y **humedad del aire** | Ideal para monitorear clima del tomate (óptimo: 20-30°C, 60-80% HR) |
| **Water Level Sensor** | Rojo con "dientes" metálicos | Mide **nivel de agua** en 1 tanque (simula los 10) | Detecta si hay suficiente agua de lluvia recolectada |
| **Soil Moisture Sensor** | Blanco (puntas) + placa azul | Mide **humedad del suelo** | Activa riego si la tierra está seca |
| **Photoresistor (LDR)** | Sensor gris suelto (2 patitas) | Mide **intensidad de luz** | Verifica si hay suficiente luz solar (mínimo 6 horas/día) |
| **Relay 5V** | SRD-05VDC-SL-C (azul) | Controla **bomba de riego** | Enciende/apaga el riego automáticamente |
| **Active Buzzer** | Negro con zumbador | **Alerta sonora** | Pita si el tanque está vacío |

---

## Por qué usamos **solo estos 6 sensores/actuadores**:

- Son **los más simples** y **disponibles en el laboratorio**.  
- Cumplen con **todos los requisitos del examen** sin complicaciones.  
- No necesitamos WiFi → usamos **cable USB** (Arduino UNO).  
- Todo se simula en **Tinkercad** y se guarda en **Python + MongoDB local**.

> **Nota para el profesor (york):**  
> Se usó Arduino UNO R3 en lugar de ESP32 por simplicidad educativa.  
> La conectividad es **serial USB** hacia PC (Python recibe datos en tiempo real).

---
