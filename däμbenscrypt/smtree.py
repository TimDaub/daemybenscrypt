import math
import sys

class Tree:
  def insert(self, root, key, value):
    left = root.left
    right = root.right

    l_dist = self.distance(key, left.key)
    r_dist = self.distance(key, right.key)

  def distance(self, k1, k2):
    b_dist = bytes(x ^ y for x, y in zip(bytes(k1, "utf-8"), bytes(k2, "utf-8")))
    return math.log2(int.from_bytes(b_dist, sys.byteorder))

  def iou_distance(self, k1, k2):
    k1 = set(k1)
    k2 = set(k2)
    intersection = len(k1.intersection(k2))
    union = len(k1.union(k2))
    return intersection / union

class Node:
  def __init__(self, root, key, value, left=None, right=None):
    self.root = root
    self.key = key
    self.value = value
    self.left = left
    self.right = right
    # TODO: Add max_key
