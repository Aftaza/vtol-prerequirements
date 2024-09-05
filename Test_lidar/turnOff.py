import Jetson.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pin connected to the relay
relay_pin = 22  # Adjust this to your GPIO pin number

# Set up the GPIO pin as output
GPIO.setup(relay_pin, GPIO.OUT)

try:
    while True:
        # Turn the relay on (close the switch)
        GPIO.output(relay_pin, GPIO.LOW)

except KeyboardInterrupt:
    print("Exiting program")

finally:
    # Clean up GPIO on exit
    GPIO.cleanup()
