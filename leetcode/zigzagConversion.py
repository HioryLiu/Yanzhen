
# class Solution:
# 	def convert(self, s, numRows):
# 		if numRows%2 ==0:
# 			rws = ["" for i in range(0, numRows+1)]
# 			for i, ch in enumerate(s):
# 				sm = (i+1)%(numRows+1)
# 				if sm == (numRows/2)+1 or sm ==0:
# 					rws[(numRows/2)+1] +=ch
# 				else:
# 					rws[sm] += ch
# 		else:
# 			rws = ["" for i in range(0,numRows+1)]
# 			for i, ch in enumerate(s):
# 				sm = (i+1)%(numRows+1)
# 				if sm == (numRows+1)/2 or sm == 0:
# 					rws[(numRows+1)/2] += ch
# 				else:
# 					rws[sm] +=ch
# 		return "".join(rws)

class Solution(object):
	"""docstring for solution"""
	def convert(self, s, numRows):
		rws = ["" for i in range(0, numRows)]
		if numRows == 1:
			return s
		md = (numRows * 2) -2
		for i,ch in enumerate(s):
			sm = i%md
			if sm < numRows:
				rws[sm] += ch
			else:
				rws[md-sm] += ch
		return "".join(rws)




solution = Solution()
print solution.convert("PAYPALISHIRING", 3)
print solution.convert("",1)
print solution.convert("ABCDEFGHIGKLMN", 4)
print solution.convert("ABCDE", 4)