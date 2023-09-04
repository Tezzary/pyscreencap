from pyscreencap.pyscreencap import Recorder
from time import sleep

fps = 1000
# Create a new record object
rec = Recorder(fps=fps, bitrate=50)

sleep(1)
# Start recording
rec.start_recording()

benchmark_time = 10
sleep(benchmark_time)

# Stop recording
print(f"Max Recording Framerate Recommended: {rec.stop_recording() / benchmark_time}")