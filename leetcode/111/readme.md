# 111. Minimum Depth of Binary Tree `Easy`

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

#### Example:
```
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its minimum depth = 2.
```

#### `TreeNode` definition:
```
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
```

### Solution

Uses `collection.deque` ([docs](https://docs.python.org/3/library/collections.html#collections.deque)).

``` python3
def minDepth(self, root: TreeNode) -> int:
  if root is None:
    return 0

  frontier = collections.deque([(root, 1)])

  while frontier:
    currentNode, depth = frontier.popleft() # 

    # Leaf node
    if currentNode.left is None and currentNode.right is None:
      return depth

    # Add children to the frontier
    if currentNode.left:
      frontier.append((currentNode.left, depth + 1))
    if currentNode.right:
      frontier.append((currentNode.right, depth + 1))

  return minDepth
```

### Alternative Solution:

This version is recursive (DFS).

```python3
def minDepth(self, root: TreeNode) -> int:
  if root is None:
    return 0

  def minPathToLeaf(node: TreeNode):
    # Leaf node
    if node.left is None and node.right is None:
      return 1

    leftMinDepth = self.minDepth(node.left) if node.left else float('inf')
    rightMinDepth = self.minDepth(node.right) if node.right else float('inf')

    return min(leftMinDepth, rightMinDepth) + 1

  return minPathToLeaf(root)
```

#### Complexity

```
???
```

