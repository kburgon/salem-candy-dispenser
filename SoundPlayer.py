from pydub import AudioSegment
from pydub.playback import play

class SoundPlayer(object):
    def __init__(self):
        self.root_path = 'Sounds/'
    def play(self, sound_name='hag_idle'):
        print('playing name ' + sound_name)
        full_name = self.root_path + sound_name + '.mp3'
        song = AudioSegment.from_mp3(full_name)
        play(song)