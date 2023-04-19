def pulsador(bandera):
	import RPi.GPIO as GPIO
	GPIO.setup(12, GPIO.OUT)
	if bandera == True:
		GPIO.output(12, GPIO.HIGH)
		print('Led encendido')
	if bandera == False:
		GPIO.output(12, GPIO.LOW)
		print('Led apagado')
	return ('acpetado')
	
