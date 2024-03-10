class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_largest(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.val

def find_smallest(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.val

def sum_values(node):
    if node is None:
        return 0
    return node.val + sum_values(node.left) + sum_values(node.right)

# Create a sample BST
root = TreeNode(5,
                TreeNode(3,
                         TreeNode(2),
                         TreeNode(4)),
                TreeNode(8,
                         TreeNode(6),
                         TreeNode(10)))

# Test the functions
largest = find_largest(root)
smallest = find_smallest(root)
total_sum = sum_values(root)

print(f'Найбільше: {largest}, Найменше: {smallest}, Сумма всіх нодів: {total_sum}')