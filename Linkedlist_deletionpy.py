class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
        
        
class LinkedList:
    
    def __init__(self):
        self.head=None
        
        
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
        
    #deleting the first node
    
    def deleteNode(self,key):
        
        #Store the head node
        temp=self.head
        
        if(temp is not None):
            if(temp.data==key):
                self.head=temp.next
                temp=None
                return
          
        # Search for the key to be deleted,keep track of the
        # previous node as we need to change 'prev.next'
        
        while(temp is not None):
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
            
        if(temp == None):
            return
        
        prev.next=temp.next
        
        temp=None
            
    
    def printList(self):
        temp=self.head
        while(temp):
            print(" %d" %(temp.data)),
            temp=temp.next
                      
        
llist=LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)           

print("Created Linked List:")
llist.printList()
llist.deleteNode(1)
print("\nLinked List after Deletion of 1:")
llist.printList()


 
        
        