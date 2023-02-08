import streamlit as st
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

fs = 44100  # sample rate
duration = 5  # recording duration


def get_note(frequency):
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    reference_note = 440
    semitones = 12 * (np.log2(frequency / reference_note))
    note_index = int(semitones) % 12
    return notes[note_index]


def audio_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    # Get the most prominent frequency from the audio
    frequency = np.abs(np.fft.rfft(indata[:, 0]))
    frequency = np.argmax(frequency) * fs / (2 * (indata.shape[0] - 1))
    note = get_note(frequency)
    print(f'Note: {note}')


with sd.InputStream(callback=audio_callback, blocksize=int(fs * duration),
                    samplerate=fs, channels=1):
    print('Recording...')
    sd.sleep(duration * 1000)
    print('Done.')
