#graph 



class Graph():
    def __init__(self) -> None:
        self.length=0
        self.adjacentList={}

    def addNodes(self,value):
        self.adjacentList[value]=[]
        self.length+=1

    def addEdge(self,node1,node2):
        
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

        


gp=Graph()
gp.addNodes(0)
gp.addNodes(1)
gp.addNodes(2)
gp.addNodes(3)

gp.addEdge(0,2)
gp.addEdge(2,1)
gp.addEdge(2,3)
gp.addEdge(1,3)
print(gp.adjacentList)    

    
    
