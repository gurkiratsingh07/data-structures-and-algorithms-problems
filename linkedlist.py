# A simple Python Program to introduce a linked list

# Node class
class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

# Linked List class contains a node object    
class LinkedList:
    
    #Function to initialize head
    def __init__(self):
        self.head=None
    
    #printing contents starting from head
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
            print(temp)
        
        
            
#code execution starts here
if __name__=='__main__':
    
    #start with the empty list
    llist=LinkedList()
    
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)
    
    llist.head.next=second;
    second.next=third;

    llist.printList()