# importing setup from setup tools
from setuptools import setup

setup(
   name='cvpack',
   packages=['cvpack'],
   version='0.0.1',
   license='MIT',
   description='An helper library for openCv developer.',
   author='Kartik Panchal',
   author_email='clickshare07@gmail.com',
   url='https://github.com/MrBucks07/OpenCv',
   keywords=['MediaPipe', 'FaceMesh', 'FaceDetection', 'HandTracking', 'HandModule', 'FaceModule'],
   install_requires=[
      'opencv-python',
      'mediapipe'
   ],
   classifiers=[
      'License :: OSI Approved :: MIT License',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
      'Operating System :: OS Independent'
    ],
)
