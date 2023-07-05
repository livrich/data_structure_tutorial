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


