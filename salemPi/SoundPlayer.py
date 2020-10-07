from pydub import AudioSegment
from pydub.playback import play
from os import listdir
from os.path import isfile, join

class SoundPlayer(object):
    def __init__(self):
        self.root_path = 'Sounds/'
        self.all_sounds = self.list_sounds()
        self.current_index = 0
    def list_sounds(self):
        return [f for f in listdir(self.root_path) if isfile(join(self.root_path, f))]
    def play(self, sound_name):
        print('playing name ' + sound_name)
        full_name = self.root_path + sound_name
        song = AudioSegment.from_mp3(full_name)
        play(song)
    def play_rotated_sound(self):
        sound = self.all_sounds[self.current_index]
        self.play(sound)
        self.current_index += 1
        if self.current_index == len(self.all_sounds):
            self.current_index = 0
