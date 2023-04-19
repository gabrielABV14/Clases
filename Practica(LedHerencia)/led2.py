import RPi.GPIO as GPIO		#Importamos las librerias para los pines GPIO, tiempo y uno propio (LedPULL), para simplificar le nombre se lo llama pul
import time
import LedPULL as pul
GPIO.cleanup()		#limpiamos todos los pines para volverlos a inicializar 
GPIO.setmode(GPIO.BOARD)	#Declaramos que el orden de los pines se define al orden fisico de la placa
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Delcaramos el pin 11 como entrada para le pulsador, aparte declarando al pin para la funcion pull_up
#GPIO.setup(12, GPIO.OUT)

led_on = False	#la bandera que define el estado del led

while True:
	if GPIO.input(11) == GPIO.LOW:	#leemos el pin del pulsador para poder entrar a cambiar a la bandera, para luego enviarla a LedPULL para realizar la tarea que cambia el estado del led
		led_on = not led_on
		print(pul.pulsador(led_on))	#enviamos la bandera y recibimos si la tarea se ejecuto con exito
		time.sleep(0.2)
	'''if led_on == True:
		GPIO.output(12, GPIO.HIGH)
		print('Led encendido')
	if led_on == False:
		GPIO.output(12, GPIO.LOW)
		print('Led apagado')'''
