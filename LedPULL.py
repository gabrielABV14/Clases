def pulsador(bandera):	#obtenemos la bandera
	import RPi.GPIO as GPIO #volvemos a importar la libreria para ejecutar el estado de los pines
	GPIO.setup(12, GPIO.OUT)
	if bandera == True: #dependiendo del estado de la bandera que recibimos realizamos el cambio del estado del led a HIGH o LOW
		GPIO.output(12, GPIO.HIGH)
		print('Led encendido')
	if bandera == False:
		GPIO.output(12, GPIO.LOW)
		print('Led apagado')
	return ('acpetado') #Terminamos la tarea y enviamos a que se acepto la bandera, como tambien que la tarea fue realizada
	
