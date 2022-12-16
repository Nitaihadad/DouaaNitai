#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - complete info
#name2    - complete info  



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





"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):


	"""
	Constructor, you are allowed to add more fields.

	"""
	def __init__(self):
		self.size = 0
		self.root = None
		self.VIRTUALNODE = AVLNode("VIRTUAL")
		self.VIRTUALNODE.setSize(0)



	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return self.size == 0


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

		if i > self.size:
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
		if self.size == 0 and i==0:
			self.root = new_node
			self.size=1
		elif i == 0:
			tmp = self.root
			self.root = new_node
			new_node.setRight(tmp)
			tmp.setParent(new_node)
			self.size += 1

		elif self.size == i:
			parent = self.getMaxNode()
			parent.setRight(new_node)
			new_node.setParent(parent)
			self.size += 1
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
					self.size += 1
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
				node_child = left
			elif right.isRealNode():
				node_child = right


			if node_is_left_child:
				parent.setLeft(node_child)
			else:
				parent.setRight(node_child)
			parent.setSize(parent.getSize()-1)
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
		return None

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return None

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		return None

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return None

	"""sort the info values of the list

	@rtype: list
	@returns: an AVLTreeList where the values are sorted by the info of the original list.
	"""
	def sort(self):
		return None

	"""permute the info values of the list 

	@rtype: list
	@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
	"""
	def permutation(self):
		return None

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		return None

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		return None



	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return None


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

	def inorderPrint(self):
		def inorderPrintRec(node):
			if not node.isRealNode():
				return
			else:
				inorderPrintRec(node.getLeft())
				print('val: ' + node.getValue() + ' height: ' + str(node.getHeight()) + ' size: ' + str(node.getSize()) + ' left: ' + node.getLeft().getValue() + ' right: ' + node.getRight().getValue())
				inorderPrintRec(node.getRight())
		inorderPrintRec(self.root)
		print("tree size " + str(self.size))


def test():
	avl = AVLTreeList()
	avl.insert(0,'0')
	avl.insert(1,'1')
	avl.insert(0,'2')
	avl.insert(1,'3')
	avl.insert(0,'4')

	node = avl.retrieve(3).getValue()
	print(node)
	#
	# avl.insert(1,'1')
	# avl.insert(2,'2')
	# n = avl.retrieve(2)
	# avl.insert(2,'3')
	# avl.insert(0,'4')
	# avl.insert(1,'5')
	avl.inorderPrint()
	# avl.delete(0)


	# avl.inorderPrint()

test()








