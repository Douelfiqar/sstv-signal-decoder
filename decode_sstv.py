import numpy as np
from scipy import signal
from scipy.io import wavfile

# Parameters
sample_rate = 156250
offset = -22000

# 1. Read the radio recording
iq = np.fromfile("radio_chall1.raw", dtype="<c8")

# 2. Correct the frequency
t = np.arange(len(iq)) / sample_rate
iq *= np.exp(-2j * np.pi * offset * t)

# 3. Filter the signal
sos = signal.butter(5, 6000, fs=sample_rate, output="sos")
iq = signal.sosfilt(sos, iq)

# 4. Demodulate FM into audio
audio = np.angle(iq[1:] * np.conj(iq[:-1]))

# 5. Convert to 48 kHz audio
audio = signal.resample_poly(audio, 192, 625)

# 6. Save WAV
audio /= np.max(np.abs(audio)) + 1e-12
wavfile.write("sstv_audio.wav", 48000, (audio * 32767).astype(np.int16))
