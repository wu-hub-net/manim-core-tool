from manim import *
from Mobject.MShape import *
class main(Scene):
  def construct(self):
    text = Text(text='asddasd',color=WHITE)
    print(text.font_size)
    rec = Rectangle(color=RED)
    ashape = TextShape.init(shape=rec,data="wpde")
    self.play(ashape.show())
    self.play(ashape.merge_change_color())
    self.play(ashape.circom_change())
    self.wait()
    self.play(ashape.top_change())
    print(ashape.width,ashape.height)
    self.wait()
    self.play(ashape.circom_change())
    self.wait()

