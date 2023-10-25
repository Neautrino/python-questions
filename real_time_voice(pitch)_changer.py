import numpy as np
import pyaudio

# Parameters
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1  # Mono audio
RATE = 44100  # Sample rate (Hz)
CHUNK = 1024  # Audio chunk size

# Initialize PyAudio
p = pyaudio.PyAudio()

# Start the audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

# Pitch shift factor (0.5 = one octave down, 2.0 = one octave up)
pitch_factor = 1.5

try:
    print("Voice changer running. Press Ctrl+C to exit.")
    while True:
        data = stream.read(CHUNK)
        audio_data = np.frombuffer(data, dtype=np.int16)

        # Apply pitch shift
        pitch_shifted_data = np.interp(np.arange(0, len(audio_data), pitch_factor),
                                       np.arange(0, len(audio_data)),
                                       audio_data).astype(np.int16)

        stream.write(pitch_shifted_data.tobytes())

except KeyboardInterrupt:
    pass

print("Voice changer stopped.")

# Close the audio stream and terminate PyAudio
stream.stop_stream()
stream.close()
p.terminate()
