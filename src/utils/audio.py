import wave
import numpy as np
import pyaudio

def load_audio(file_path):
    with wave.open(file_path, 'rb') as wf:
        n_channels = wf.getnchannels()
        sample_width = wf.getsampwidth()
        frame_rate = wf.getframerate()
        n_frames = wf.getnframes()
        audio_data = wf.readframes(n_frames)
        audio_array = np.frombuffer(audio_data, dtype=np.int32)

        print(frame_rate)

    return audio_array, frame_rate

def play_audio(audio_array, frame_rate):
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=pyaudio.paInt32,
                    channels=1,
                    rate=frame_rate,
                    output=True)
    
    stream.write(audio_array.tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()