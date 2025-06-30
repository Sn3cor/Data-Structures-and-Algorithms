#operacje na BST
#   - wstawianie 
#   - max i min
#   - następnik i poprzednik

class Node:
    def __init__(self,value,parent = None):
        self.left = None
        self.right = None
        self.parent = parent
        self.value = value

    def insert(self,n_value):
        if self.right is None and self.value<n_value:
            self.right = Node(n_value,self)
        elif self.left is None and self.value>n_value:
            self.left = Node(n_value,self)
        elif self.value < n_value:
            self.right.insert(n_value)
        elif self.value > n_value:
            self.left.insert(n_value)

    def find_min(self):
        while self.left:
            self = self.left
        return self

    def find_max(self):
        pass

    def next(self):#szukamy następnika jakiegoś node'a niekoniecznie root'a
        if self.right is not None:
            return self.right.find_min()
        else:
            tmp = self
            while self.parent and self.parent.value<tmp.value:
                self = self.parent
            if self.value < tmp.value : 
                return None
            if self.right:
                return self.find_min()
            else:
                return self
            
#analogicznie robimy last()
