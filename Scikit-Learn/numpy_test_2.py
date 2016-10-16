from numpy import *

mylist = [1,2,3,4]

a =10
mymatrix = mat(mylist)

print a * mymatrix

myRand = random.rand(3,4)*10
print myRand

myOnes =ones([3, 3])
myEye = eye(3)
print myOnes + myEye

mymatrix1 = mat([[1,2,3,],[4,5,6,],[7,8,9]])
mymatrix2 = mat([[1],[2],[3]])

print mymatrix1 * mymatrix2
[m,n] = shape(mymatrix1)

print mymatrix1.T[0]

A = [8, 1, 6]
modA = sqrt(sum(power(A, 2)))
normA = linalg.norm(A)
print modA , normA