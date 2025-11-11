# 2. Placa de Desarrollo (10 pts)

## Placa Utilizada: **Arduino UNO R3**

| Característica | Detalle |
|----------------|--------|
| **Microcontrolador** | ATmega328P |
| **Voltaje de operación** | 5V |
| **Pines digitales** | 14 (6 PWM) |
| **Pines analógicos** | 6 |
| **Memoria Flash** | 32 KB |
| **Conectividad** | USB (serial) |

---

## Justificación del Uso de Arduino UNO

- **Aprobado por el profesor (york)**.  
- **No requiere WiFi** → usamos **cable USB** a PC.  
- **Más simple que ESP32** para aprender conceptos básicos.  
- **Compatible con todos los sensores del laboratorio**.  
- **Simulación 100 % funcional en Tinkercad**.

> **Conectividad:**  
> Los datos se envían por **puerto serial (USB)** a Python en la PC.  
> Python los guarda en **MongoDB local**.

---
