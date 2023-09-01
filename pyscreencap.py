import dxcam
import cv2
import ffmpeg
import numpy as np
from threading import Thread
from time import perf_counter

def _accurate_sleep(seconds):
    start = perf_counter()
    while perf_counter() - start < seconds:
        pass

class Recorder:
    def __init__(self, path="video.mp4", monitor=0, fps=60, bitrate=50):
        self.path = path
        self.fps = fps
        self.camera = dxcam.create(output_idx=monitor, output_color="BGR")
        #self.encoder = cv2.VideoWriter(self.path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (1920, 1080))
        #x264
        self.encoder = (
            ffmpeg
                .input('pipe:', format='rawvideo', pix_fmt='bgr24', s='{}x{}'.format(1920, 1080), r=fps)
                .output(path, pix_fmt='yuv420p', vcodec='libx264', movflags='faststart', preset='ultrafast', tune='zerolatency', cbr=True, b=f"{bitrate}M", g=fps)
                .overwrite_output()
                .run_async(pipe_stdin=True)
        )
        '''
        NVENC
        self.encoder = (
            ffmpeg
                .input('pipe:', format='rawvideo', pix_fmt='bgr24', s='{}x{}'.format(1920, 1080), r=fps)
                .output(path, pix_fmt='yuv420p', vcodec='h264_nvenc', movflags='faststart', preset=12, tune=3, cbr=True, b=f"{bitrate}M", g=fps)
                .overwrite_output()
                .run_async(pipe_stdin=True)
        )'''
        self.thread = None
        self.recording = False

    
    def _start_recording(self):
        start_time = perf_counter()
        frame_count = 0
        self.recording = True
        while self.recording:
            temp_frame = self.camera.grab()
            
            #check for None as will be the case occasionally if fps is set near monitor refresh rate or higher
            if(temp_frame is not None):
                frame = temp_frame

            if(frame is not None):
                frame_count += 1
                #self.encoder.write(frame)
                self.encoder.stdin.write(
                    frame
                    .astype(np.uint8)
                    .tobytes()
                )
                _accurate_sleep(start_time + frame_count / self.fps - perf_counter())

    def start_recording(self):
        self.thread = Thread(target=self._start_recording)
        self.thread.start()

    def stop_recording(self):
        if not self.thread:
            print("Attempted to stop recording when not recording")
            return
        self.recording = False
        self.thread.join()
        self.thread = None
        self.camera.stop()
        #self.encoder.release()
        self.encoder.stdin.close()
        self.encoder.wait()
            