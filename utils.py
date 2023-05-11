class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def create_tree_from_list(lst):
    if not lst:
        return None

    root = TreeNode(lst[0])
    nodes = [root]
    index = 1

    while nodes:
        node = nodes.pop(0)
        if index < len(lst) and lst[index] is not None:
            node.left = TreeNode(lst[index])
            nodes.append(node.left)
        index += 1
        if index < len(lst) and lst[index] is not None:
            node.right = TreeNode(lst[index])
            nodes.append(node.right)
        index += 1

    return root
