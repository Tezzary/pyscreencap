import pyscreencap as psc
from time import sleep

# Create a new record object
rec = psc.Recorder()

# Start recording
rec.start_recording()

sleep(5)

# Stop recording
rec.stop_recording()