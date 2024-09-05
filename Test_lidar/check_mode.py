import Jetson.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()

print(mode)
