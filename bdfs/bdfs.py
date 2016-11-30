# -*-coding:utf-8 -*-

# 先序遍历 时间复杂度为O(n),空间复杂度为 树的深度(log(n)~n)
def preOrder(node, otherParams):
	if cornerCase: #处理边界条件
		dealWithCornerCase()
	dealWith(node, otherParams)# 处理本节点
	preOrder(node.leftChild, otherParamsLeft)
	preOrder(node.rightChild, otherParamsRight)
	mergeRusult() #可选

#中序遍历 
def inOrder(node, otherParams):
	if cornerCase:
		dealWithCornerCase()
	inOrder(node.leftChild, otherParamsLeft)
	dealWith(node, otherParams)
	inOrder(node.rightChild, otherParamsRight)
	mergeRusult()

# 后序遍历
def postOrder(node, otherParams):
	if cornerCase:
		dealWithCornerCase()
	postOrder(node.rightChild, otherParamsRight)
	postOrder(node.leftChild, otherParamsLeft)
	dealWith(node, otherParams)
	mergeRusult()

# 层序遍历 时间复杂度为O(n) 空间复杂度也为O(n)
def levelOrder(root, otherParams):
	Queue queue
	add(queue, root)
	while !isEmpty(queue):
		TreeNode node = remove(queue)
		dealWith(node, otherParams)
		if !cornerCase(node.leftChild):
			add(node.leftChild)
		sameToRightChild()
		mergeRusult()