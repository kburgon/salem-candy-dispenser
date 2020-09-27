from SoundPlayer import SoundPlayer
import serial
import time

heartbeat_value = int(1)
candy_triggered = int(2)
port = '/dev/ttyACM0'

def run():
    # Initialize Objects
    arduino = serial.Serial(port, 9600, timeout=5)
    time.sleep(2)

    while True:
        try:
            listen(arduino)
        except Exception as e:
            print('Error ' + str(e) + ' encountered')


def listen(arduino):
    # Listen for input
    # arduino.flush()
    response = arduino.readline()
    decoded_response = int(response[0:len(response)-2].decode("utf-8"))
    print(decoded_response)

    # Check input for action
    if decoded_response == heartbeat_value:
        print('Arduino Alive')
    elif decoded_response == candy_triggered:
        print('Candy triggered')
        arduino.write(candy_triggered)
        play_sound()
        # log(trigger, time.now())
    else:
        raise BufferError('Arduino response invalid')

    # Return heartbeat to arduino
    arduino.write(heartbeat_value)

def play_sound():
    print('playing sound')


if __name__ == "__main__":
    run()