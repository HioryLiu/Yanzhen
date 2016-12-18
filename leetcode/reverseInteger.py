
class Solution(object):
	def reverse(self, x):
		if x>=0:
			result = int(str(x)[::-1])
			if result > 2147483648:
				return 0
			else:return result
				
		else:
			result = int("-"+str(abs(x))[::-1])
			if result < -2147483648:
				return 0
			else: return result


s = Solution()
print s.reverse(-123)
print s.reverse(123)