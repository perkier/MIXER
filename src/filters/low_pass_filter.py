import numpy as np
from .filter_base import FilterBase

class LowPassFilter(FilterBase):
    def __init__(self, cutoff_frequency, sample_rate):
        super().__init__("Low Pass Filter")
        self.cutoff_frequency = cutoff_frequency
        self.sample_rate = sample_rate
        self.alpha = None
        self.previous_sample = 0.0
        self.calculate_alpha()

    def calculate_alpha(self):
        rc = 1.0 / (2 * np.pi * self.cutoff_frequency)
        dt = 1.0 / self.sample_rate
        self.alpha = dt / (rc + dt)

    def apply(self, audio_data):
        filtered_data = []
        for sample in audio_data:
            self.previous_sample = self.alpha * sample + (1 - self.alpha) * self.previous_sample
            filtered_data.append(self.previous_sample)
        return np.array(filtered_data)
