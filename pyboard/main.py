# main.py -- put your code here!
import time
from pyb import LED
from pyb import Switch

led = LED(1)  # 1=red, 2=green, 3=yellow, 4=blue
sw = Switch()

print('Hello world!')
print('I can count:')
i = 1

while (sw.value() == False):
    print(i)
    i += 1
    for n in range(10):
        time.sleep_ms(100)  # Delay for 0.1 second.
        led.toggle()

print('done.')
