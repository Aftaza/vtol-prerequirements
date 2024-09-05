import RPi.GPIO as GPIO
import time

# Setup
BUZZER_PIN = 18  # Use the GPIO pin connected to the buzzer
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

def beep(duration):
    """Function to make the buzzer beep"""
    GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Turn on buzzer
    time.sleep(duration)                # Wait for the specified duration
    GPIO.output(BUZZER_PIN, GPIO.LOW)   # Turn off buzzer

try:
    while True:
        beep(1)  # Beep for 1 second
        time.sleep(1)  # Wait for 1 second
except KeyboardInterrupt:
    print("Program interrupted")

finally:
    GPIO.cleanup()  # Cleanup GPIO settings
