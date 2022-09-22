#linked list




class Node():
    

    def __init__(self,value):
        self.head=value
        self.next=None
    
    


class Linkedlist():
    

    def __init__(self,value):
        self.HeadNode=Node(value)
        self.TailNode=self.HeadNode
        self.length=1
        



    def append(self,val):
       
        node = Node(val)   
       
        self.TailNode.next=node       
        self.TailNode=node
        self.length=self.length+1
        

    def prepend(self,val):
        node=Node(val)
        node.next=self.HeadNode
        self.HeadNode=node
        self.length=self.length+1

    def traverse(self):
        node=self.HeadNode
        
        while(node.next!=None):  
            print(node.head)          
            node=node.next
        print(node.next)
    
    def insert(self,index,value):
        node=self.HeadNode
        i=0        
        while(node.next!=None):
            if(i==index-1):
                new_node=Node(value)
                new_node.next=node.next
                node.next=new_node
                self.length=self.length+1
                break
            else:
                node=node.next
            i=i+1

    def delete(self,index):
        node=self.HeadNode
        i=0        
        while(node.next!=None):
            if(i==index-1):
                node.next=node.next.next
                self.length=self.length-1
            else:
                node=node.next
            i=i+1




        

ll=Linkedlist(121)
ll.append(12)
ll.append(123)
ll.append(124)
ll.append(126)
ll.append(127)
ll.append(129)
ll.append(124)
ll.traverse()
ll.insert(3,999)
print("inserted")
ll.traverse()
ll.delete(3)
print("deleted")
ll.traverse()


