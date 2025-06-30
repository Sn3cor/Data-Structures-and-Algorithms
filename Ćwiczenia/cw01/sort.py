class Node():
	def __init__(self,value):
		self.value = value
		self.next = None

def bubble(T):
	N = len(T)
	for i in range(N):
		for j in range(i+1,N):
			if T[i]>T[j]:
				T[i],T[j]=T[j],T[i]
	return T


def selection2(head,n):
	head1 = head
	sorted_ = None
	for i in range(n):
		max_value = head
		max_ptr=None
		prev_max_ptr=None
		prev=None
		itr = head1
		while itr is not None:
			if itr.value>max_value:
				prev_max_ptr = prev
				max_ptr = itr
				max_val = itr.val
			prev = itr
			itr = itr.next
		if sorted_ == None:
			prev_max_ptr.next = max_ptr.next
			sorted_ = max_ptr
			sorted_.next=None
		else:
			pass