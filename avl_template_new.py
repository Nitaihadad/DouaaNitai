#username -
#id1      - 206360521
#name1    - Douaa Satel
#id2      - 208784843
#name2    - Nitai Hadad
from random import randrange


"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields.

	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1 # Balance factor
		self.size = 1

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		return self.height

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""

	def setLeft(self, node):
		self.left = node

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = node

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent = node

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		self.value = value

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
		self.height = h

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		return self.getSize() != 0 and self.getHeight() != -1


	"""
	Returns LEFT if curr node is left child of its parent, RIGHT if right child, and ROOT else.
	"""
	def childDirection(self):
		if self.parent == None:
			return "ROOT"
		elif self.getParent().getLeft() == self:
			return "LEFT"
		else:
			return "RIGHT"

	def getSize(self):
		return self.size

	def setSize(self,s):
		self.size = s




##Helper functions used in AVLTreeList

def mergeSort(arr):  ##helper function for sort
	if len(arr) > 1:
		mid = len(arr) // 2
		L = arr[:mid]
		R = arr[mid:]
		mergeSort(L)
		mergeSort(R)
		i = j = k = 0
		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
	pass

def shuffle(arr):
	for i in reversed(range(1, len(arr))):
		j = randrange(i + 1)
		temp = arr[i]
		arr[i] = arr[j]
		arr[j] = temp
	pass

"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.

	"""
	def __init__(self):
		self.len = 0
		self.root = None
		self.VIRTUALNODE = AVLNode(None)
		self.VIRTUALNODE.setSize(0)



	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return (self.len == 0)


	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self, i):
		node = self.get(i)
		if node == None:
			return None
		return node.getValue()


	'''return the i'th node'''
	def get(self,i):
		def get_rec(node,i):
			left_subtree_size = 0
			if node.getLeft().isRealNode():
				left_subtree_size = node.getLeft().getSize()
			if i==left_subtree_size: #if the left subtree size is i, the current node is th i'th node
				return node
			else:
				if i<node.getLeft().getSize(): #if the left subtree size is greather then i, the i'th node is in the left sub tree of the current node, search by recursion
					ind = i
					return get_rec(node.getLeft(), ind)
				else: #if the left subtree size is less then i, the i'th node is in the right sub tree of the current node, search by recursion with updated i
					ind = i-node.getLeft().getSize()-1
					return get_rec(node.getRight(),ind)

		if i >= self.length() or i<0:
			return None
		else:
			return get_rec(self.root,i)

	def setRoot(self,node):
		self.root = node



	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, i, val):
		new_node = AVLNode(val)
		low_node = new_node
		new_node.setRight(self.VIRTUALNODE)
		new_node.setLeft(self.VIRTUALNODE)
		if self.len == 0 and i==0: #for the first node of the tree, make it the node
			self.root = new_node
			self.len=1
		elif i == 0: #if i=0, the new node should be the left son of the current 0'th node, which is the min node
			parent = self.getMinNode()
			parent.setLeft(new_node)
			new_node.setParent(parent)
			self.len += 1

		elif self.len == i: #if i=len, the new node should be the right child of the current last node, which is the max node
			parent = self.getMaxNode()
			parent.setRight(new_node)
			new_node.setParent(parent)
			self.len += 1
		else:
			node = self.get(i)
			if not (node.getLeft().isRealNode()): #if the current i'th node doesn't have a left child, make the new node its left child
				# node.setRight(new_node)
				# new_node.setParent(node)
				node.setLeft(new_node)
				new_node.setParent(node)
				self.len += 1

			else: #if the current i'th node has a left child, make the new node its predecessor right child (for sure, it doesn't have a right child
				# sucessor = self.getSucessor(node)
				# succ_curr_left = sucessor.getLeft()
				# sucessor.setLeft(new_node)
				# new_node.setParent(succ_curr_left)
				predecessor = self.getPredecessor(node)
				if predecessor == None:
					tmp = self.root
					self.root = new_node
					new_node.setRight(tmp)
					tmp.setParent(new_node)
					low_node = tmp
					self.len += 1
				else:
					predecessor_curr_right = predecessor.getRight()
					predecessor.setRight(new_node)
					new_node.setParent(predecessor)
					self.len += 1


		rotations_cnt = self.rebalance(low_node) #rebalance the tree to keep it an avl, and update node fields
		self.updateHeight(low_node)
		self.updateSize(low_node)
		return rotations_cnt



	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		if i >= self.length() or i<0:
			return -1
		node = self.get(i)
		parent = node.getParent()
		left = node.getLeft()
		right = node.getRight()
		direction = node.childDirection()

		if direction == 'ROOT' and self.len == 1: #if the tree is has one node and we need to remove it, remove the root
			self.root = None
			self.len = 0
			return 0

		rotations_cnt = 0
		if left.isRealNode() and right.isRealNode(): #if the node both childs are real, need to find and remove the succ and replace the deleted node with it
			succ = self.getSuccessor(node)
			succ_right_child = succ.getRight()
			succ_parent = succ.getParent()


			if succ != node.getRight():
				succ_right_child.setParent(succ_parent) #romove succ from tree, succ don't have left child
				succ_parent.setLeft(succ_right_child)
				succ.setRight(node.getRight())
				succ.getRight().setParent(succ)
				node.setRight(None)


			succ.setLeft(node.getLeft()) #replace succ with node
			node.setLeft(None)
			succ.getLeft().setParent(succ)

			succ.setParent(parent)
			if direction == 'LEFT':
				parent.setLeft(succ)
			elif direction == 'RIGHT':
				parent.setRight(succ)
			node.setParent(None)


			if direction == 'ROOT':
				self.root = succ

			if succ != node.getRight():
				rotations_cnt = self.rebalance(succ_parent)
				self.updateSize(succ_parent)

			else:
				rotations_cnt = self.rebalance(succ)
				self.updateSize(succ)


		else:
			node_is_left_child = direction == 'LEFT'
			node_child = self.VIRTUALNODE              #the deafult is virtual, will change if the node has one son and wouldn't if not

			if left.isRealNode():
				left.setParent(parent)
				node_child = left
			elif right.isRealNode():
				right.setParent(parent)
				node_child = right

			if direction!='ROOT':
				if node_is_left_child:
					parent.setLeft(node_child)
				else:
					parent.setRight(node_child)


				parent.setSize(parent.getSize()-1)
				if node_child.isRealNode():
					self.updateSize(node_child)
				else:
					self.updateSize(parent)

			elif node_child.isRealNode():
				self.root = node_child
				self.updateSize(node_child)


			if node_child.isRealNode():
				node_child.setParent(parent)
				rotations_cnt = self.rebalance(node_child)
				self.updateSize(node_child)


			else:
				rotations_cnt = self.rebalance(parent)
				self.updateSize(parent)

		self.len -=1


		return rotations_cnt

	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		if self.len == 0:
			return None
		else:
			return  self.retrieve(0)



	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		if self.length() == 0:
			return None
		else:
			idx= self.length() - 1
			return self.retrieve(idx)
	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self): ##time complexity:
		if self.empty():
			return None
		else:
			listArr= ([self.retrieve(i) for i in range(self.length())]) #create an array and use retrieve to hold the values the list elements
			return listArr

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self): #time complexity O(1)
		if self.getRoot() == None:
			return 0
		rootNode= self.getRoot()
		sizeTree= rootNode.getSize()
		return sizeTree
	"""sort the info values of the list

	@rtype: list
	@returns: an AVLTreeList where the values are sorted by the info of the original list.
	"""
	def sort(self):
		if self.empty():
			return None
		T1= AVLTreeList() ## make a copy of the self tree
		arr = self.listToArray() ##store sorter list of elements
		mergeSort(arr)
		newArr=[]
		for i in range (len(arr)):
			T1.insert(i, newArr[i])
		return T1

	"""permute the info values of the list 

	@rtype: list
	@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
	"""
	def permutation(self):
		if self.empty():
			return None
		T1 = AVLTreeList()
		arr = self.listToArray()
		shuffle(arr)
		for i in range(len(arr)):
			T1.insert(i, arr[i])
		return T1

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""

	def concat(self, lst):
		if (self.empty() and lst.empty()):  # both trees are empty
			return 0
		elif (self.empty()):
			self.setRoot(lst.getRoot())
			self.len = lst.length()
			return abs(self.getTreeHeight() - (-1))
		elif (lst.empty()):
			return abs(self.getTreeHeight() - (-1))
		lstHeight = lst.getTreeHeight()  # initialize lst height
		selfHeight = self.getTreeHeight()  # initialize tree height for self
		# if neither of the trees are empty:
		slf1 = self.length()
		lst1 = lst.length()
		self.len = self.length() + lst.length()
		if selfHeight < lstHeight and self.length() == 1:  ##if self is simple one node then insert into lst
			curr = lst.get(0)
			curr.setLeft(self.getRoot())
			self.getRoot().setParent(curr)
			self.setRoot(lst.getRoot())
			self.updateSize(curr)
			self.updateHeight(curr)
			self.rebalance(curr)
			return abs(selfHeight - lstHeight)
		elif selfHeight > lstHeight and lst.length() == 1:  # if we just need to insert one node from lst
			curr = self.get(self.length() - 1)
			curr.setRight(lst.getRoot())
			lst.getRoot().setParent(curr)
			self.updateSize(curr)
			self.updateHeight(curr)
			self.rebalance(curr)
			return abs(selfHeight - lstHeight)
		elif selfHeight > lstHeight:
			rightMostNode = (self.get(self.length() - 1))
			lowestNode = rightMostNode.getParent()
			self.delete(self.length() - 1)
			self.len += 1     #node will be add manually and not by insert, need to keep the len field updated
			curr = self.getRoot()
			h = lst.getTreeHeight()
			while curr.getHeight() >= h + 1:
				curr = curr.getRight()
			b = curr
			c = b.getParent()
			rightMostNode.setParent(c)
			rightMostNode.setRight(lst.getRoot())
			lst.getRoot().setParent(rightMostNode)
			rightMostNode.setLeft(b)
			b.setParent(rightMostNode)

			if c != None:
				c.setRight(rightMostNode)
			else:
				self.getRoot().setParent(rightMostNode)
				self.setRoot(rightMostNode)
				rightMostNode.setParent(None)
			if lowestNode != None:
				self.updateHeight(lowestNode)
				self.updateSize(lowestNode)
				self.rebalance(lowestNode)
			else:
				self.updateHeight(rightMostNode)
				self.updateSize(rightMostNode)
				self.rebalance(rightMostNode)
			return abs(selfHeight - lstHeight)
		elif selfHeight < lstHeight:
			LeftMostNode = (lst.get(0))
			lowestNode = LeftMostNode.getParent()
			lst.delete(0)
			curr = lst.getRoot()
			h = self.getTreeHeight()
			while curr.getHeight() >= h + 1:
				curr = curr.getLeft()
			b = curr
			c = b.getParent()
			LeftMostNode.setParent(c)
			LeftMostNode.setLeft(self.getRoot())
			LeftMostNode.setRight(b)
			b.setParent(LeftMostNode)
			self.getRoot().setParent(LeftMostNode)
			if c != None:
				c.setLeft(LeftMostNode)
				self.getRoot().setParent(lst.getRoot())
				self.setRoot(lst.getRoot())
			else:
				self.getRoot().setParent(LeftMostNode)
				self.setRoot(LeftMostNode)
				LeftMostNode.setParent(None)
			if lowestNode != None:
				self.updateHeight(lowestNode)
				self.updateSize(lowestNode)
				self.rebalance(lowestNode)
			else:
				self.updateHeight(LeftMostNode)
				self.updateSize(LeftMostNode)
				self.rebalance(LeftMostNode)
			return abs(selfHeight - lstHeight)
		elif selfHeight == lstHeight and selfHeight == 1:
			lst.getRoot().setParent(self.getRoot())
			self.getRoot().setRight(lst.getRoot())
			self.updateHeight(self.getRoot())
			self.updateSize(self.getRoot())
			return 0
		else:  # selfheight==lstheight
			rightMostNode = (self.get(self.length() - 1))
			lowestNode = rightMostNode.getParent()
			if lowestNode == None:
				lowestNode = rightMostNode
			self.delete(self.length() - 1)
			self.len += 1
			b = lst.getRoot()
			rightMostNode.setLeft(self.getRoot())
			rightMostNode.setRight(b)
			self.getRoot().setParent(rightMostNode)
			b.setParent(rightMostNode)
			self.setRoot(rightMostNode)
			rightMostNode.setParent(None)
			self.updateHeight(lowestNode)
			self.updateSize(lowestNode)
			self.rebalance(lowestNode)

		return abs(selfHeight - lstHeight)

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val): #O(nlogn)
		for i in range (self.length()):
			if self.retrieve(i)== val:
				return i
		return -1



	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return self.root


	"""
	rotate right the edge between child node and parent node, and update heights
	@rtype: child node left node, and parent node as right node
	@returns: None
	"""
	def rightRotation(self, child_node,parent_node):
		grand_parent = parent_node.getParent()
		parent_direction = parent_node.childDirection()
		is_parent_left_child = parent_direction == "LEFT"
		is_parent_right_child = parent_direction == "RIGHT"
		is_parent_root = parent_direction == "ROOT"


		parent_node.setLeft(child_node.getRight())
		# parent_node.getLeft().getParent().setParent(parent_node)
		parent_node.getLeft().setParent(parent_node)


		if is_parent_left_child:
			grand_parent.setLeft(child_node)
		elif is_parent_right_child:
			grand_parent.setRight(child_node)
		if not is_parent_root:
			child_node.setParent(grand_parent)
		else:
			child_node.setParent(None)
			self.root = child_node

		child_node.setRight(parent_node)
		parent_node.setParent(child_node)

		child_node.setHeight(child_node.getHeight()+1)
		parent_node.setHeight(parent_node.getHeight()-1)


	"""
	rotate right the edge between child node and parent node, and update heights
	@rtype: child node right node, and parent node as left node
	@returns: None
	"""
	def leftRotation(self, child_node, parent_node):
		grand_parent = parent_node.getParent()
		parent_direction = parent_node.childDirection()
		is_parent_left_child = parent_direction == "LEFT"
		is_parent_right_child = parent_direction == "RIGHT"
		is_parent_root = parent_direction == "ROOT"

		parent_node.setRight(child_node.getLeft())
		parent_node.getRight().setParent(parent_node)

		if is_parent_left_child:
			grand_parent.setLeft(child_node)
		elif is_parent_right_child:
			grand_parent.setRight(child_node)
		if not is_parent_root:
			child_node.setParent(grand_parent)
		else:
			child_node.setParent(None)
			self.root = child_node

		child_node.setLeft(parent_node)
		parent_node.setParent(child_node)

		child_node.setHeight(child_node.getHeight()+1)
		parent_node.setHeight(parent_node.getHeight()-1)



	""" 
	@rtype: AVLNode
	@returns: if index(node) = i, return the node in index i-1
	"""

	def getTreeHeight(self):
		return self.root.getHeight()

	def getPredecessor(self,node):
		predecessor = None
		curr = None
		if node.getLeft().isRealNode():
			curr = node.getLeft()
			while curr.getRight().isRealNode():
				curr = curr.getRight()
			predecessor = curr
		else:
			curr = node
			while curr.getParent() != None:
				curr_direction = curr.childDirection()
				if curr_direction == "RIGHT":
					predecessor = curr.getParent()
					break
				else:
					curr = curr.getParent()
		return predecessor


	""" 
	@rtype: AVLNode
	@returns: if index(node) = i, return the node in index i-1
	"""
	def getSuccessor(self, node):
		successor = None
		curr = None
		if node.getRight().isRealNode():
			curr = node.getRight()
			while curr.getLeft().isRealNode():
				curr = curr.getLeft()
			successor = curr
		else:
			curr = node
			while curr.getParent() != None:
				curr_direction = curr.childDirection()
				if curr_direction == "LEFT":
					successor = curr.getParent()
					break
				else:
					curr = curr.getParent()
		return successor

	"""
	traverse the tree bottom-up, and update the height of each subtree, all the way to the root
	@rtype: AVLNode, the lowest one in the tree that we need to changes
	@returns: None
	"""
	def updateHeight(self, lowest_node):
		curr = lowest_node
		curr = lowest_node
		if curr == self.VIRTUALNODE:
			curr = curr.getParent()
		while curr != None:
			curr.setHeight(max(curr.getLeft().getHeight(),curr.getRight().getHeight()) + 1)
			curr = curr.getParent()

	"""
	traverse the tree bottom-up, and update the size of each subtree, all the way to the root 
	@rtype: AVLNode, the lowest one in the tree that we need to changes
	@returns: None
	"""
	def updateSize(self, lowest_node):
		curr = lowest_node
		if curr == self.VIRTUALNODE:
			curr = curr.getParent()
		while curr != None:
			curr.size = 1 + curr.getLeft().getSize() + curr.getRight().getSize()
			curr = curr.getParent()


	""" 
	@rtype: AVLTree
	@returns: int, the height diff between node left subtree and node right subtree
	"""

	def getBfs(self,node):
		left_tree_height = node.getLeft().getHeight()
		right_tree_height = node.getRight().getHeight()
		bfs = left_tree_height - right_tree_height
		return bfs

	"""
	rebalance the tree, and update each changed node height
	@rtype: AVLTree
	@returns: rotations count
	"""

	def rebalance(self,lowest_node):
		self.updateHeight(lowest_node)
		cnt = 0
		curr = lowest_node
		if curr == self.VIRTUALNODE:
			curr = curr.getParent()
		while curr!=None:
			bfs = self.getBfs(curr)
			if -1<=bfs<=1:
				curr = curr.getParent()
				continue
			if bfs <= -2:
				right_child = curr.getRight()
				right_child_bfs = self.getBfs(right_child)
				if -1 <= right_child_bfs <= 0:
					self.leftRotation(right_child, curr)
					cnt += 1
					# curr.setHeight(curr.getHeight()-1)
					# right_child.setHeight(right_child.getHeight()+1)

				elif right_child_bfs == 1:
					right_child_left_child = right_child.getLeft()
					self.rightRotation(right_child_left_child,right_child)
					self.leftRotation(right_child_left_child, curr)
					self.updateSize(right_child)

					cnt += 2

			if bfs >= 2:
				left_child = curr.getLeft()
				left_child_bfs = self.getBfs(left_child)
				if left_child_bfs == -1:
					left_child_right_child = left_child.getRight()
					self.leftRotation(left_child_right_child, left_child)
					self.rightRotation(left_child_right_child, curr)
					self.updateSize(left_child)

					cnt += 2
				elif 0<=left_child_bfs <= 1:
					self.rightRotation(left_child, curr)
					cnt +=1
			self.updateHeight(curr)
			self.updateSize(curr)

			curr = curr.getParent()
		return cnt

	def getMaxNode(self):
		def maxNodeRec(node):
			curr = node
			while curr.getRight().isRealNode():
				curr = curr.getRight()
			return curr
		return maxNodeRec(self.root)
	def getMinNode(self):
		def mindNodeRec(node):
			curr = node
			while curr.getLeft().isRealNode():
				curr = curr.getLeft()
			return curr
		return mindNodeRec(self.root)

	def inorderPrint(self):
		def inorderPrintRec(node):
			if not node.isRealNode():
				return
			else:
				inorderPrintRec(node.getLeft())
				print('val: ' + node.getValue() + ' height: ' + str(node.getHeight()) + ' size: ' + str(node.getSize()) + ' left: ' + node.getLeft().getValue() + ' right: ' + node.getRight().getValue())
				inorderPrintRec(node.getRight())
		inorderPrintRec(self.root)
		print("tree size " + str(self.len))
# """ from here, all functions are for testing - REMOVE before submition"""

	def getTreeHeight(self):
		return self.root.getHeight()
	def append(self, val):
		return self.insert(self.length(), val)

	def printt(self):
		out = ""
		for row in self.printree(self.root):  # need printree.py file
			out = out + row + "\n"
		print(out)

	def printree(self, t, bykey=True):
		# for row in trepr(t, bykey):
		#        print(row)
		return self.trepr(t, False)

	def trepr(self, t, bykey=False):
		if t == None:
			return ["#"]

		thistr = str(t.key) if bykey else str(t.getValue())

		return self.conc(self.trepr(t.left, bykey), thistr, self.trepr(t.right, bykey))

	def conc(self, left, root, right):

		lwid = len(left[-1])
		rwid = len(right[-1])
		rootwid = len(root)

		result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

		ls = self.leftspace(left[0])
		rs = self.rightspace(right[0])
		result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid *
					  " " + "\\" + rs * "_" + (rwid - rs) * " ")

		for i in range(max(len(left), len(right))):
			row = ""
			if i < len(left):
				row += left[i]
			else:
				row += lwid * " "

			row += (rootwid + 2) * " "

			if i < len(right):
				row += right[i]
			else:
				row += rwid * " "

			result.append(row)

		return result

	def leftspace(self, row):
		# row is the first row of a left node
		# returns the index of where the second whitespace starts
		i = len(row) - 1
		while row[i] == " ":
			i -= 1
		return i + 1

	def rightspace(self, row):
		# row is the first row of a right node
		# returns the index of where the first whitespace ends
		i = 0
		while row[i] == " ":
			i += 1
		return i

