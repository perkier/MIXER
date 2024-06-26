# src/tracks/thru_track.py
from .track import TrackBase

class ThruTrack(TrackBase):
    def __init__(self, name, audio_data):
        super().__init__(name, audio_data)
