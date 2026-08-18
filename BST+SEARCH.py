class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)
def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")
def search(root, key):
    if root is None:
        return False

    if root.key == key:
        return True

    if key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)

print("Inorder:")
inorder(root)

print("\nPreorder:")
preorder(root)

print("\nPostorder:")
postorder(root)

key = int(input("\nEnter key to search: "))

if search(root, key):
    print("Key found")
else:
    print("Key not found")
