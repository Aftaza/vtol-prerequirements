import time
import board
import busio
import adafruit_vl53l0x as lidar
import Jetson.GPIO as GPIO

# Set GPIO mode for Jetson Nano
GPIO.setmode(GPIO.TEGRA_SOC)

shut_pin_lidar1 = 'DAP4_SCLK'
shut_pin_lidar2 = 'UART2_RTS'
shut_pin_lidar3 = 'DAP4_FS'
shut_pin_lidar4 = 'DAP4_DIN'

GPIO.setup(shut_pin_lidar1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(shut_pin_lidar2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(shut_pin_lidar3, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(shut_pin_lidar4, GPIO.OUT, initial=GPIO.HIGH)

def change_sensor_address(i2c, current_address, new_address, shut_pin):
    try:
        GPIO.output(shut_pin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(shut_pin, GPIO.HIGH)
        time.sleep(0.1)

        sensor = lidar.VL53L0X(i2c, address=current_address)
        sensor.set_address(new_address)
        print(f"Address changed to: {hex(new_address)}")

        # Close sensor connection
        sensor = None
    except OSError as e:
        print(f"Error changing address for sensor with shutdown pin {shut_pin}: {e}")

i2c = busio.I2C(board.SCL, board.SDA)

# Attempt to change addresses
change_sensor_address(i2c, 0x29, 0x30, shut_pin_lidar1)
change_sensor_address(i2c, 0x29, 0x31, shut_pin_lidar2)
change_sensor_address(i2c, 0x29, 0x32, shut_pin_lidar3)
change_sensor_address(i2c, 0x29, 0x33, shut_pin_lidar4)

# Clean up GPIO
GPIO.cleanup()
