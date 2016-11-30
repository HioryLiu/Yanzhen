# fen tang guo

# def candy(rating):
# 	candy = [1 for x in range(len(rating))]
# 	for i in range(1, len(rating)):
# 		if rating[i] > rating[i-1]:
# 			candy[i] = candy[i-1]+1
# 	sum = candy[-1]
# 	print str(candy)
# 	for j in range(len(rating)-2, -1, -1):
# 		print j
# 		cur = 1
# 		if rating[j] > rating[j+1]:
# 			cur = candy[j+1]+1
# 		sum += max(cur, candy[j])
# 		candy[j] = cur
# 	print str(candy)
# 	return sum
# print candy([3, 2, 4, 1, 2])

def candy(rating):
	_len = len(rating)
	candy = [ 1 for x in range(_len)]
	for i in range(1, _len):
		if rating[i] > rating[i-1]:
			candy[i] = candy[i-1]+1
	sum = candy[_len-1]
	for j in range(_len-2, -1, -1):
		cur = 1
		if rating[j] > rating[j+1] and candy[j] <= candy[j+1]:
			candy[j] = candy[j+1]+1
		sum += candy[j]
	print candy
	return sum

print candy([3, 2, 4, 1, 2])

def canJump(vec):
	if len(vec) <=0:
		return True
	maxstep = vec[0]
	for i in range(1, len(vec)):
		if maxstep == 0:
			return False
		maxstep -= 1
		if maxstep <vec[i]:
			maxstep = vec[i]
		if maxstep+i >= len(vec)-1:
			return True

print canJump([1,0,2])
