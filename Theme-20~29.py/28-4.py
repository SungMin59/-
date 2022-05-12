import sys
class Node:
  def __init__(self, item, le, ri):
    self.item = item
    self.le = le
    self.ri = ri

def preorder(node):
  print(node.item, end="")
  if node.le != '.':
    preorder(tree[node.le])
  if node.ri != '.':
    preorder(tree[node.ri])

def inorder(node):
  if node.le != '.':
    inorder(tree[node.le])
  print(node.item, end="")
  if node.ri != '.':
    inorder(tree[node.ri])

def postorder(node):
  if node.le != '.':
    postorder(tree[node.le])
  if node.ri != '.':
    postorder(tree[node.ri])
  print(node.item, end="")

n = int(sys.stdin.readline().rstrip())
tree = {}

for _ in range(n):
  node, le, ri = map(str, sys.stdin.readline().rstrip().split())
  tree[node] = Node(item=node, le=le, ri=ri)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])