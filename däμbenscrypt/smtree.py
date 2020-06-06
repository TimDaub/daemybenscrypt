class Tree:
  def insert(self, root, key, value):
    left = root.left
    right = root.right

    l_dist = self.distance(key, left.key)
    r_dist = self.distance(key, right.key)

  def distance(self, k1, k2):
    # NOTE: Inspired by:
    # https://en.wikipedia.org/wiki/Hamming_distance#Algorithm_example
    shortest = min(k1, k2, key=len)
    longest = max(k1, k2, key=len)
    
    dist_counter = len(longest) - len(shortest)
    for n in range(len(shortest)):
      if shortest[n] != longest[n]:
        dist_counter += 1
    return dist_counter
    
class Node:
  def __init__(self, root, key, value, left=None, right=None):
    self.root = root
    self.key = key
    self.value = value
    self.left = left
    self.right = right
    # TODO: Add max_key
