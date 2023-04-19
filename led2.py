import RPi.GPIO as GPIO
import time
import LedPULL as pul
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(12, GPIO.OUT)

led_on = False

while True:
	
	if GPIO.input(11) == GPIO.LOW:
		led_on = not led_on
		print(pul.pulsador(led_on))
		time.sleep(0.2)
	#if led_on == True:
	#	GPIO.output(12, GPIO.HIGH)
	#	print('Led encendido')
	#if led_on == False:
	#	GPIO.output(12, GPIO.LOW)
	#	print('Led apagado')
