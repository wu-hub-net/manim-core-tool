import numpy as np
from manim import *
from abc import abstractmethod
"""
将两个mobject合并为VGroup
一个作为主mob，一个作为副mob
副mob围绕主mob操作
"""
class MShape(VGroup):
  DEFAULT_TIME = 0.5

  def __init__(self, shape: Mobject, accomp: Mobject, **kwargs):
    super().__init__(**kwargs)
    self.shape = shape
    self.accomp = accomp
    self.add(shape,accomp)

  # 位置操作
  def merge(self):
    self.accomp.move_to(self.shape.get_center())
    return self
  def merge_change(self, time=DEFAULT_TIME):
    return self.accomp.animate(runtime=time).move_to(self.shape.get_center())
  
  def top(self, buff=0.2):
    self.accomp.next_to(self.shape, UP, buff=buff)
    return self
  def top_change(self, buff=0.2, time=DEFAULT_TIME):
    return self.accomp.animate(runtime=time).next_to(self.shape, UP, buff=buff)
  
  def bottom(self, buff=0.2):
    self.accomp.next_to(self.shape, DOWN, buff=buff)
    return self
  def bottom_change(self, buff=0.2, time=DEFAULT_TIME):
    return self.accomp.animate(run_time=time).next_to(self.shape, DOWN, buff=buff)
  
  def left(self, buff=0.2):
    self.accomp.next_to(self.shape, LEFT, buff=buff)
    return self
  def left_change(self, buff=0.2, time=DEFAULT_TIME):
    return self.accomp.animate(run_time=time).next_to(self.shape, LEFT, buff=buff) 
  
  def right(self, buff=0.2):
    self.accomp.next_to(self.shape, RIGHT, buff=buff)
    return self
  def right_change(self, buff=0.2, time=DEFAULT_TIME):
    return self.accomp.animate(run_time=time).next_to(self.shape, RIGHT, buff=buff) 
  
  # 个体变化
  def set_shape_color(self, color):
    self.shape.set_color(color)
    return self
  def change_shape_color(self, color, time=DEFAULT_TIME):
    return self.shape.animate(run_time=time).set_color(color)
  
  def set_accomp_color(self, color):
    self.accomp.set_color(color)
    return self
  def change_accomp_color(self, color, time=DEFAULT_TIME):
    return self.accomp.animate(run_time=time).set_color(color)
  
  def merge_color(self):
    self.match_color(self.shape.color)
    return self
  def merge_change_color(self, time=DEFAULT_TIME):
    return self.change_accomp_color(self.shape.color, time)
  
  def set_shape_width(self,width):
    self.shape.stretch(width/self.shape.width,0)
    return self
  def change_shape_width(self,width):
    return self.shape.animate.stretch(width/self.shape.width,0)

  def set_accomp_height(self,height):
    self.accomp.stretch(height/self.accomp.height,1)
    return self
  def change_accomp_height(self,height):
    return self.accomp.animate.stretch(height/self.accomp.height,1)
  
  def merge_width(self, number=1):
    self.accomp.match_width(self.shape).scale(number)
    return self
  def merge_change_width(self, number=1, time=DEFAULT_TIME):
    return self.accomp.animate(run_time=time).match_width(self.shape).scale(number)
  
  def merge_height(self, number=1):
    self.accomp.match_height(self.shape).scale(number)
    return self
  def merge_change_height(self, number=1, time=DEFAULT_TIME):
    return self.accomp.animate(run_time=time).match_height(self.shape).scale(number)
  
  # 指示
  def wave_change_shape(self, time: float = DEFAULT_TIME, direction: np.ndarray = UP,
                         ripples: int = 1, time_width: float = 1):
    # 运行时间 波动方向 波数 波长相对于mob宽度的长度
    return ApplyWave(self.shape, run_time=time, direction=direction,
                      ripples=ripples, time_width=time_width)
  def wave_change_accomp(self, time: float = DEFAULT_TIME, direction: np.ndarray = UP,
                         ripples: int = 1, time_width: float = 1):
    return ApplyWave(self.accomp, run_time=time, direction=direction,
                      ripples=ripples, time_width=time_width)
  def wave_change(self, time: float = DEFAULT_TIME, direction: np.ndarray = UP,
                         ripples: int = 1, time_width: float = 1):
    anim1 = self.wave_change_accomp(time=time, direction=direction,
                      ripples=ripples, time_width=time_width)
    anim2 = self.wave_change_shape(time=time, direction=direction,
                      ripples=ripples, time_width=time_width)
    return AnimationGroup(anim1,anim2)
  
  def circom_change_shape(self, time: float = DEFAULT_TIME, circom_type: type = Rectangle):
    # 运行时间 形状（Rectangle or Circle） 
    return Circumscribe(self.shape, run_time=time, shape=circom_type)
  def circom_change_accomp(self, time: float = DEFAULT_TIME, circom_type: type = Rectangle): 
    return Circumscribe(self.accomp, run_time=time, shape=circom_type)
  def circom_change(self, time: float = DEFAULT_TIME, circom_type: type = Rectangle): 
    return Circumscribe(self, run_time=time, shape=circom_type)

class TShape:
  @abstractmethod
  def value(self):
    pass
"""
携带普通文本的图形
""" 
class TextShape(MShape,TShape):
  DEFAULT_TIME = MShape.DEFAULT_TIME
  DEFAULT_TEXT = Text("测试").scale(0.5)

  def __init__(self,shape: Mobject, text: Text=DEFAULT_TEXT):
    super().__init__(shape=shape, accomp=text)

  @classmethod
  def init(cls, shape: Mobject,data="测试", font_size=48, font_color=BLUE, font_style="Consolas", font_opacity=1):
    text = Text(text=data, font=font_style, font_size=font_size, color=font_color, fill_opacity=font_opacity)
    return cls(shape=shape, text=text)
  
  def show(self,time=DEFAULT_TIME): 
    return AnimationGroup(Write(self.accomp),Create(self.shape),run_time=time)
  
  @property
  def value(self):
    return self.accomp.text
"""
携带整数的图形
"""
class IntShape(MShape):
  DEFAULT_TIME = MShape.DEFAULT_TIME
  DEFAULT_INTEGER = Integer(number=0, font_size=48)
  def __init__(self,shape: Mobject, integer: Integer=DEFAULT_INTEGER):
    super().__init__(shape=shape, accomp=integer)

  @classmethod
  def init(cls, shape: Mobject,number=0, font_size=48, font_color=BLUE, font_opacity=1):
    integer = Integer(number=number, font_size=font_size, color=font_color, fill_opacity=font_opacity)
    return cls(shape=shape, integer=integer)
  
  def show(self,time=DEFAULT_TIME): 
    return AnimationGroup(Write(self.accomp), Create(self.shape), run_time=time)
  
  @property
  def value(self):
    return self.accomp.get_value()
  
class MShapeModel():
  @staticmethod
  def int_rectangle(number = 0):
    return IntShape.init(shape=Rectangle(), number=number)
  @staticmethod
  def int_circle(number = 0):
    return IntShape.init(shape=Circle(),number=number)
