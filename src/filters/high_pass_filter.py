import numpy as np
from .filter_base import FilterBase

class HighPassFilter(FilterBase):
    def __init__(self, cutoff_frequency, sample_rate):
        super().__init__("High Pass Filter")
        self.cutoff_frequency = cutoff_frequency
        self.sample_rate = sample_rate
        self.alpha = None
        self.previous_input = 0.0
        self.previous_output = 0.0
        self.calculate_alpha()

    def calculate_alpha(self):
        rc = 1.0 / (2 * np.pi * self.cutoff_frequency)
        dt = 1.0 / self.sample_rate
        self.alpha = rc / (rc + dt)

    def apply(self, audio_data):
        filtered_data = []
        for sample in audio_data:
            output = self.alpha * (self.previous_output + sample - self.previous_input)
            self.previous_input = sample
            self.previous_output = output
            filtered_data.append(output)
        return np.array(filtered_data)
