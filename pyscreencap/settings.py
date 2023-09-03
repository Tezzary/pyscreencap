def x264(fps, bitrate, path):
    return [
            './pyscreencap/binaries/ffmpeg',  # Path to ffmpeg executable
            '-f', 'rawvideo',
            '-pix_fmt', 'bgr24',
            '-s', '1920x1080',
            '-r', str(fps),
            '-i', 'pipe:',
            '-pix_fmt', 'yuv420p',
            '-vcodec', 'libx264',
            '-movflags', 'faststart',
            '-preset', 'ultrafast',
            '-tune', 'zerolatency',
            '-cbr', 'true',
            '-b:v', f'{bitrate}M',
            '-g', str(fps),
            '-y',  # Overwrite output file if it exists
            path
        ]

def nvenc(fps, bitrate, path):
    return [
            './pyscreencap/binaries/ffmpeg',  # Path to ffmpeg executable
            '-f', 'rawvideo',
            '-pix_fmt', 'bgr24',
            '-s', '1920x1080',
            '-r', str(fps),
            '-i', 'pipe:',
            '-pix_fmt', 'yuv420p',
            '-c:v', 'h264_nvenc',
            '-movflags', 'faststart',
            '-preset', '12',  # You can specify preset values here, or use 'fast' as an example
            '-tune', '3',
            '-b:v', f'{bitrate}M',
            '-g', str(fps),
            '-y',  # Overwrite output file if it exists
            path
        ]