import numpy as np
from scipy.signal import butter, lfilter
from .filter_base import FilterBase

class BandPassFilter(FilterBase):
    def __init__(self, lowcut, highcut, sample_rate, order=5):
        super().__init__("Band Pass Filter")
        self.lowcut = lowcut
        self.highcut = highcut
        self.sample_rate = sample_rate
        self.order = order
        self.b, self.a = butter(self.order, [self.lowcut, self.highcut], btype='band', fs=self.sample_rate)

    def apply(self, audio_data):
        filtered_data = lfilter(self.b, self.a, audio_data)
        return filtered_data