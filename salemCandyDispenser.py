from SoundPlayer import SoundPlayer
import serial
import time

heartbeat_value = '1'
candy_triggered = '2'
port = '/dev/ttyACM0'

def run():
    # Initialize Objects
    arduino = serial.Serial(port, 9600, timeout=5)
    time.sleep(2)

    while True:
        try:
            listen(arduino)
        except Exception as e:
            print('Error ' + e + ' encountered')


def listen(arduino):
    # Listen for input
    arduino.flush()
    response = arduino.read(arduino.in_waiting())

    # Check input for action
    if response == heartbeat_value:
        print('Arduino Alive')
    elif response == candy_triggered:
        print('Candy triggered')
        play_sound()
    else:
        raise BufferError('Arduino response invalid')

    # Return heartbeat to arduino
    arduino.write('1')

def play_sound():
    print('playing sound')


if __name__ == "__main__":
    run()