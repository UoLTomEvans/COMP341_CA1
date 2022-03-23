import os
import glob
from rgbimage import RGB_Image

class Dataset:
    def __init__(self,file_path,start=0,end=0.9,ds_rotate=0):
        # Load all text files containing grasp location.
        graspf = glob.glob(os.path.join(file_path,"*","*_grasps.txt"))
        graspf.sort()
        grasp_file_length = len(graspf)
        depth_files = [file.replace("grasps.txt", "perfect_depth.tiff") for file in graspf]
        rgb_files = [file.replace('perfect_depth.tiff', 'RGB.png') for file in depthf]
    
    def get_rgb(self,index):
        rbg_img = RGB_Image.from_file(self.rgb_files[index])
        rgb_img.normalise()
        rgb_img.img = rbg_img.img.transpose((2,0,1))
        return rbg_img.img


