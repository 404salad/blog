## Overview
- **Arduino**: A board with a microcontroller, typically an **ATmega328**.
- **PWM Pins (~)**: Indicated by `~` on the Arduino pins, capable of **Pulse Width Modulation (PWM)**.  
  - **PWM**: Allows values other than on and off by precisely controlling frequency.  
  - Used to simulate analog output using `analogWrite()`, but still digital in nature.  

- **Analog Pins**: Real analog input pins are available on the Arduino.

## Pin Information
- **Pin 13**: Same as the built-in LED pin.
- **TX and RX LEDs**: Indicate when the Arduino is transmitting (TX) or receiving (RX) data.
- **Reset Button**: Resets the code but does not clear the memory.

## Serial Communication
- **`Serial.begin(9600);`**: Initializes serial communication at 9600 baud rate.
- **`Serial.print();`**: Prints data to the serial monitor without a newline.
- **`Serial.println();`**: Prints data to the serial monitor with a newline.

## Logic Levels
- **HIGH**: Equivalent to `true` or `1`.
- **LOW**: Equivalent to `false` or `0`.

## Variables
- Use **`static int`** for variables to persist their value across function calls instead of declaring global variables.

## ADC (Analog-to-Digital Conversion)
- Converts voltage values from **0V to 5V** into digital values ranging from **0 to 1023**.

## Key Functions
### Digital I/O
- **`digitalRead(pin)`**: Reads the state (HIGH or LOW) of a digital pin.
- **`digitalWrite(pin, value)`**: Sets a digital pin to HIGH or LOW.

### Analog I/O
- **`analogRead(pin)`**: Reads the value from an analog pin (0 to 1023).
- **`analogWrite(pin, value)`**: Outputs PWM signal (0 to 255) for controlling LED brightness or motor speed.  
  - Can only be used with **PWM pins** (`~`).

## PWM Details
- **Duty Cycle**: Fraction of the period during which the voltage is HIGH.  
  - `analogWrite(0)` → 0% duty cycle  
  - `analogWrite(64)` → 25% duty cycle  
  - `analogWrite(127)` → 50% duty cycle  
  - `analogWrite(191)` → 75% duty cycle  
  - `analogWrite(255)` → 100% duty cycle  
- PWM is used to control things like **LED brightness** and **motor speed**.

---

