# Raspberry Pi Pico 2 microPython Blinky
# Write your code here :-)
import machine
import time

led = machine.Pin(25, machine.Pin.OUT) # Onboard LED is connected to GPIO 25

while True:
    led.value(1)  # Turn the LED on (set to 1)
    time.sleep(2)  # Wait for 1 second
    led.value(0)  # Turn the LED off (set to 0)
    time.sleep(1)  # Wait for 1 second
