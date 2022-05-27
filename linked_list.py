class Node:

    def __init__(self, data=None):
        self.val = data
        self.next = None
    

'''A class used to represent collection of nodes, each node has some data and 
    reference variable that points to the next node.

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
class Linked_list:


    def __init__(self):
        self.head = None

    #Push the data into the list
    def push(self,val):                
        new_node = Node(val)                # first create a new node 
        
        #if head == null
        if self.head is None:
            self.next = new_node
        
        # if one or more node in the list 
        last = self.head
        while last.next is not None:
            last = last.next

        last.next = new_node

    # function convert into the string  

    def __str__(self):

        ret_str ='['
        temp = self.head
        while temp is not None:
            ret_str += str(temp.val) + ', '
            temp =temp.next
        ret_str = ret_str.rstrip(', ')
        ret_str += ']'
        return ret_str
        

    def pop(self):

        # when there is no node 
        if self.head is None:
            raise Exception('can not pop. no value in the list')

        # when only one node in the list
        if self.head.next is None:
            val = self.head.val
            self.head = None            # automatic garbage collection
            return val 
        ## when more than one node in the list 
        # reach at the end of the list

        temp = self.head 
        while temp.next is not None:
            prev = temp
            temp = temp.next

        val = temp.val
        prev.next = None 
        return val 


    def insert(self, index, value):
        # first make a new node 
        new_node = Node(value)

        # insert at the index 0
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # insert at any index in the list 
        temp = self.head 
        counter = 0
        while temp is not None and counter < index:
            prev = temp 
            temp = temp.next
            counter += 1

        prev.next = new_node
        new_node.next = temp
        
# Linked_list.insert = insert ---> add function in the classes after the class 

    def remove(self, value):
        
        temp = self.head

        # to check first node

        if temp is not None:
            if temp.val == value:
                self.head = temp.head
                temp.next = None
                return 
        
        #remove in the mid of the list 

        while temp is not None:
            if temp.val == value:
                break 
                
            prev = temp
            temp = temp.next

        if temp is None:
            return 
        
        prev.next = temp.next           
