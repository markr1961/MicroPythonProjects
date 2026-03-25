## ESP32-S3 Matrix board
Code for the [Waveshare ESP32-S3 Matrix](https://www.waveshare.com/esp32-s3-matrix.htm) dev board. 
Includes instructions on using ESP-IDF.

<B>DO NOT RUN WITH HIGH BRIGHTNESS! </B>
Apparently the problem is the 5v->3.3V regulator, not the LEDs themselves. 
There is 1A series diode on the USB input. WS2812B @ 20mA/LED → 60mA/pixel, 64 pixel → 3.840A!

### Documentation
schematic: https://files.waveshare.com/wiki/ESP32-S3-Matrix/ESP32-S3-Matrix-Sch.pdf  
pinout: https://www.waveshare.com/w/upload/2/25/ESP32-S3-Matrix_OR.png  
wiki: [ESP32-S3-Matrix - Waveshare Wiki](https://www.waveshare.com/wiki/ESP32-S3-Matrix)

### [QMI8658](https://qstcorp.com/upload/pdf/202202/QMI8658C%20datasheet%20rev%200.9.pdf) QST 6-axis sensor 
Onboard [QMI8658 QST 6-axis sensor](https://jutland.atlassian.net/wiki/x/BwAVHQ) (3-axis accel, 3-axis gyro) Arduino and Circuit Python drivers available.  
At least partially compatible with BMI160.  
