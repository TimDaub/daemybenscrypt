from däμbenscrypt.smtree import Tree


def test_distance():
  t = Tree()

  equal_strings = t.distance("test", "test")
  assert equal_strings == 0

  d = t.distance("test", "täst")
  assert d != equal_strings

  r1 = t.distance("teest", "test")
  r2 = t.distance("test", "teest")
  assert r1 == r2
  assert r1 != equal_strings
  assert r2 != equal_strings


