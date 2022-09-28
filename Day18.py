# stack and queue using array and linked list

#stack as array / list

class Stack():
    
    def __init__(self) -> None:
        self.Stack=[]
    
    def Push(self,value):
        self.Stack.append(value)
        return self.Stack
    
    def Pop(self):
        self.Stack.pop()
    
    def Peek(self):
        print(self.Stack)
    

stack=Stack()
stack.Push(1)
stack.Push(2)
stack.Push(3)
stack.Push(5)
stack.Pop()
print(stack.Push(4))





