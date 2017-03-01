"""Implementation of AVL trees
@Author: Naveen Chaudhary"""
#!/bin/python3

class node:
    def __init__(self,data,left=None,right=None,parent = None,balanceFactor = 0):
        self.data = data
        self.right = right
        self.left = left
        self.parent = parent
        self.balanceFactor = 0
    def isRoot(self):
        return not self.parent
class avl:
    def __init__(self):
        self.root = None
        
    def insert(self,root,value):
        if self.root is None:
            self.root = node(value)
        else:
            if root.data > value:
                if root.left is None:
                    root.left = node(value,parent = root)
                    self.updatebalance(root.left)
                else:
                    self.insert(root.left,value)
            else:
                if root.right is None:
                    root.right = node(value,parent = root)
                    self.updatebalance(root.right)
                else:
                    self.insert(root.right,value)
    def updatebalance(self,root):
        if root.balanceFactor > 1 or root.balanceFactor < -1:
            self.rebalance(root)
            return
        if root.parent is not None:
            if root.parent.left is root:
                root.parent.balanceFactor += 1
            elif root.parent.right is root:
                root.parent.balanceFactor -= 1
            if root.parent.balanceFactor != 0:
                self.updatebalance(root.parent)
    def leftrotation(self,root):
        newroot = root.right
        root.right = newroot.left
        if newroot.left:
            newroot.left.parent = root
        newroot.parent = root.parent
        if root.isRoot():
            self.root = newroot
        else:
            if root.parent.left is root:
                root.parent.left = newroot
            else:
                root.parent.right = newroot
        newroot.left = root
        root.parent = newroot
        root.balanceFactor = root.balanceFactor + 1 - min(0,newroot.balanceFactor)
        newroot.balanceFactor = newroot.balanceFactor + 1 + max(0,root.balanceFactor)
        
    def rightrotation(self,root):
        newroot = root.left
        root.left = newroot.right
        if newroot.right:
            newroot.right.parent = root
        newroot.parent = root.parent
        if root.isRoot():
            self.root = newroot
        else:
            if root.parent.right is not None:
                root.parent.right = newroot
            else:
                root.right.parent = newroot
        newroot.right = root
        root.parent = newroot
        root.balanceFactor = root.balanceFactor -1 - max(newroot.balanceFactor,0)
        newroot.balanceFactor = newroot.balanceFactor - 1 + min(root.balanceFactor,0)
        
    def rebalance(self,root):
        if root.balanceFactor < 0:
            if root.right.balanceFactor > 0:
                self.rightrotation(root.right)
                self.leftrotation(root)
            else:
                self.leftrotation(root)
        elif root.balanceFactor > 0:
            if root.left.balanceFactor < 0 :
                self.leftrotation(root.left)
                self.rightrotation(root)
            else:
                self.rightrotation(root)
    def preorder(self,root):
        if root is not None:
            print(root.data);
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
def main():
    Tree = avl()
    avltree = [10,20,30,40,50,25]
    for item in avltree:
        Tree.insert(Tree.root,item)
    print("inorder")
    print(Tree.inorder(Tree.root))
main()
    
                
        
        
                
    