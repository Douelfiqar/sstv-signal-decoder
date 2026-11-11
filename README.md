# SSTV Signal Decoder

A simple Python script to extract SSTV audio from a raw IQ radio recording using FM demodulation.

Built while solving an OSINT challenge.

## How it works

1. Read raw IQ samples.
2. Shift the signal to the correct frequency.
3. Apply a low-pass filter.
4. Demodulate the FM signal.
5. Export the audio as a WAV file.

The resulting audio can be opened in an SSTV decoder to reconstruct the transmitted image.

## Requirements

- Python 3
- NumPy
- SciPy

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Place `radio_chall1.raw` in the project directory and run:

```bash
python decode_sstv.py
```

The script generates `sstv_audio.wav`.

## Parameters

| Parameter | Value |
|---|---|
| Sample rate | 156250 Hz |
| IQ format | Complex float32 |
| Frequency offset | -22000 Hz |
| Output audio rate | 48000 Hz |

These values are specific to the challenge recording. The frequency offset was identified during signal analysis.
