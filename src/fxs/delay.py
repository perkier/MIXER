import numpy as np

class DelayEffect:
    def __init__(self, delay=0.3, feedback=0.5, sample_rate=44100):
        self.delay = delay
        self.feedback = feedback
        self.sample_rate = sample_rate

    def apply(self, audio_data):
        delay_samples = int(self.delay * self.sample_rate)
        delay_signal = np.zeros(len(audio_data) + delay_samples)
        delay_signal[:len(audio_data)] = audio_data
        for i in range(delay_samples, len(delay_signal)):
            delay_signal[i] += self.feedback * delay_signal[i - delay_samples]
        return delay_signal[:len(audio_data)]