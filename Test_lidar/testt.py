# import time
# import board
# import busio
# from adafruit_vl53l0x import VL53L0X

# # Initialize I2C and sensor
# i2c = busio.I2C(board.SCL, board.SDA)
# try:
#     sensor = VL53L0X(i2c)
#     print("VL53L0X sensor initialized.")
# except Exception as e:
#     print(f"Failed to initialize sensor: {e}")
#     exit(1)

# while True:
#     try:
#         distance = sensor.range
#         print(f"Distance: {distance} mm")
#     except Exception as e:
#         print(f"Error reading distance: {e}")
#     time.sleep(1)


 


import time
import board
import busio
import adafruit_vl53l0x as lidar
import Jetson.GPIO as GPIO

# Set GPIO mode for Jetson Nano
GPIO.setmode(GPIO.TEGRA_SOC)

shut_pin_lidar1 = 'DAP4_SCLK'
# shut_pin_lidar2 = 'UART2_RTS'
# shut_pin_lidar3 = 'DAP4_FS'
# shut_pin_lidar4 = 'DAP4_DIN'


GPIO.setup(shut_pin_lidar1, GPIO.OUT, initial=GPIO.HIGH)
# GPIO.setup(shut_pin_lidar2, GPIO.OUT, initial=GPIO.HIGH)
# GPIO.setup(shut_pin_lidar3, GPIO.OUT, initial=GPIO.HIGH)
# GPIO.setup(shut_pin_lidar4, GPIO.OUT, initial=GPIO.HIGH)

# Function to change sensor address
def change_sensor_address(i2c, current_address, new_address, shut_pin):
    GPIO.output(shut_pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(shut_pin, GPIO.HIGH)
    time.sleep(0.1)

    sensor = lidar.VL53L0X(i2c, address=current_address)
    sensor.set_address(new_address)
    print(f"Address changed to: {hex(new_address)}")

    sensor = None

i2c = busio.I2C(board.SCL, board.SDA)
change_sensor_address(i2c, 0x29, 0x30, shut_pin_lidar1)
# change_sensor_address(i2c, 0x29, 0x31, shut_pin_lidar2)
#change_sensor_address(i2c, 0x29, 0x32, shut_pin_lidar3)
# change_sensor_address(i2c, 0x29, 0x33, shut_pin_lidar4)

# Clean up GPIO
GPIO.cleanup()




# import time
# import board
# import busio
# import adafruit_vl53l0x as lidar
# import Jetson.GPIO as GPIO

# # Set GPIO mode for Jetson Nano
# GPIO.setmode(GPIO.TEGRA_SOC)

# shut_pin_lidar1 = 'DAP4_SCLK'
# shut_pin_lidar2 = 'UART2_RTS'
# shut_pin_lidar3 = 'DAP4_FS'
# shut_pin_lidar4 = 'DAP4_DIN'


# GPIO.setup(shut_pin_lidar1, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(shut_pin_lidar2, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(shut_pin_lidar3, GPIO.OUT, initial=GPIO.LOW)
# GPIO.setup(shut_pin_lidar4, GPIO.OUT, initial=GPIO.LOW)

# # Function to change sensor address
# def change_sensor_address(i2c, current_address, new_address, shut_pin):
#     GPIO.output(shut_pin, GPIO.LOW)
#     time.sleep(0.1)
#     GPIO.output(shut_pin, GPIO.HIGH)
#     time.sleep(0.1)

#     sensor = lidar.VL53L0X(i2c, address=current_address)
#     sensor.set_address(new_address)
#     print(f"Address changed to: {hex(new_address)}")

#     sensor = None

# i2c = busio.I2C(board.SCL, board.SDA)
# change_sensor_address(i2c, 0x29, 0x30, shut_pin_lidar1)
# change_sensor_address(i2c, 0x29, 0x31, shut_pin_lidar2)
# change_sensor_address(i2c, 0x29, 0x32, shut_pin_lidar3)
# change_sensor_address(i2c, 0x29, 0x33, shut_pin_lidar4)

# # Clean up GPIO
# GPIO.cleanup()








# import time
# import board
# import busio
# import adafruit_vl53l0x as vl53l0x

# def initialize_sensors():
#     i2c = busio.I2C(board.SCL, board.SDA)
    
#     # Initialize sensor with default address
#     sensor1 = vl53l0x.VL53L0X(i2c, address=0x30)
    
#     return sensor1

# def read_distances(sensor1):
#     while True:
#         try:
#             # Read distance
#             distance1 = sensor1.range
#             print(f"VL53L0X Sensor 1 reading: {distance1} mm")
#         except Exception as e:
#             print(f"Error reading distance: {e}")
        
#         time.sleep(1)

# if __name__ == "__main__":
#     sensor1 = initialize_sensors()
#     read_distances(sensor1)




