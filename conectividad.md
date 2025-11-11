# 3. Conectividad (10 pts)

## Método de Conectividad: **Serial USB (COM)**

| Característica | Detalle |
|----------------|--------|
| **Tipo** | Comunicación serial por cable USB |
| **Puerto** | COM3 / COM4 (según tu PC) |
| **Velocidad** | 9600 baudios |
| **Protocolo** | Comunicación asíncrona (Arduino → Python) |
| **Herramienta** | `pyserial` en Python |

## Diagrama de Flujo de Datos

Arduino UNO
↓ (cable USB)
Puerto Serial (COM)
↓ (Python con pyserial)
Base de Datos MongoDB Local


---

## Justificación

- **No se usa WiFi ni ESP32** →.  
- **Más simple y educativo** que redes inalámbricas.  
- **100 % funcional** con `Serial.println()` en Arduino.  
- Python recibe los datos en tiempo real y los guarda en MongoDB.

> **Ejemplo de dato enviado:**
> `TEMP:25.5,HUM:65,AGUA:320,SUELO:45,LUZ:780`

---
