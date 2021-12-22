# Author: Adam Exley
import logging

from scan.extractor import Extractor
from scan.builder import Builder


logging.basicConfig()

ex = Extractor()

"""Crop (2nd arg) is where the scan is located in the video frame. Trial and error tends to work"""
# frames = ex.run_and_cvt('scans/BRAIN_2.mp4',[5,-175,130,-1])
# frames = ex.run_and_cvt('scans/BRAIN_1.mp4',[20,-275,215,-1])
frames = ex.run_and_cvt('scans/xxxx.mp4',[0,-1,0,-1])

b = Builder()


"""Slicing here will change what portion of the scan is shown in 3D"""
# b.source(frames[:75])
# b.source(frames[:,200:-50])
b.source(frames)


b.build()
b.voxel(1)

