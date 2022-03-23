from imageio import imread
import cv2
import numpy as np


class RGB_Image:
    def __init__(self,img):
        self.img = img

    @classmethod
    def from_file(cls,filename) -> RGB_Image:
        return cls(imread(filename))

    def normalise(self):
        self.img = self.img.astype(np.float32)/255.0