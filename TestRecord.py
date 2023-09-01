import pyscreencap
from time import sleep

# Create a new record object
rec = pyscreencap.Recorder(fps=60, bitrate=50)

sleep(1)
# Start recording
rec.start_recording()

sleep(10)

# Stop recording
rec.stop_recording()