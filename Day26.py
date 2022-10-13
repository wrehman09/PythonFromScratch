# tree 

class Node():
    
    def __init__(self) -> None:
        self.value=None
        self.left=None
        self.right=None

    


class Tree():
    def __init__(self) -> None:
        self.root=Node()
        self.length=0

    def insert(self,val):
        if(self.root.value==None):
            self.root.value=val
            self.length+=1
            print("root inserted")
        else:
            
            node=self.root
            while(True):
                if(node.value<val):
                    if(node.right!=None):
                        node=node.right
                        
                    else:
                        node.right=Node()
                        node.right.value=val
                        self.length+=1
                       
                        break
                else:
                    if(node.left!=None):
                        node=node.left
                        
                    else:
                        node.left=Node()
                        node.left.value=val
                        self.length+=1
                        
                        break
            

            
    def pretraverse(self,node): # root , left then right
        print(node.value)
        if(node.left!=None):
            self.pretraverse(node.left)
        if(node.right!=None):
            self.pretraverse(node.right)

    def intraverse(self,node): # left root right or sorted tree
        
        if(node.left!=None):
            self.intraverse(node.left)
        print(node.value)
        if(node.right!=None):
            self.intraverse(node.right)  
            







    def traverse(self):
        self.intraverse(self.root)
        

       

        

        
        

    

print("Tree Program")

tr=Tree()
tr.insert(13)
tr.insert(54)
tr.insert(4)
tr.insert(17)
tr.insert(9)
tr.insert(67)

print("inserted")
tr.traverse()

                
                
                
        

        