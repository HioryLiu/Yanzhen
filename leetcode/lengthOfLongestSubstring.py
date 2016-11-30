
def lengthOfLongestSubstring(s):
	res=0 
	left = 0
	d = {}
	for i, ch in enumerate(s):
		if ch in d and d[ch] >= left:
			left = d[ch] + 1
		d[ch] = i
		if res < i- left+1:
			subStr = s[left:i+1]
		res = max(res, i - left + 1)
		print subStr
	return res


s = "abcabcbb"
print lengthOfLongestSubstring(s)

	