from SoundPlayer import SoundPlayer
import serial
import time
import traceback
import DbLogger

player = SoundPlayer()
heartbeat_value = '1'
candy_triggered = '2'
port = '/dev/ttyACM0'

def run():
    # Initialize Objects
    arduino = serial.Serial(port, 9600, timeout=5)
    time.sleep(2)

    # Continuously loop, listening for and responding to arduino triggers
    while True:
        try:
            listen(arduino)
        except Exception as e:
            print('Error ' + str(e) + ' encountered')
            traceback.print_exc()

def listen(arduino):
    # Listen for input
    response = arduino.readline()
    decoded_response = str(response[0:len(response)-2].decode("utf-8"))
    print(decoded_response)

    # Check input for action
    if decoded_response == heartbeat_value:
        print('Arduino Alive')
    elif decoded_response == candy_triggered:
        perform_action(arduino)
    else:
        arduino.write(str.encode(heartbeat_value))
        raise BufferError('Arduino response invalid')

def perform_action(arduino):
    print('Candy triggered')
    arduino.write(str.encode(candy_triggered))
    play_sound()
    arduino.write(str.encode(heartbeat_value))
    DbLogger.log_trigger()


def play_sound():
    print('playing sound')
    player.play_rotated_sound()


if __name__ == "__main__":
    run()