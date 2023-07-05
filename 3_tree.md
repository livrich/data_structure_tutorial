# Tree

## What is a Tree?
A **tree** is an abstract data type that represents a hierarchical tree structure with a set of connected **nodes**. Each node in the tree can be connected to many **children**, but must be connected to exactly one **parent**, except for the root node, which has no parent.

</br>

## Types of Trees
### Binary Tree
A **binary tree** is a tree that links to no more than two other nodes. 

The top node is called the **root** node. There is only ever one root node. A node that has connected nodes is called a **parent** node. The node(s) connected to the parent are called **child** nodes. The nodes to the left and right of any parent node form a **subtree**. The nodes that connect to no other nodes are called **leaf** nodes.

![binary tree labeled](binary_tree_labeled.png)

</br>

### Binary Search Tree
A **binary search tree (BST)**, also called an ordered or sorted binary tree, is a rooted binary tree with the key of each internal node being greater than all the keys in the respective node's left subtree and less than the ones in its right subtree.

Reiterated, if the data being added is less than the parent node, it is added in the left subtree. Otherwise, if it is greater, it is added to the right subtree. Comparisons always start from the root node and continue until an empty place for the new node is found.

If duplicates are allowed, then the duplicate can be put either to the left or right of the root. Though, duplicates are often avoided.

![binary tree](binary_tree.png)

</br>

### Balanced Binary Search Tree
A **balanced binary search tree** is a BST that is as close to uniformly the same height throughout the tree as it can get. The height of a tree can be found by counting the maximum number of nodes between the root and the leaves.

It is not expected that a BST will automatically be balanced or remain balanced. Numerous algorithms have been written to detect if a tree is unbalanced and to correct the unbalance. Common algorithms include **red black trees** and **Adelson-Velskii and Landis (AVL)** trees.

When an imbalance is detected, a node rotation is performed to make the BST balanced again.

![balanced vs unbalanced tree](balanced_vs_unbalanced.png)

</br>

## Basic Operations
### Inserting
Inserting into a BST is a recursive operation:
* Base Case - If there is space to add the node (subtree is empty), then the correct place has been foudn and the item can be inserted.
* Smaller Problem - Insert a value into either the left subtree or the right subtree based on the value.

Example:
```python
def insert(self, data):
	"""
	Insert 'data' into the BST.  If the BST
	is empty, then set the root equal to the new 
	node.  Otherwise, use _insert to recursively
	find the location to insert.
	"""
	if self.root is None:
		self.root = BST.Node(data)
	else:
		self._insert(data, self.root)  # Start at the root

def _insert(self, data, node):
	"""
	This function will look for a place to insert a node
	with 'data' inside of it.  The current subtree is
	represented by 'node'.  This function is intended to be
	called the first time by the insert function.
	"""
	if data < node.data:
		# The data belongs on the left side.
		if node.left is None:
			# We found an empty spot
			node.left = BST.Node(data)
		else:
			# Need to keep looking.  Call _insert recursively on the left subtree.
			self._insert(data, node.left)
	elif data >= node.data:
		# The data belongs on the right side.
		if node.right is None:
			# We found an empty spot
			node.right = BST.Node(data)
		else:
			# Need to keep looking.  Call _insert recursively on the right subtree.
			self._insert(data, node.right)
```

</br>

### Traversing
A BST is traversed when we want to display all the data in the tree. This is done by either visiting each node from smallest to largest or largest to smallest.

Traversing a BST is a recursive process:
* Base Case - If the subtree is empty, then don't recursively traverse or use anything.
* Smaller Problem - Traverse the left subtree of a node, use the current node, and then traverse the right subtree of the node. (This could also be done in reverse, right and then left.)

Example:
```python
def __iter__(self):
	"""
    Perform a forward traversal (in order traversal) starting from 
    the root of the BST.  This is called a generator function.
    This function is called when a loop	is performed:

	for value in my_bst:
		print(value)

	"""
	yield from self._traverse_forward(self.root)  # Start at the root

def _traverse_forward(self, node):
	"""
	Does a forward traversal (in-order traversal) through the 
	BST.  If the node that we are given (which is the current
	subtree) exists, then we will keep traversing on the left
	side (thus getting the smaller numbers first), then we will 
	provide the data in the current node, and finally we will 
	traverse on the right side (thus getting the larger numbers last).

	The use of the 'yield' will allow this function to support loops
	like:

	for value in my_bst:
		print(value)

    The keyword 'yield' will return the value for the 'for' loop to
    use.  When the 'for' loop wants to get the next value, the code in
    this function will start back up where the last 'yield' returned a 
    value.  The keyword 'yield from' is used when our generator function
    needs to call another function for which a `yield` will be called.  
    In other words, the `yield` is delegated by the generator function
    to another function.

	This function is intended to be called the first time by 
	the __iter__ function.
	"""
	if node is not None:
		yield from self._traverse_forward(node.left)
		yield node.data
		yield from self._traverse_forward(node.right)
```
Note: A reverse traversal is frequently assoiated with the **\__reversed__** function in Python.

</br>

## Big O Notation
Note: This information is under the assumption you are using a balance BST. If your BST is not balanced, it is highly likely your performance will be worse than what this table states. \
Common BST functions:
Operation | Description | Performance
--------- | ----------- | -----------
insert(value) | Insert a value into the tree. | O(log n) - Recursively search the subtrees to find the next available spot
remove(value) | Remove a value from the tree. | O(log n) - Recursively search the subtrees to find the value and then remove it. This will require some cleanup of the adjacent nodes.
contains(value) | Determine if a value is in the tree. | O(log n) - Recursively search the subtrees to find the value.
traverse_forward | Visit all objects from smallest to largest. | O(n) - Recursively traverse the left subtree and then the right subtree.
traverse_reverse | Visit all objects from largest to smallest. | O(n) - Recursively traverse the right subtree and then the left subtree.
height(node) | Determine the height of a node. If the height of the tree is needed, the root node is provided. | O(n) - Recursively find the height of the left and right subtrees and then return the maximum height (plus one to account for the root).
size() | Return the size of the BST. | O(1) - The size is maintained within the BST class.
empty() | Returns true if the root node is empty. This can also be done by checking the size for 0. | O(1) - The comparison of the root node or the size.

Note: Python does not have a built-in BST class. There are packages that can be installed that provide implementations for a BST. Many people create their own BST class in Python. Thus, if you make your own class, be sure that your performance matches what is expected.

</br>

## Code Example
### Matching Elements
Given two binary search trees consisting of unique positive elements, check whether the two BSTs conatin the same set of elements or not.

&nbsp;&nbsp;&nbsp;&nbsp;`Input: `

![input bst](example_prob_bst.png)

&nbsp;&nbsp;&nbsp;&nbsp;`Output: Yes, they contain the same elements`

Method: A property of BSTs is that inorder traversal of a BST generates a sorted array. Thus, we can do inorder traversal of both the BSTs and generate two arrays and finally, we can compare these two arrays. If both of the arrays are the same, then the BSTs are have the same elements. Otherwise, the elements of the two BSTs are different.

```python
# Program to check if two BSTs contains
# same set of elements
 
# BST Node
class Node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None
 
# Utility function to create Node
def Node_(val1):
 
    temp = Node()
    temp.data = val1
    temp.left = temp.right = None
    return temp
 
v = []
 
# Function to insert elements of the
# tree to map m
def storeInorder(root):
 
    if (root == None):
        return
    storeInorder(root.left)
    v.append(root.data)
    storeInorder(root.right)
 
# Function to check if the two BSTs contain
# same set of elements
def checkBSTs(root1, root2):
 
    # Base cases
    if (root1 == None and root2 == None) :
        return True
    if ((root1 == None and root2 != None) or \
        (root1 != None and root2 == None)):
        return False
         
    # Create two hash sets and store
    # elements both BSTs in them.
    v1 = []
    v2 = []
    v = v1
    storeInorder(root1)
    v1 = v
    v = v2
    storeInorder(root2)
    v2 = v
     
    # Return True if both hash sets
    # contain same elements.
    return (v1 == v2)
 
 
# First BST
root1 = Node_(15)
root1.left = Node_(10)
root1.right = Node_(20)
root1.left.left = Node_(5)
root1.left.right = Node_(12)
root1.right.right = Node_(25)
     
# Second BST
root2 = Node_(15)
root2.left = Node_(12)
root2.right = Node_(20)
root2.left.left = Node_(5)
root2.left.left.right = Node_(10)
root2.right.right = Node_(25)
     
# Check if two BSTs have same set of elements
if (checkBSTs(root1, root2)):
    print("YES")
else:
    print("NO")
```

</br>

## Practice Problem
### Remove All Leaf Nodes From BST
Given a binary search tree, delete the leaf nodes from the binary search tree.

Example: \
&nbsp;&nbsp;&nbsp;&nbsp;`Input: 20 10 5 15 30 25 35` \
&nbsp;&nbsp;&nbsp;&nbsp;`Output: In order before deleting the leaf node` \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`5 10 15 20 25 30 35` \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`In order after deleting the leaf node` \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`10 20 30`

[Solution](delete_leaf_node.py)

</br>

## Return
[Back to Welcome Page](0_welcome.md)
