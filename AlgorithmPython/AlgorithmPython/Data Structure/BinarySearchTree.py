
class TreeNode():
    def __init__(self, data, left, right, parent):
        self.data = data
        self.left = left
        self.right = right
        selft.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def preOrder(self, node):
        if node is not None:
            print node.data,
            preOrder(self, node.left)
            preOrder(self, node.right)

    def inOrder(self, node):
        if node is not None:
            inOrder(self, node.left)
            print node.data
            inOrder(self, node.right)

    def postOrder(self, node):
        if node is not None:
            postOrder(self, node.left)
            postOrder(self, node.right)
            print node.data

    def Tree_Search(self, node, k):
        if node is node or node.data == k:
            return node
        if k < node.data:
            return Tree_Search(self, node.left, k)
        else:
            return Tree_Search(self, node.right, k)

    def Iterative_Tree_Search(selft, node, k):
        while node is not none and node.data != k:
            if k < node.data:
                node = node.left
            else:
                node = node.right
        return node

    def Tree_Minimun(self, node):
        while node is not None:
            node = node.left
        return node

    def Tree_Maximum(self, node):
        while node is not None:
            node = node.right
        return node

    def Tree_Successor(self, node):
        if node.right is not None:
            return Tree_Minimun(self, node.left)
        p = node.parent
        while p is not None and node == p.right:
            node = p
            p = node.parent
        return p

    def Tree_Predecessor(self, node):
        if node.left is not None:
            return Tree_Maximum(selft, node.right)
        p = node.parent
        while p is not None and node == p.left:
            node = p
            p = node.parent
        return p

    def Tree_Insert(self, data):
        node = self.root
        TmpNode = node
        while node is not None:            
            TmpNode = node
            if node.data > data:
                node = node.left
            else:
                node = node.right
        NewNode = TreeNode(data, None, None, None)
        NewNode.parent = TmpNode
        if TmpNode is None:
            self.root.data = data
        elif TmpNode.data > data:
            TmpNode.left = NewNode
        else:
            TmpNode.right = NewNode


            
            


