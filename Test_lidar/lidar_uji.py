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
    
    sensor1.set_address(0x29)
    sensor3.set_address(0x29)

    for s in [sensor1, sensor2, sensor3, sensor4]:
        s.timing_budget = 200000
        s.signal_rate_limit = 0.01
    
    return sensor1, sensor2, sensor3, sensor4

def read_distances(sensor1, sensor2, sensor3, sensor4):
    while True:
        distance1 = (sensor1.range/10.0) - 5
        distance2 = (sensor2.range/10.0) - 5
        distance3 = (sensor3.range/10.0) - 5
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
