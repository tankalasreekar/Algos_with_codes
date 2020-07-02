# Recursive Algorithm

def getClosestValueInBst(bst, target):
	return getClosestValueInBstHelper(bst, target, float("inf"))

def getClosestValueInBstHelper(bst, target, closest):

	current = bst.value

	if current is None:
		return closest

	if abs(closest - target) > abs(target - current):
		closest = current

	if target > current :
		return getClosestValueInBstHelper(bst.right, target, closest)

	elif target < current:
		return getClosestValueInBstHelper(bst.left, target, closest)

	else:
		return closest


# Iterative Algorithm

def getClosestValueInBstIterative(bst, target):
	return getClosestValueInBstIterativeHelper(bst, target, float("inf"))

def getClosestValueInBstIterativeHelper(bst, target, closest):

	current = bst

	while current is not None:

		if abs(closest - target) > abs(target - current):
			closest = current.value

		if target > current.value :
			current = current.right

		elif target < current.value:
			current = current.left

		else:
			break

	return closest