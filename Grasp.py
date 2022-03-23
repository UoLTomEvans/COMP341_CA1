import numpy as np
class Grasp:
    def __init__(self,center,angle,length,width):
        self.center = center
        self.angle = angle
        self.length = length
        self.width = width
    
    def as_gr(self):
        """
        Convert the input to GraspRectangle format
        """
        xo = np.cos(self.angle)
        yo = np.sin(self.angle)

        y1 = self.center[0] + self.length / 2 * yo
        x1 = self.center[1] - self.length / 2 * xo
        y2 = self.center[0] - self.length / 2 * yo
        x2 = self.center[1] + self.length / 2 * xo

        return GraspRectangle(np.array(
                       [
             [y1 - self.width/2 * xo, x1 - self.width/2 * yo],
             [y2 - self.width/2 * xo, x2 - self.width/2 * yo],
             [y2 + self.width/2 * xo, x2 + self.width/2 * yo],
             [y1 + self.width/2 * xo, x1 + self.width/2 * yo]
             ] 
        ).astype(np.float))

class GraspRectangle:
    def __init__(self,grasp=None):
        if grasp:
            self.grasp = grasp
        else:
            self.grasp = []
    
    @classmethod
    def load_from_file(cls,filename):
        grasps = []
        with open(filename) as f:
            for l in f:
                x,y,theta,w,h = [float(v) for v in l[:-1].split((";"))]
                grasps.append(Grasp(np.array([y,x]),-theta/180.0*np.pi,w,h).as_gr)
        grasps = cls(grasps)
        return grasps