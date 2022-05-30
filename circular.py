class Node:
    def __init(self,data=None):
        self.val = data
        self.next = None 
        

class Ring:
    
    def __init(self):
        self.head = None 

def __str__(self):
    ret_str = '['
    temp = self.head
    
    while tmep is not None:
        ret_str = str(temp.val) + ', '
        temp = temp.next 
        
        if temp == self.head:
            break
        ret_str =ret_str.rstrip(', ')
        ret_str += ret_str
        
        return 
Ring.__str__ = __str__

        