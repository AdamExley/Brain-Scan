# Author: Adam Exley
import logging
import os

import cv2
import numpy as np



class Extractor():

    # def find_limits(self, file):
    #     cap = cv2.VideoCapture(file)
    #     ret = True
    #     frames = []

    #     ret,frame = cap.read()

    #     while ret:
    #         frames.append(frame)
    #         ret,frame = cap.read()

    #     frames = np.array(frames)
    #     example = frames[len(frames)//2]

    #     crop = [0]*4
    #     labels = ['Left','Right','Top','Bottom']

    #     def get_input(choice):
    #         print(f'\n\nChange {labels[choice]}:\n\tCurrent Value:{crop[choice]}')
    #         get = True
    #         while get:
    #             try:
    #                 new = input('\tNew Value: ')
    #                 crop[choice] = int(new)
    #                 get = False
    #             except Exception as e:
    #                 print('Invalid')

    #     cont = True

    #     while cont:
    #         print("\n\nChoose an Option:\n\t1) Left\n\t2) Right\n\t3) Top\n\t4) Bottom")



    def run(self, file, crop):

        cap = cv2.VideoCapture(file)
        ret = True
        frames = []

        ret,frame = cap.read()

        while ret:
            frames.append(frame[crop[0]:crop[1],crop[2]:crop[3]])
            ret,frame = cap.read()

        return np.array(frames)

    def recolor(self, frames):
        # Get blue out
        hues = (self.cvt_full(frames, cv2.COLOR_BGR2HSV)[...,0]  > 100) & (self.cvt_full(frames, cv2.COLOR_BGR2HSV)[...,1] > 100)
        frames[hues] = [0,0,0]

        # Go to grayscale
        frames = self.cvt_full(frames, cv2.COLOR_BGR2GRAY)
        return frames

    def cvt_full(self, frames, code):
        out = []
        for frame in frames:
            out.append(cv2.cvtColor(frame, code))
            # cv2.imshow("",cv2.cvtColor(frame, code))
            # cv2.waitKey(100)
        return np.array(out)

    def run_and_cvt(self, file, crop):
        frames = self.run(file, crop)
        return self.recolor(frames)
