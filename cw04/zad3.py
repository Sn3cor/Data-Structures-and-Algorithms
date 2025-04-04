#zmodyfikuj BST tak by operacje były O(n)
#   - znajdz i-ty element
#   - ktory co do wielkosci jest element x

class Node:
    def __init__(self,value,left=None,right=None,parent = None):
        self.left = left
        self.right = right
        self.parent = parent
        self.value = value
        self.size = left.size + right.size + 1


    def kth_element(self,k):
        l_size = 0 if self.left is None else self.left.size
        if k == l_size+1:
            return self
        if k<l_size+1:
            return self.kth_element(k)
        return self.kth_element(k-l_size+1)