class node(object):
    def __init__(self,data,parent = None,left = None,right = None,color = None):
        self.data = data
        
        self.parent = parent
        
        self.left = left
        
        self.right = right
        
        self.color = color
        
    def isRoot(self):
        
        return not self.parent
    

class redblack(object):
    def __init__(self):
        self.root = None
        
    
    
    def insert(self,root,value):
        
    
            
        if self.root is None:
            self.root = node(value,color = "black")
            
        elif root.data < value:
            
             if root.right is not None:
                 
                  self.insert(root.right,value)
                 
             else:
                root.right = node(value,color = "red",parent = root)
                
                self.update(root.right)
        
        elif root.data > value:
            
            if root.left is not None:
                
                 self.insert(root.left,value)
                
            else:
                root.left = node(value,color = "red",parent = root)
                
                self.update(root.left)
                
    def update(self,x):
        
        if x.parent.color == "red" and not x.isRoot():
            
            if x.parent == x.parent.parent.right:
                
                y = x.parent.parent.left
                
                if y is not None and y.color == "red":
                    
                    y.color = "black"
                    
                    x.parent.color = "black"
                    
                    x.parent.parent.color = "red"
                    
                    x = x.parent.parent
                    
                elif y is None or (y is not None and y.color == "black") :
                    
                    self.leftrotate(x.parent.parent)
                    
            elif x.parent == x.parent.parent.left:
                
                y = x.parent.parent.right
                
                if y is not None and y.color == "red":
                    
                    y.color = "black"
                    
                    x.parent.color = "black"
                    
                    x.parent.parent.color = "red"
                    
                elif y is None or(y is not None and y.color == "black"):
                    
                    self.rightrotate(x.parent.parent)
                    
            elif x.parent == x.parent.parent.left and x is x.parent.right:
                
                self.leftrotate(x.parent)
                
                self.rightrotate(x.parent.parent)
                
            elif x.parent == x.parent.parent.right and x is x.parent.left:
                
                self.rightrotate(x.parent)
                
                self.leftrotate(x.parent.parent)
                
        self.root.color = "black"
        
                    
    def rightrotate(self,root):
        
        newroot = root.left
        
        root.left = newroot.right
        
        if newroot.right is not None:
            
            newroot.right.parent = root
            
        newroot.parent = root.parent
        
        if root.isRoot():
            
            self.root = newroot
        else:
            
            if root.parent.left is not None:
                
                root.parent.left = newroot
            else:
                
                root.parent.right = newroot
                
        newroot.right = root
        
        root.parent = newroot
        
        temp = root.color
        
        root.color = newroot.color
        
        newroot.color = temp
        
    def leftrotate(self,root):
        
        newroot = root.right
        
        root.right = newroot.left
        
        if newroot.left is not None:
            
            newroot.left.parent = root
            
        newroot.parent = root.parent
        
        if root.isRoot():
            
            self.root = newroot
        else:
            if root.parent.right is not None:
                
                root.parent.right = newroot
            else:
                
                root.parent.left = newroot
                
        newroot.left = root
        
        root.parent = newroot
        
        temp = root.color
        
        root.color = newroot.color
        
        newroot.color = temp
        
    def inorder(self,root):
        
        if root is not None:
            
            self.inorder(root.left)
            
            print(root.data)
            
            self.inorder(root.right)
            
def main():
    
    Tree = redblack()
    
    rdtree = [7,6,5,4,3,2,1]
    
    for item in rdtree:
        
        Tree.insert(Tree.root,item)
        
    print("inorder")
    
    print(Tree.inorder(Tree.root))
main()
        
            
                 
    
        