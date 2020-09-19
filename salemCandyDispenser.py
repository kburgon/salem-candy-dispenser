from SoundPlayer import SoundPlayer
import serial
import time

heartbeat_value = 1
candy_triggered = 2
port = '/dev/ttyACM0'

def run():
    # Initialize Objects
    arduino = serial.Serial(port, 9600, timeout=5)
    time.sleep(2)

    # Listen for input
    arduino.flush()
    response = arduino.read(arduino.in_waiting())

    # Check input for action
    response_num = int(response)
    if response_num == heartbeat_value:
        print('Arduino Alive')
    elif response_num == candy_triggered:
        print('Candy triggered')
        play_sound()

def play_sound():
    print('playing sound')