# this is a bubble sort function 	
def bubble(list):
	length = len(list)
	while  length>0:
		for i in range(length - 1):
			if list[i]>list[i+1]:
				n = list[i+1]
				list[i+1] = list[i]
				list[i] = n
		length -= 1
	print list

if __name__ == '__main__':
	bubble_list = [3,5,6,2,4,6,8,9]
	bubble(bubble_list)