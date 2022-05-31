class Node:
    def __init(self,data=None):
        self.val = data
        self.next = None 
'''
A circular linked list is a ring shape last reference variable points to the first node of the list.


 Attributes
    ----------
    value  : int
        a integer value in the node
    index : int
        element from the start of the list and returns the lowest index where the element appears. 
    
    Methods
    -------

    _get_last_()
        this is a helper function for the ring like structure helps in the insertion and the 
    remove operation on circular list


    insert(index=int ,val=int)
        insert the value in the list at the index position 
    
    delete(val=int)
        delete the value in the list

    __str__()
        represents the class objects as a string 


'''       

class Ring:
    
    def __init(self):
        self.head = None 

def __str__(self):
    ret_str = '['
    temp = self.head
    while temp is not None:
        ret_str += str(temp.val) + ', '
        temp = temp.next 
        
        if temp == self.head:
            break
            
    ret_str =ret_str.rstrip(', ')
    ret_str += ']'
        
    return ret_str
# Ring.__str__ = __str__   add function in the class by using the '.'

def _get_last(self):
    
    # when there is no node
    if self.head is None:
        return None 
    
    # at least two node in the list 
    temp = self.head.next     # run advacne once  
    while temp.next != self.head:
        temp = temp.next
    
    return temp




def insert(self,index,value):
    
    new_node = Node(value)
    last = self._get_last()
    
    # insertion at index 0 
    if index == 0:
        new_node.next = self.head 
        self.head = new_node
        
        if last is None:
            self.head.next = self.head 
        else:
            last.next = new_node
           
        return 
    
    if self.head is None and index > 0:
        raise IndexError("cannot insert at str(index) + " list is empty")
                                      
    # for index 3,4......
    temp = self.head 
    counter = 0 
    
    while temp is not None and counter < index:
        prev = temp 
        temp = temp.next
        counter +=1
        
    prev.next = new_node
    new_node.next = temp

    


def remove(self, val):
    
    # empty list
    if self.head is None:
        return None
    
    temp = self.head
    last = self._get_last()
    
    #first node match case
    if temp.val == val:
        if last == self.head:
            self.head = temp.next
            last.next = self.head
            
        else:
            self.head = temp.next
            last.next = self.head
        return
    
    # let move on the other nodes
    # temp hold the val that node will delete 
    prev = temp 
    temp = temp.next
    
    while temp != last.next:
        if temp.val == val:
            break
            
        prev = temp
        temp = temp.next
    if temp  == last.next:          # not found in the list 
        return 
    
    prev.next = temp.next
   
