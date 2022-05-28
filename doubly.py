class Node:

    def __init__(self,data=None):
        self.val = data 
        self.next = None
        self.prev = None 
class doubly:

    '''
    A doubly connected linked list is a type of list in which two reference variables 
    next and previous it is a collection of nodes, each node has some data and 
    reference variables
    
    ...

    Attributes
    ----------
    value  : int
        a integer value in the node
    index : int
        element from the start of the list and returns the lowest index where the element appears. 
    
    Methods
    -------
    
    push(self)
        push the value in the list 
    
    pop(self)
       pop the value from the list 
    
    insert(index=int ,val=int)
        insert the value in the list at the index position 
    
    delete(val=int)
        push the value in the list




    
    
    '''

    def __init__(self):
        self.head = None
    
    def push(self, val):
        new_node = Node(val)

        #at the begining of the list 
        if self.head is None:
            self.head = new_node
            return 
        
        # for the 2nd case

        last = self.head 
        while last.next is not None:
            last = last.next

        last.next = new_node
        new_node.prev = last 

    def pop(self):

        if self.head is None:
            raise Exception('no val, no node in the list')

        # for the first node 
        if self.head.next is None:
            val = self.head.val
            self.head = None 
            return val 

        # where more than nodes in the list

        temp = self.head 
        while temp.next is not None:
            prev = temp 
            temp = temp.next 
        
        val = temp.val
        prev.next = None 
        return val 

    def insert(self, index, value):
        new_node = Node(val)

        # insert at the index 0
        if index == 0:
            new_node.next = self.head 
        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node 

        # insert other places in list 

        temp = self.head 
        counter = 0 
        while temp.next is not None and counter < index:
            prev = temp 
            temp =temp.next

        prev.next = new_node
        new_node.prev = prev

        new_node.next = temp
        if temp is not None:
            temp.prev = new_node 


    def remove(self, value):

        if self.head is None:
            self.head = self.head.next

            if self.head is not None:
                self.head.prev = None
            
        
        #remove in the mid of the list 
        temp =self.head 
        while temp is not None:
            if temp.val == value:
                break 
                
            prev = temp
            temp = temp.next

        if temp is None:
            return 
        
        prev.next = temp.next         

    def __str__(self):
        ret = "["

        temp = self.head
        while temp is not None:
            ret += str(temp.val) + ","
            temp = temp.next

        ret = ret.rstrip(",")
        ret += "]"

        return ret