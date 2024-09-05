# import time
# import board
# import busio
# import adafruit_vl53l1x as vl53l1x
# import smbus
# import math  

# LIDAR_ADDR = 0x62
# LIDAR_REG_ACQ_COMMAND = 0x00
# LIDAR_REG_STATUS = 0x01
# LIDAR_REG_ACQ_CONFIG = 0x04
# LIDAR_REG_DISTANCE = 0x8f

# def initialize_sensors():
#     i2c = busio.I2C(board.SCL, board.SDA)
    
#     sensor1 = vl53l1x.VL53L1X(i2c, address=0x30)
#     sensor2 = vl53l1x.VL53L1X(i2c, address=0x31)
#     #sensor3 = vl53l1x.VL53L1X(i2c, address=0x32)
#     sensor4 = vl53l1x.VL53L1X(i2c, address=0x33)
    
#     sensor1.start_ranging()
#     sensor2.start_ranging()
#    # sensor3.start_ranging()
#     sensor4.start_ranging()
    
#     bus = smbus.SMBus(1)
    
#     bus.write_byte_data(LIDAR_ADDR, LIDAR_REG_ACQ_CONFIG, 0x08)  
    
#     return sensor1, sensor2, sensor4, bus

# def read_distances(sensor1, sensor2, sensor4, bus):
#     while True:
#         # Read distance from Garmin LiDAR Lite v3
#         bus.write_byte_data(LIDAR_ADDR, LIDAR_REG_ACQ_COMMAND, 0x04) 
#         time.sleep(0.04)
#         distance_garmin = bus.read_word_data(LIDAR_ADDR, LIDAR_REG_DISTANCE) / 100.0 
#         distance1 = sensor1.distance
#         distance2 = sensor2.distance
#         #distance3 = sensor3.distance
#         distance4 = sensor4.distance
        
#         # Print readings
#         print(f"Garmin LiDAR Lite v3 reading: {distance_garmin:.2f} cm")
#         print(f"VL53L1X Sensor 1 reading: {distance1} cm")
#         print(f"VL53L1X Sensor 2 reading: {distance2} cm")
#         #print(f"VL53L1X Sensor 3 reading: {distance3} cm")
#         print(f"VL53L1X Sensor 4 reading: {distance4} cm")
        
#         time.sleep(1)

# if __name__ == "__main__":
#     sensor1, sensor2, sensor4, bus = initialize_sensors()
#     read_distances(sensor1, sensor2, sensor4, bus)




import time
import board
import busio
import adafruit_tca9548a
import adafruit_vl53l0x as sensor

i2c = board.I2C()  
tca = adafruit_tca9548a.TCA9548A(i2c)

def initialize_sensors():
    sensor1 = sensor.VL53L0X(tca[1])
    sensor2 = sensor.VL53L0X(tca[2])
    sensor3 = sensor.VL53L0X(tca[6])
    sensor4 = sensor.VL53L0X(tca[7])
    
    return sensor1, sensor2, sensor3, sensor4

def read_distances(sensor1, sensor2, sensor3, sensor4):
    while True:
        distance1 = (sensor1.range/10.0) - 5
        distance2 = (sensor2.range/10.0) - 5
        distance3 = (sensor3.range/10.0) - 12
        distance4 = (sensor4.range/10.0) - 5

        distance1 = 0 if (distance1<0) else distance1
        distance2 = 0 if (distance2<0) else distance2
        distance3 = 0 if (distance3<0) else distance3
        distance4 = 0 if (distance4<0) else distance4

        print(f"VL53L0X Sensor 1 reading: {distance1:.2f} cm")
        print(f"VL53L0X Sensor 2 reading: {distance2:.2f} cm")
        print(f"VL53L0X Sensor 3 reading: {distance3:.2f} cm")
        print(f"VL53L0X Sensor 4 reading: {distance4:.2f} cm")

        time.sleep(0.1)


if __name__ == "__main__":
    sensor1, sensor2, sensor3, sensor4 = initialize_sensors()
    read_distances(sensor1, sensor2, sensor3, sensor4)

