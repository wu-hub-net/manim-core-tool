from manim import *
import numpy as np
class MStack(VGroup):
  DEFAULT_TITLE = Text('Stack', opacity=0.5, color=WHITE).scale(0.5)
  DEFAULT_TBUFF = 0.1
  def __init__(self, title: Mobject=DEFAULT_TITLE, direction=UP, **kwargs):
    super().__init__(**kwargs)
    text = title
    self.add(text)
    self.title = text
    self.length = 1 
    self.direction = direction
  @classmethod
  def init_text(cls,data="测试", font_size=48, font_color=BLUE, font_style="Consolas", font_opacity=1):
    text = Text(text=data, font=font_style, font_size=font_size, color=font_color, fill_opacity=font_opacity)
    return cls(title=text)
  
  #准备推栈动画
  def push_prepare(self, mobject, direction=UL):
    return mobject.animate.next_to(self[self.length-1], direction, buff=0.5)
  #推栈动画
  def push(self, mobject):
    top_mob = self[self.length-1]
    self.add(mobject)
    self.length += 1
    if(self.length == 2):
      return mobject.animate.next_to(top_mob, self.direction, buff=self.DEFAULT_TBUFF)
    return mobject.animate.next_to(top_mob, self.direction, buff=0)
  #隐式出栈
  def pop(self):
    if self.length == 1:
        return None
    top_mob = self[self.length-1]
    self.length -= 1
    self.remove(top_mob)
    return top_mob
  #显式出栈动画
  def pop_change_fadeout(self):
    if self.length == 1:
        return None
    top_mob = self[self.length-1]
    self.length -= 1
    self.remove(top_mob)
    return FadeOut(top_mob)
  
  def pop_change_uncreate(self):
    if self.length == 1:
        return None
    top_mob = self[self.length-1]
    self.length -= 1
    self.remove(top_mob)
    return Uncreate(top_mob)
  
  def pop_change_unwrite(self):
    if self.length == 1:
        return None
    top_mob = self[self.length-1]
    if type(top_mob) != Text:
       return None
    self.length -= 1
    self.remove(top_mob)
    return Unwrite(top_mob)
  
  #栈顶
  def get_top(self):
    if(self.length == 1):
      return None
    return self[self.length-1]
  #长度
  def get_length(self):
    return self.length - 1
class MTree(VGroup):
    def __init__(self, **kwargs):
      super().__init__(**kwargs)
      self.nodes = []
      self.edges = []
      self.relations = []
      self.childs = []
      self.parent = []
    # 添加节点及连线
    def add_node(self, node: Mobject, parent: Mobject=None, direction=DOWN, config:type = Rectangle):
      if(config not in [Rectangle,Circle]):
         return
      # 添加结点
      self.add(node)
      # 添加信息
      self.nodes.append(node)
      if parent is None:
        self.childs.append([])
        self.parent.append(-1)
        return
      child_idx = len(self.nodes) - 1
      parent_idx = self.nodes.index(parent)
      self.childs[parent_idx].append(child_idx)
      self.parent.append(parent_idx)
      # 移动结点
      node.next_to(parent, direction)
      # 连线
      if(config == Rectangle):
        start = parent.get_bottom()
        end = node.get_top()
      elif(config == Circle):
        direction = node.get_center() - parent.get_center()
        direction = direction / np.linalg.norm(direction)
        parent_radius = parent.shape.radius
        node_radius = node.shape.radius
        start = parent.get_center() + direction * parent_radius
        end = node.get_center() - direction * node_radius
      edge = Line(start, end)
      self.add(edge)
      self.edges.append(edge)
      edge_idx = len(self.edges) - 1
      self.relations.append({
        "parent_idx": parent_idx,
        "child_idx": child_idx,
        "edge_idx": edge_idx
      })