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
		return self.value != "VIRTUAL"


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
		self.VIRTUALNODE = AVLNode("VIRTUAL")
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
		def retrieve_rec(node,i):
			left_subtree_size = 0
			if node.getLeft().isRealNode():
				left_subtree_size = node.getLeft().getSize()
			if i==left_subtree_size:
				return node
			else:
				if i<node.getLeft().getSize():
					ind = i
					return retrieve_rec(node.getLeft(), ind)
				else:
					ind = i-node.getLeft().getSize()-1
					return retrieve_rec(node.getRight(),ind)

		if i > self.len:
			return None
		else:
			return retrieve_rec(self.root,i)


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
		if self.len == 0 and i==0:
			self.root = new_node
			self.len=1
		elif i == 0:
			tmp = self.root
			self.root = new_node
			new_node.setRight(tmp)
			tmp.setParent(new_node)
			self.len += 1

		elif self.len == i:
			parent = self.getMaxNode()
			parent.setRight(new_node)
			new_node.setParent(parent)
			self.len += 1
		else:
			node = self.retrieve(i)
			if not (node.getLeft().isRealNode()):
				# node.setRight(new_node)
				# new_node.setParent(node)
				node.setLeft(new_node)
				new_node.setParent(node)
			else:
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

		rotations_cnt = self.rebalance(low_node)
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
		if i >= self.length():
			return
		self.len -=1
		node = self.retrieve(i)
		parent = node.getParent()
		left = node.getLeft()
		right = node.getRight()
		rotations_cnt = 0
		if left.isRealNode() and right.isRealNode():
			pred = node.getPredecessor() 				#if node has right son, its predecessor is the max node in the left sub tree (no right sons)
			pred_left_child = pred.getLeft()
			pred_parent = pred.getParent()

			if pred_left_child.isRealNode():
				pred_left_child.setParent(pred_parent)
				pred_parent.setRight(pred_left_child)
			pred.setLeft(node.getLeft())
			pred.setRight(node.getRight())
			pred.setParent(node.getParent())
			rotations_cnt = self.rebalance(pred_parent)

			self.updateSize(pred_left_child)

		else:
			direction = node.childDirection()
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
				self.updateSize(node_child)

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

		return rotations_cnt

	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		if self.len == 0:
			return None
		else:
			node = self.retrieve(0)
			return node.value()



	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		if self.len == 0:
			return None
		else:
			idx= self.len - 1
			node = self.retrieve(idx)
			return node.value()
	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self): ##time complexity:
		if self.empty():
			return None
		else:
			listArr= ([(self.retrieve(i)).value() for i in range(self.length())]) #create an array and use retrieve to hold the values the list elements
			return listArr

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self): #time complexity O(1)
		if self.getRoot() == None:
			return 0
		rootNode= self.getRoot()
		sizeTree= rootNode.size()
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
		if len(lst)==0:
			return self
		T2 = AVLTreeList()
		if self.length()==0:
			for i in range(len(lst)):
				self.insert(i, lst[i])
				return self
		if len(lst) == self.length():
			T2Max=T2.getMaxNode()
			selfMax= self.getMaxNode()
			if T2Max>selfMax:
				joiningNode= T2Max
				T2.delete(joiningNode)
				joiningNode.setLeft(self.getRoot())
				joiningNode.setRight(T2.getRoot())
				return self
			else:
				joiningNode = selfMax
				self.delete(joiningNode)
				joiningNode.setRight(self.getRoot())
				joiningNode.setLeft(T2.getRoot())
				return self
		selfTreeHeight = self.getTreeHeight()
		for i in range(len(lst)):
			T2.insert(i, lst[i])
		T2TreeHeight= T2.getTreeHeight()
		if selfTreeHeight< T2TreeHeight:
			rightMostNode= self.getMaxNode()
			self.delete(rightMostNode)
			firstVertexOnLeftSpineT2 = AVLNode(lst[0])
			for i in range(len(lst)):
				firstVertexOnLeftSpineT2= AVLNode(lst[i])
				h=firstVertexOnLeftSpineT2.getHeight()
				if h== selfTreeHeight or h == selfTreeHeight -1:
					break
			rootSelf= self.getRoot()
			rootSelf= AVLNode(rootSelf)
			rootSelf.setLeft(rightMostNode.value())
			firstVertexOnLeftSpineT2.setRight(rightMostNode.value() )
			self.rebalance(rightMostNode)
		else: #selfTreeHeight>T2TreeHeight: ##the opposite is a symmetric problem
			rightMostNode = T2.getMaxNode()
			T2.delete(rightMostNode)
			firstVertexOnLeftSpineSelf = AVLNode(self.retrieve(0))
			for i in range(len(self.length())):
				firstVertexOnLeftSpineSelf = AVLNode(self.retrieve(i))
				h = firstVertexOnLeftSpineSelf.getHeight()
				if h == T2TreeHeight or h == T2TreeHeight-1:
					break
			rootT2 = T2.getRoot()
			firstVertexOnLeftSpineSelf.setRight(rightMostNode)
			rootT2.setLeft(rightMostNode)
			self.rebalance(rightMostNode)
		selfTreeHeightAfter = self.getTreeHeight()
		return abs(selfTreeHeight - selfTreeHeightAfter)

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val): #O(nlogn)
		for i in range (self.length()):
			if self.retrieve(i).value() == val:
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
		parent_node.getLeft().getParent().setParent(parent_node)

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
				if curr_direction == "LEFT":
					predecessor = node.getParent()
					break
				else:
					curr = curr.getParent()
		return predecessor


	""" 
	@rtype: AVLNode
	@returns: if index(node) = i, return the node in index i-1
	"""
	def getSucessor(self,node):
		sucessor = None
		curr = None
		if node.getRight().isRealNode():
			curr = node.getRight()
			while curr.getLeft().isRealNode:
				curr = curr.getLeft()
			sucessor = curr
		else:
			curr = node
			while curr.getParent() != None:
				curr_direction = curr.childDirection()
				if curr_direction == "RIGHT":
					sucessor = node.getParent()
					break
				else:
					curr = curr.getParent()
		return sucessor

	"""
	traverse the tree bottom-up, and update the height of each subtree, all the way to the root
	@rtype: AVLNode, the lowest one in the tree that we need to changes
	@returns: None
	"""
	def updateHeight(self, lowest_node):
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
# """ from here, all functions are for testing - REMOVE"""

# 	def getTreeHeight(self):
# 		return self.root.getHeight()
# 	def append(self, val):
# 		self.insert(self.length(), val)
#
# 	def printt(self):
# 		out = ""
# 		for row in self.printree(self.root):  # need printree.py file
# 			out = out + row + "\n"
# 		print(out)
#
# 	def printree(self, t, bykey=True):
# 		# for row in trepr(t, bykey):
# 		#        print(row)
# 		return self.trepr(t, False)
#
# 	def trepr(self, t, bykey=False):
# 		if t == None:
# 			return ["#"]
#
# 		thistr = str(t.key) if bykey else str(t.getValue())
#
# 		return self.conc(self.trepr(t.left, bykey), thistr, self.trepr(t.right, bykey))
#
# 	def conc(self, left, root, right):
#
# 		lwid = len(left[-1])
# 		rwid = len(right[-1])
# 		rootwid = len(root)
#
# 		result = [(lwid + 1) * " " + root + (rwid + 1) * " "]
#
# 		ls = self.leftspace(left[0])
# 		rs = self.rightspace(right[0])
# 		result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid *
# 					  " " + "\\" + rs * "_" + (rwid - rs) * " ")
#
# 		for i in range(max(len(left), len(right))):
# 			row = ""
# 			if i < len(left):
# 				row += left[i]
# 			else:
# 				row += lwid * " "
#
# 			row += (rootwid + 2) * " "
#
# 			if i < len(right):
# 				row += right[i]
# 			else:
# 				row += rwid * " "
#
# 			result.append(row)
#
# 		return result
#
# 	def leftspace(self, row):
# 		# row is the first row of a left node
# 		# returns the index of where the second whitespace starts
# 		i = len(row) - 1
# 		while row[i] == " ":
# 			i -= 1
# 		return i + 1
#
# 	def rightspace(self, row):
# 		# row is the first row of a right node
# 		# returns the index of where the first whitespace ends
# 		i = 0
# 		while row[i] == " ":
# 			i += 1
# 		return i
#
#
# def test():
# 	avl = AVLTreeList()
# 	avl.insert(0,'0')
# 	avl.insert(1, '1')
#
# 	avl.delete(0)
# 	avl.inorderPrint()

	# avl.insert(1,'2')

	#
	# avl.insert(0,'2')
	# avl.insert(1,'3')
	# avl.insert(0,'4')
#
# 	node = avl.retrieve(3).getValue()
# 	print(node)
# 	#
# 	# avl.insert(1,'1')
# 	# avl.insert(2,'2')
# 	# n = avl.retrieve(2)
# 	# avl.insert(2,'3')
# 	# avl.insert(0,'4')
# 	# avl.insert(1,'5')
# 	avl.inorderPrint()
# 	avl.delete(0)


	# avl.inorderPrint()
	#test()








