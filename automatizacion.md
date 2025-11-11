## Lógica de Control Implementada

| Condición | Acción | Actuador |
|----------|--------|----------|
| `humedad_suelo < 300` | Encender bomba 3 segundos | **Relay (pin 8)** |
| `nivel_agua < 100` | Emitir alerta sonora | **Buzzer (pin 9)** |
| `luz < 400` | (Opcional) Encender luz LED | No implementado |

---

## Código de Automatización (Arduino)

```cpp
if (suelo < 300) {
  digitalWrite(RELAY_PIN, LOW);  // Enciende bomba
  delay(3000);
  digitalWrite(RELAY_PIN, HIGH); // Apaga
}

if (agua < 100) {
  tone(BUZZER_PIN, 1000, 500);   // Pita 0.5 seg
}

Justificación

Riego automático solo cuando la tierra está seca.
Alerta sonora si falta agua en el tanque.
Todo controlado por Arduino UNO → simple y educativo.
No requiere internet → 100 % local y confiable.
