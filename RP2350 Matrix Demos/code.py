import time
from machine import Pin
from WS2812 import LEDController

# Initialize RGB LED control pins
led_ctrl = LEDController(brightness=20)

def main():
    # Update the display
    led_ctrl.show()
    time.sleep_ms(1000)
    
    led_ctrl.clear()
    led_ctrl.show()
    time.sleep_ms(1000)
    

if __name__ == "__main__":
    main()
