# tree  removal 



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
            







    def preordertraverse(self):
        self.pretraverse(self.root)

    def inordertraverse(self):
        self.intraverse(self.root)
        
    def lookup(self,val):
        node=self.root
        while(node!=None):
            if(node.value==val):
                print(f"{val} Found")
                return
            else:
                if(node.value<val):
                    node=node.right
                else:
                    node=node.left
        print(f"{val} Not found")

    def remove(self,val):
        node=self.root
        parentnode=None
        found=True
        while(node!=None):
            if(node.value==val):
                print(f"{val} Found")  
                found=False              
                break
            else:
                if(node.value<val):
                    parentnode=node
                    node=node.right
                else:
                    parentnode=node
                    node=node.left
        
        if(found):
            print(f"{val} Not found")
            return
        else:
            if(node.left==None and node.right==None):
                print("both child none")
                if(parentnode.value<val):
                    parentnode.right=None
                else:
                    parentnode.left=None
                print("Deleted")
            elif(node.left==None):
                print("Left  none")
                if(parentnode.value>val):
                    parentnode.left=node.right
                else:
                    parentnode.right=node.right
                print("Deleted")    
            elif(node.right==None):
                print("right none")
                if(parentnode.value>val):
                    parentnode.left=node.right
                else:
                    parentnode.right=node.right
                print("Deleted")  
            else:
                print("Both child not none")
                rightChild=node.right
                
                leftNode=rightChild
                childparentNode=None

                while(leftNode.left!=None):
                    childparentNode=leftNode
                    leftNode=leftNode.left
                
                if(parentnode.value>val):
                    parentnode.left=leftNode
                else:
                    parentnode.right=leftNode

                if(childparentNode!=None):
                    childparentNode.left=leftNode.right
                    leftNode.right=childparentNode
                
                
                leftNode.left=node.left

                



                print("Deleted")
                

                


            



                




            
                    


        
                

       

        

        
        

    

print("Tree Program")

tr=Tree()
tr.insert(13)
tr.insert(54)
tr.insert(4)
tr.insert(17)
tr.insert(9)
tr.insert(6)
tr.insert(67)
tr.insert(58)
tr.insert(83)



print("inserted")
tr.preordertraverse()

#tr.lookup(17)
#tr.lookup(68)


tr.remove(54)




# tr.preordertraverse()

tr.preordertraverse()

                
                
                
        

        