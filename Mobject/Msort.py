from manim import *
from .MShape import *
class Maxis(VGroup):
  def __init__(self, height, width,array,lower: int=0, upper: int=10, color=BLUE, **kwargs):
    super().__init__(**kwargs)
    # 轴
    x_axis = NumberLine(
          x_range=[lower, upper, 1],
          length = (upper - lower)  * width,
          color=BLUE,
          include_numbers=False,
          label_direction=DOWN
      )
    custom_lables = {
      i + 0.5: str(i)
      for i in range(lower, upper)
    }
    x_axis.add_labels(custom_lables,direction=DOWN, buff=0.2)
    # 形
    x = x_axis.get_start()[0]
    y = x_axis.get_start()[1]
    rects = VGroup()
    for i,value in enumerate(array):
      rect = Rectangle(color=color,width=width,height=height * value)
      intrect = IntShape(shape=rect, integer=Integer(number=value)).top()
      intrect.move_to([x + width * (0.5 + i),y + intrect.height / 2,0])
      rects.add(intrect)
    self.add(x_axis,rects)
    self.x_axis = x_axis
    self.rects = rects
    self.array = array
    self.__height = height
    self.__width = width
    self.lower = lower
    self.upper = upper
    self.__color = color
  def split(self,number = 1):
    if(number >= self.upper | number <= self.upper): return None
    start1 = self.x_axis.get_corner(DL)
    start2 = start1.copy()
    start2[0] = self.x_axis.number_to_point(number)[0]
    maxis1 = Maxis(self.__height,
                   self.__width,
                   self.array[:number],
                   self.lower,
                   number,
                   color=self.__color
    ).move_to(start1, aligned_edge=DL)
    maxis2 = Maxis(self.__height,
                   self.__width,
                   self.array[number:],
                   number,
                   self.upper,
                   color=self.__color
    ).move_to(start2, aligned_edge=DL)
    return maxis1,maxis2
  def get_position(self,number=0):
    return self.x_axis.number_to_point(number)