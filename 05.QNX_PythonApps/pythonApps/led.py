import rpi_gpio as GPIO
import time

GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.LOW)

while True:
	GPIO.output(2,GPIO.HIGH)
	print("Set GPIO 2 : HIGH")
	time.sleep(0.5)
	GPIO.output(2,GPIO.LOW)
	print("Set GPIO 2 : LOW")
	time.sleep(0.5)
