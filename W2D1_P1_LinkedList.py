class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head

    def insert(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode

    def printLinkedList(self):
        currentNode = self.head
        array = []
        while(currentNode != None):
            # print(currentNode.value)
            array.append(currentNode.value)
            currentNode = currentNode.next
        print(array)


# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList(1)

    llist.printLinkedList()
    ''' 
    Three nodes have been created. 
    We have references to these three blocks as head, 
    second and third 
  
    llist.head = llist.tail      
         |             
         |                
    +----+------+    
    | 1  | None |
    +----+------+     
    '''
    llist.insert(2)
    ''' 
    Now we insert the second node (value =2) to the tail 
  
    llist.head        llist.tail=second    third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  | null |     |  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''
    llist.insert(3)
    llist.printLinkedList()
    ''' 
    Now we insert the third node (value =2) to the tail
  
    llist.head        second              llist.tail = third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''
