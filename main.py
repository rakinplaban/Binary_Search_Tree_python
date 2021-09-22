class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
    def insertNode(self,val):
        node = Node(val)
        if self.data:
            if self.data > val:
                if self.left is None:
                    self.left = node
                else:
                    self.left.insertNode(val)
            else:
                if self.right is None:
                    self.right = node
                else:
                    self.right.insertNode(val) 
                    
    def deleteNode(self,val):  
        if self.data > val:
            if self.left:
                self.left = self.left.deleteNode(val)
        elif self.data < val:
            if self.right:
                self.right = self.right.deleteNode(val)
        else:
            if self.left is None:
               return self.right
            elif self.right is None:
               return self.left
            else:
               largest = self.left.findMax()
               self.data = largest
               self.left = self.left.deleteNode(largest)
        return self
            
    def findNode(self,val):
        if self.data:
            if self.data == val:
                return True
            if self.data > val:
                try:
                    if self.left.findNode(val):
                        return True
                    else:
                        return False
                except AttributeError:
                    print(val,end=" ")
            if self.data <= val:
                if self.right.findNode(val):
                    return True
                else:
                    return False
            else:
                return False
        else:
             return False
                    
    def inorder(self):
        if self.data is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.data,end=" ")
            if self.right is not None:
                self.right.inorder()
            
    def preorder(self):
        if self.data is not None:
            print(self.data,end=" ")
            if self.left is not None:
                self.left.preorder()
            if self.right is not None:
                self.right.preorder()
            
    def postorder(self):
        if self.data is not None:
            if self.left is not None:
                self.left.postorder()
            if self.right is not None:
                self.right.postorder()
            print(self.data,end=" ")
        
    def findMin(self):
        if self.data:
            if self.left is None:
                return self.data
            else:
                return self.left.findMin()
                
    def findMax(self):
        if self.data:
            if self.right is None:
                return self.data
            else:
                return self.right.findMax()
            
rootdata = int(input("please insert Node data: "))
t1 = Node(rootdata)
t1.insertNode(53)
t1.insertNode(64)
t1.insertNode(50)
t1.insertNode(34)
t1.insertNode(21)
t1.insertNode(40)
t1.inorder()
print()
t1.preorder()
print()
t1.postorder()
print("\nThis tree has root data:",t1.data," with minimum node: ",t1.findMin()," and maximum node: ",t1.findMax())
t2 = Node(35)
t2.insertNode(21)
t2.insertNode(42)
print("\nThis tree has root data:",t2.data," with minimum node: ",t2.findMin()," and maximum node: ",t2.findMax())
print()
i = int(input("Please enter the node you want to find out: "))
if(t1.findNode(i) == True):
    print(i," found in t1 tree\n")
else:
    print(" not found in t1 tree")

print()
j = int(input("Enter a node to delete : "))
t1.deleteNode(j)
t1.inorder()
print()
t1.preorder()
print()
t1.postorder()
print()
print("\nThis tree has root data:",t1.data," with minimum node: ",t1.findMin()," and maximum node: ",t1.findMax())
