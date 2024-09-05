from pymavlink import mavutil
import json
import time
import sys

#HOW TO USE: python executeBoat.py "C:\KKCTBN 2023\kkctbn2023\Blueberry\A" provide the json pathe file


# Check if the user provided a JSON file path as a command line argument
if len(sys.argv) < 2:
    print("Error: Please provide the path to the JSON file.")
    exit()

json_file_path = sys.argv[1]

# Create a connection to the Pixhawk
master = mavutil.mavlink_connection("/dev/ttyACM0", baud=57600)

# Wait for the first heartbeat to make sure the connection has been established
master.wait_heartbeat()

# Load the logged RC values from the specified JSON file
try:
    with open(json_file_path, 'r') as f:
        rc_log = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading RC log: {e}")
    exit()

# Send RC_CHANNELS_OVERRIDE messages from the JSON data
for log in rc_log:
    # Extract the PWM values
    chan_raw = [log.get('chan{}_raw'.format(i), 0) for i in range(1, 19)]

    # Send an RC_CHANNELS_OVERRIDE message with the logged values
    master.mav.rc_channels_override_send(
        master.target_system, master.target_component, *chan_raw
    )

    # Wait a short time before sending the next message
    time.sleep(0.24)

print("Autonomous execution completed.")
