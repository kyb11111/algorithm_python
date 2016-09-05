

class TreeNode:
    def __init__(self, data, left, right, parent,color):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color

class RedBlackTree:
    def __init__(self):        
        self.Nil = TreeNode(None,None,None,None,None)
        self.root = Nil
    def preOrder(self, node):
        if node is not None:
            print node.data,
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            print node.data,
            self.inOrder(node.right)

    def postOrder(self, node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print node.data,

    def Tree_Search(self, node, k):
        if node is None or node.data == k:
            return node
        if k < node.data:
            return self.Tree_Search(node.left, k)
        else:
            return self.Tree_Search(node.right, k)

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

    #The successor of T is the smallest number bigger than T
    def Tree_Successor(self, node):
        if node.right is not None:
            return self.Tree_Minimun(node.right)
        p = node.parent
        while p is not None and node == p.right:
            node = p
            p = node.parent
        return p

    #The Predecessor of T is the biggest number smaller than T
    def Tree_Predecessor(self, node):
        if node.left is not None:
            return self.Tree_Maximum(node.left)
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
            self.root = NewNode
        elif TmpNode.data > data:
            TmpNode.left = NewNode
        else:
            TmpNode.right = NewNode

    def RB_Insert(self, data):
        Node = self.root
        TmpNode = Node
        while Node != self.Nil:
            TmpNode = Node
            if data < Node.data:
                Node = Node.left
            else:
                Node = Node.right
        NewNode = TreeNode(data,self.Nil,self.Nil,self.Nil,'RED')
        NewNode.parent = TmpNode
        if TmpNode == self.Nil:
            self.root = NewNode
        elif NewNode.data < TmpNode.data:
            TmpNode.left = NewNode
        else:
            TmpNode.right = NewNode
        RB_Insert_Fixup(NewNode)

    def RB_Insert_Fixup(self, Node):


        #relace the substree rooted at node u with the subtree root at node v
        #if u.parent is None u is the root so v is the new root 
    def Transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent
    
        #nodeSuc is the Successor of z if z has right child the successor must be the node in the subtree
        #if the nodeSuc is z.right replace z with nodSuc and let z.left to be nodeSuc.left
        #Otherwise, repace nodeSuc while nodeSuc.right and let z.right to be nodeSuc.right Then repace z with nodSuc
    def Tree_Delete(self, z):
        if z.left is None:
            self.Transplant(z, z.right)
        elif z.right is None:
            self.Transplant(z, z.left)
        else:
            nodeSuc = self.Tree_Minimun(z.right)
            if nodeSuc.parent != z:
                self.Transplant(nodeSuc, nodeSuc.right)
                nodeSuc.right = z.right
                nodeSuc.right.parent = nodeSuc
            self.Transplant(z, nodeSuc)
            nodeSuc.left = z.left
            nodeSuc.left.parent = nodeSuc

    def Left_Rotate(self, Node):
        RightNode = Node.right
        Node.right = RightNode.left
        if RightNode.left != self.Nil:
            RightNode.left.parent = Node
        RightNode.parent = Node.parent
        if Node.parent == self.Nil:
            self.root = RightNode
        elif Node == Node.parent.left:
            Node.parent.left = RightNode
        else:
            Node.parent.right = RightNode
        RightNode.left = Node
        Node.parent = RightNode

    def RightRotate(self, Node):
        LeftNode = Node.left
        Node.left = LeftNode.right
        if LeftNode.right != self.Nil:
            LeftNode.right.parent = Node
        LeftNode.parent = Node.parent
        if Node.parent == self.Nil:
            self.root = LeftNode
        elif Node == Node.parent.left:
            Node.parent.left = LeftNode
        else:
            Node.parent.right = LeftNode
        LeftNode.right = Node
        Node.parent = LeftNode
        
                
btree = BinarySearchTree()
btree.Tree_Insert(5)
btree.Tree_Insert(10)
btree.Tree_Insert(12)
btree.Tree_Insert(4)
btree.Tree_Delete(btree.Tree_Search(btree.root, 10))
print btree.Tree_Search(btree.root, 4), btree.Tree_Search(btree.root, 10)
btree.preOrder(btree.root)
print
btree.inOrder(btree.root)
print
btree.postOrder(btree.root)
print


            
            


