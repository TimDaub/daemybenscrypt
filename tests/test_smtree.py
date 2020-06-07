from däμbenscrypt.smtree import Tree


def test_distance():
  t = Tree()
  print(t.iou_distance("test", "täst"))
  print(t.iou_distance("test", "test"))
  print(t.iou_distance("test", "teest"))
  print(t.iou_distance("teest", "test"))


