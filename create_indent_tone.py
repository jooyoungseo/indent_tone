import os

import numpy as np
import pandas as pd
from scipy.io.wavfile import write

# Load the CSV file
file_path = "data/pitch.csv"
data = pd.read_csv(file_path)

# Define the sample rate and the new duration
sample_rate = 44100  # Standard CD quality sample rate
duration = 0.1  # Duration in seconds


# Function to generate and save a sine wave for a given frequency
def generate_sine_wave(frequency, file_name):
    t = np.linspace(
        0, duration, int(sample_rate * duration), endpoint=False
    )  # Time axis
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # Generate sine wave
    # Normalize to 16-bit signed integers
    wave_int16 = np.int16(wave / np.max(np.abs(wave)) * 32767)
    write(file_name, sample_rate, wave_int16)


# Directory for the new WAV files
wav_dir = "wav/"
os.makedirs(wav_dir, exist_ok=True)

# Generate and save a sine wave for each frequency in the 'pitch' column with the updated naming convention
for index, row in data.iterrows():
    frequency = row["pitch"]
    space_value = int(row["space"])  # Use 'space' column value for naming
    file_name = os.path.join(wav_dir, f"{space_value}space.wav")
    generate_sine_wave(frequency, file_name)
