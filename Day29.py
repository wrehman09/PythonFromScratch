# leet code challenge for add 2 number 



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        
        node=l1
        num1=0
        i=1

        while node!=None:
            num1=int(num1)+int(node.val)*i
            node=node.next
            i=i*10
        
        node=l2
        num2=0
        i=1
        while node!=None:
            num2=int(num2)+int(node.val)*i
            node=node.next
            i=i*10
            

        
        sum=num1+num2

        i= True
        num=sum
        retnode=node=ListNode()

        for nu in str(sum):
           
           node.val=nu
           node2=ListNode()
           node2.next=node
           node=node2

        node=node.next

        return node

           
           

          
        
        







    






l1=ListNode()
l1.val="2"
l1.next=ListNode()
l1.next.val="4"
l1.next.next=ListNode()
l1.next.next.val="3"


l2=ListNode()
l2.val="5"
l2.next=ListNode()
l2.next.val="6"
l2.next.next=ListNode()
l2.next.next.val="4"




sol=Solution()
sol.addTwoNumbers(l1,l2)

   