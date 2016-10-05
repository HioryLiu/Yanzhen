## this is a bucket sort function
def bucket_sort(list,n):
	size = len(list)
	buckets =[[] for x in range(n)]
	for s in list:
		buckets[s].append(s);# also can be a function to create buckets
	so = []
	for bk in buckets:
		if len(bk) > 0:
			so.extend(bk)
	print so

if __name__ == '__main__':
	list = [2,3,4,5,2,2]
	bucket_sort(list,6)