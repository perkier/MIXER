import numpy as np

class ReverbEffect:
    def __init__(self, decay=0.5, delay=0.1, sample_rate=44100):
        self.decay = decay
        self.delay = delay
        self.sample_rate = sample_rate

    def apply(self, audio_data):
        delay_samples = int(self.delay * self.sample_rate)
        reverb_signal = np.zeros(len(audio_data) + delay_samples)
        reverb_signal[:len(audio_data)] = audio_data
        for i in range(delay_samples, len(reverb_signal)):
            reverb_signal[i] += self.decay * reverb_signal[i - delay_samples]
        return reverb_signal[:len(audio_data)]