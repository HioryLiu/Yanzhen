# dong tai gui hua
# -*- coding: utf-8 -*-

# 动态规划问题，关键在于找到状态转移方程
# 求解编码方式的数量

def decod_num(string):
	ls = [1 for x in range(len(string))]
	if len(string)<2:
		return 1
	if string[0]=='1' or string[0]=='2' and string[1] <='6':
		ls[1] = 2
	for i in range(2, len(string)):
		if string[i] >= '0' and string[i] <='9':
			ls[i] = ls[i-1]
		else:
			return 0
		tmp = int(string[i-1])
		tmp = tmp*10 + int(string[i])
		if string[i-1] != '0' and tmp <= 26:
			ls[i] += ls[i-2]
	return ls[len(string)-1]

print decod_num('123234656563121')


# 从左上角到右下角，寻找代价最小的路径
# 典型的动态规划问题

def minPath(vec):




# 最大子数组的乘积
# 最大字串乘积，由于可能出现负数，也是DP问题，也是局部最优和全局最优问题。
# 这里需要记录最小值，假设两个数组，分别记录包括当前元素在内的字串所能构成的最大和最小值，然后根据这个在更新全局
# 最大，至于当前最大，可能是之前最大乘以当前元素，也可能是前一个元素最小乘以当前元素，也可能是当前元素

def maxProduct(vec):
	'''核心代码'''
	for i in range(len(vec)):
		maxcur[i] = max(vec[i], max(maxcur[i-1]*vec[i], mincur[i-1]*vec[i]))
		mincur[i] = min(vec[i], min(mincur[i-1]*vec[i], maxcur[i-1]*vec[i]))

		maxproduct = max(maxcur[i], maxproduct)
	return maxproduct


