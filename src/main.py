# src/main.py
from utils.audio import load_audio, play_audio
from fxs.reverb import ReverbEffect
from fxs.delay import DelayEffect
from tracks.thru_track import ThruTrack
from tracks.looper_track import LooperTrack

def main():
    # Load sample audio files

    audio1, rate1 = load_audio('samples/sample1.wav')
    audio2, rate2 = load_audio('samples/sample2.wav')

    # Create tracks
    track1 = ThruTrack('Track 1', audio1)
    track2 = LooperTrack('Track 2', audio2)

    # Apply effects
    reverb = ReverbEffect()
    delay = DelayEffect()

    #track1.add_effect(reverb)
    track2.add_effect(delay) 

    processed_audio1 = track1.apply_effects()
    processed_audio2 = track2.apply_effects()

    # Play processed audio
    print("Playing Track 1 with Reverb...")
    play_audio(processed_audio1, rate1)

    print("Playing Track 2 with Delay...")
    play_audio(processed_audio2, rate2)

if __name__ == '__main__':
    main()
