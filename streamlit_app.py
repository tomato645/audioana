import streamlit as st
from audio_recorder_streamlit import audio_recorder

audio_bytes = audio_recorder()
if audio_bytes:
    audio_bytes = audio_recorder(pause_threshold=2.0, sample_rate=41_000)