class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def getBranchSums(root):
	sums = []
	calculateBranchSums(root, 0, sums)
	return sums

def calculateBranchSums(node, runningSum, sums):

	if node is None:
		return

	currentRunningSum = runningSum + node.value
	if node.left is None and node.right is None:
		sums.append(currentRunningSum)
		return

	calculateBranchSums(node.left, currentRunningSum, sums)
	calculateBranchSums(node.right, currentRunningSum, sums)