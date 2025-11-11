# 4. Monitorización (20 pts)

## Variables Monitorizadas

| Variable | Sensor | Rango Esperado | Frecuencia |
|---------|--------|----------------|------------|
| **Temperatura** | DHT11 | 20–30 °C | Cada 2 seg |
| **Humedad Aire** | DHT11 | 60–80 % | Cada 2 seg |
| **Nivel de Agua** | Water Level | 0–480 L (0–1023) | Cada 2 seg |
| **Humedad Suelo** | Soil Sensor | 0–1023 (seco: <300) | Cada 2 seg |
| **Luz Solar** | LDR | 0–1023 (día: >500) | Cada 2 seg |

---

## Formato de Datos Enviados (Serial)

TEMP:25.5,HUM:65,AGUA:320,SUELO:45,LUZ:780


- **Python** recibe esta línea cada 2 segundos.  
- **Parsea** con `split(',')` y guarda en **MongoDB**.

---

## Ejemplo de Documento en MongoDB

```json
{
  "timestamp": "2025-11-11T14:11:22",
  "temperatura": 25.5,
  "humedad_aire": 65,
  "nivel_agua": 320,
  "humedad_suelo": 45,
  "luz": 780
}Colección: invernadero_tomates
Base de datos: tomate_feliz_db
