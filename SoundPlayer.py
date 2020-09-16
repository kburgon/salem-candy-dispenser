from playsound import playsound

class SoundPlayer(object):
    def __init__(self):
        self.root_path = 'Sounds/'
    def play(self, sound_name):
        print('playing name ' + sound_name)
        playsound(sound_name + '.mp3')