from  heapq import *

def heapsort(iterable):
	h = []
	for value in iterable:
		heappush(h, value)
	return [heappop(h) for i in range(len(h))]

print heapsort([2,4,6,8,4,1,0,9,7,3])
# [0, 1, 2, 3, 4, 4, 6, 7, 8, 9]

pq = []
entry_finder = {}
REMOVED = '<removed-task>'
counter = itertools.count()

def add_task(task, priority=0):
	'Add a new task or update the priority of an existing task'
	if task in entry_finder:
		remove_task(task)
	count = next(counter)
	entry = [priority, count, task]
	heappush(pq, entry)

def remove_task(task):
	'Mark an existing task as REMOVED. Raise KeyError if not found.'
	entry = entry_finder.pop(task)
	entry[-1] = REMOVED

def pop_task():
	'Remove and return the lowest priority task. Raise KeyError if Empty'
	while pq:
		priority, count, task = heappop(qp)
		if task is not REMOVED:
			del entry_finder[task]
			return task
	raise KeyError('pop from an empty priority queue')  