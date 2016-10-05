## this is a cocktail sort function 
def cocktail_sort(list):
	size = len(list)
	sign = 1
	for i in range(size/2):
		if sign:
			sign = 0
			for j in range(i, size-1-i):
				if list[j] > list[j+1]:
					# print str(j)+' --> '+ str(j+1)
					list[j],list[j+1] = list[j+1],list[j]
			for k in range(size-2-i,i,-1):
				if list[k] < list[k-1]:	
					# print str(k)+" -> "+ str(k-1)
					list[k],list[k-1] = list[k-1],list[k]	
					sign = 1;
		else:
			break
	print list


if __name__ == '__main__':
	cocktail_list = [5,3,6,2,9,4]
	print cocktail_list
	cocktail_sort(cocktail_list);

'''[5, 3, 6, 2, 9, 4]
0 --> 1
2 --> 3
4 --> 5
4 -> 3
2 -> 1
1 -> 0
2 --> 3
[2, 3, 4, 5, 6, 9]'''

				
