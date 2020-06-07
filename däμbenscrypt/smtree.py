import math
import sys

class Tree:
  def insert(self, root, key, value):
    left = root.left
    right = root.right

    l_dist = self.distance(key, left.key)
    r_dist = self.distance(key, right.key)

  def distance(self, k1, k2):
    comparison = bytes(x ^ y for x, y in zip(bytes(k1, "utf-8"), bytes(k2, "utf-8")))
    reduced_comparison = int.from_bytes(comparison, sys.byteorder)
    if reduced_comparison == 0:
      return 0
    else:
      return math.log2(reduced_comparison)

class Node:
  def __init__(self, root, key, value, left=None, right=None):
    self.root = root
    self.key = key
    self.value = value
    self.left = left
    self.right = right
    # TODO: Add max_key
