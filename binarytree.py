class Queue:
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return self.queue == []
    
    def push(self,x):
        self.queue.append(x)
    def pop(self):
        if self.queue:
            a = self.queue[0]
            self.queue.remove(a)
            return a
        else:
            print("Queue empty")
        
    def size(self):
        return len(self.queue)

class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class tree(object):
    def __init__(self):
        self.root = None
        
    def insert(self,root,value):
        if self.root == None:
            self.root = Node(value)
        else:
            if value > root.data:
                if root.left is None:
                    root.left = Node(value)
                else:
                     self.insert(root.left,value)
            elif value < root.data:
                if root.right is None:
                    root.right = Node(value)
                else:
                     self.insert(root.right,value)
        return root 
    def inorder(self,root):
        if root == None:
            return 
        
        print(root.data)
        self.inorder(root.left)
        self.inorder(root.right)
    def node(self,root):
        if root is None:
            return 0
        else:
            return self.node(root.left) + self.node(root.right) + 1
    def fullnode(self,root):
        if root is None:
            return 0
        if root.left is not None and root.right is not None:
            return 1 + self.fullnode(root.left) + self.fullnode(root.right)
        else:
            return self.fullnode(root.left) + self.fullnode(root.right) 
        
    def halfnode(self,root):
        if root is None:
            return 0
        if (root.left is None and root.right is not None) or(root.right is None and root.left is not None):
                return 1 + self.halfnode(root.left) + self.halfnode(root.right)
        return self.halfnode(root.left) + self.halfnode(root.right)
    
    def height(self,root):
        if root is None:
            return 0
        return max(self.height(root.left),self.height(root.right)) + 1
    
    def leaves(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1 + self.leaves(root.left) + self.leaves(root.right)
        return self.leaves(root.left) + self.leaves(root.right)
    
    def levelorder(self,root):
        if root is None:
            return 
        q = Queue()
        q.push(root)
        node = None
        result = []
        while not q.isEmpty():
            node = q.pop()
            print(node.data)
            result.append(node)
            if node.right is not None:
                q.push(node.right)
            if node.left is not None:
                q.push(node.left)
    def sumofeachlevel(self,root):
        if root is None:
            return 
        q = Queue()
        q.push(root)
        maxsum = root.data
        node = None
        while not q.isEmpty():
            size = q.size()
            sum = 0
            while size > 0 :
                node = q.pop()
                sum = sum + node.data
                if node.left is not None:
                    q.push(node.left)
                if node.right is not None:
                    q.push(node.right)
                size = size - 1
            result = max(sum,maxsum)
        return result
    def maxofBinary(self,root):
        if root is None:
            return
        q = Queue()
        q.push(root)
        maxdata = float("-infinity")
        while not q.isEmpty():
            node = q.pop()
            if node.data > maxdata:
                maxdata = node.data
            if node.left is not None:
                q.push(node.left)
            if node.right is not None:
                q.push(node.right)
        return maxdata
                
    def pathfinder(self,root):
        paths = []
        self.pathsAppender(root,[],paths)
        for item in paths:
            print(item)
        return paths
        
    def pathsAppender(self,root,path,paths):
        if not root:
            return 0
        
        if  root.left is None and root.right is None:
            ans = []
            for item in path:
                ans.append(item)
            paths.append(ans + [root.data])
            
        if root.left:
                path.append(root.data)
                self.pathsAppender(root.left,path,paths)
                path.pop()
                
        if root.right:
                path.append(root.data)
                self.pathsAppender(root.right,path,paths)
                path.pop()
                
    def maxsumpath(self,root):
         result = self.pathfinder(root)
         lst = []
         for element in result:
             Sum = sum(element)
             lst.append(Sum)
             Sum = 0
         print(max(lst))
    
    def Pathsumfinder(self,root,val,path):
        answer = False
        if root is None:
            return
        subsum = val - root.data
        if subsum == 0 and root.right is None and root.left is None:
            path.append(root.data)
            print(path)
            return True
        if root.left:
            path.append(root.data)
            answer = answer or self.Pathsumfinder(root.left,subsum,path)
            path.pop()
        if root.right:
           path.append(root.data)
           answer = answer or self.Pathsumfinder(root.right,subsum,path)
           path.pop()
        return answer
    def Lca(self,root,n1,n2,v1 = False,v2 = False):
        if root is None:
            return None
        if root.data == n1:
            v1 = True
            return root
        if root.data == n2:
            v2 = True
            return root
        left_lca = self.Lca(root.left,n1,n2,v1,v2)
        right_lca = self.Lca(root.right,n1,n2,v1,v2)
        
        if left_lca and right_lca:
            return root.data
        else :
            return left_lca if left_lca is not None else right_lca
        
def main():
    Tree = tree()
    items = [3,5,2,1,4,6]
    for item in items:
        Tree.insert(Tree.root,item)
    print("Inorder Traversal")
    print(Tree.inorder(Tree.root), end = " ")
    print("Node")
    print(Tree.node(Tree.root))
    print("Full node")
    print(Tree.fullnode(Tree.root))
    print("HalfNode")
    print(Tree.halfnode(Tree.root))
    print("Height")
    print(Tree.height(Tree.root))
    print("Leaaves")
    print(Tree.leaves(Tree.root))
    print("Levelorder")
    print(Tree.levelorder(Tree.root))
    print("maxsum level")
    print(Tree.sumofeachlevel(Tree.root))
    print("Maximum of binary tree")
    print(Tree.maxofBinary(Tree.root))
    print("Path to leaf Nodde:")
    print(Tree.pathfinder(Tree.root))
    print("Maximum sum path")
    print (Tree.maxsumpath(Tree.root))
    print("Presence of sum 23")
    print(Tree.Pathsumfinder(Tree.root,6,[]))
    print("Lca of two numbers:")
    print(Tree.Lca(Tree.root,4,6,False,False))
main()
                
            
            
            