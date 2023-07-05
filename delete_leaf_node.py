# Program to delete leaf
# node from binary search tree.
 
# Create a newNode in binary search tree.
class newNode:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Insert a node in binary search tree.
def insert(root, data):
    if root == None:
        return newNode(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root
 
# Function for in order traversal in a BST.
def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.data, end = " ")
        inorder(root.right)
 
# Delete leaf nodes from binary search tree.
def leafDelete(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return None
 
    # Else recursively delete in left
    # and right subtrees.
    root.left = leafDelete(root.left)
    root.right = leafDelete(root.right)
 
    return root
 

if __name__ == '__main__':
    root = None
    root = insert(root, 20)
    insert(root, 10)
    insert(root, 5)
    insert(root, 15)
    insert(root, 30)
    insert(root, 25)
    insert(root, 35)
    print("In order before deleting the leaf node.")
    inorder(root)
    leafDelete(root)
    print()
    print("In order after deleting the leaf node.")
    inorder(root)    