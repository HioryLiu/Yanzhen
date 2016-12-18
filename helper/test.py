from ListNode import ChainTable, Node

n2 = Node(12)
n1 = Node(10, n2)
l1 = ChainTable()
l1.append(n1)


print l1
