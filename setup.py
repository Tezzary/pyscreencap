from setuptools import setup, find_packages

setup(
    name='pyscreencap',
    version='1.0.0',
    description='Easy to use Python screen recording library, that can record at very high framerates.',
    author='Tezzary',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'imageio[ffmpeg]',
        'dxcam',
        'opencv-python',
        'ffmpeg-python',
        'numpy',
    ],
)