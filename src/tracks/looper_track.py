from .track import TrackBase

class LooperTrack(TrackBase):
    def __init__(self, name, audio_data):
        super().__init__(name, audio_data)