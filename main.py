import numpy as np
from manim import *
from Mobject.MShape import *
from Mobject.MStructure import *
from Mobject.Msort import *
class main(MovingCameraScene):
  def construct(self):
    list = Maxis(height=0.3, width=0.7,
                 array=[5, 2, 8, 3, 1, 6, 4, 7, 9, 8])
    l1,l2 = list.split()
    tree = MTree()
    tree.add_node(node=list,direction=)
    self.add(tree)
    self.play(self.camera.frame.animate.scale(2))
    
