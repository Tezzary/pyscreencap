import dxcam
import cv2
from threading import Thread
from time import perf_counter

class Recorder:
    def __init__(self, path="video.mp4", monitor=0, fps=30):
        self.path = path
        self.camera = dxcam.create(output_idx=monitor, output_color="BGR")
        self.encoder = cv2.VideoWriter(self.path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (1920, 1080))
        self.thread = None
        self.recording = False

    def _accurate_sleep(seconds):
        start = perf_counter()
        while perf_counter() - start < seconds:
            pass

    def _start_recording(self):
        start_time = perf_counter()
        frame_count = 0
        while self.recording:
            if not self.recoring:
                break
            temp_frame = self.camera.grab()
            
            #check for None as will be the case occasionally if fps is set near monitor refresh rate or higher
            if(temp_frame is not None):
                frame = temp_frame

            if(frame is not None):
                frame_count += 1
                self.encoder.write(frame)
                self._accurate_sleep(start_time + frame_count / self.fps - perf_counter())

    def start_recording(self):
        thread = Thread(target=self._start_recording)
        thread.start()

    def stop_recording(self):
        if self.thread:
            self.recording = False
            self.thread.join()
            self.thread = None
            self.camera.stop()
            self.encoder.release()
            