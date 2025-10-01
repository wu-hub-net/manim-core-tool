from manim import *
from Mobject.MShape import *
from Mobject.MStructure import *
class main(Scene):
  def construct(self):
    shape1 = MShapeModel.int_rectangle(1).to_edge(UP)
    shape2 = MShapeModel.int_rectangle(2)
    shape3 = MShapeModel.int_rectangle(3)
    tree = MTree()
    tree.add_node(node=shape1)
    tree.add_node(node=shape2,parent=shape1,direction=DL + DOWN*2)
    tree.add_node(node=shape3,parent=shape1,direction=DR + DOWN*2)
    self.add(tree)
    self.wait()

