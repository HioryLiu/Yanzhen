# creditx windows 
# -*- conding: utf-8 -*-

from numpy import *

A = [[8,1,6],[3,5,7],[4,9,2]]
evals, evecs = linalg.eig(A)

print 'evals:',evals,'evecs:',evecs


vmat = mat([[1,2,3],[4,5,6]])
v12 = vmat[0]-vmat[1]
print sqrt(v12*v12.T)
varmat = std(vmat.T,axis=0)
normvmat = (vmat-mean(vmat))/varmat.T
normv12 = normvmat[0]-normvmat[1]
print sqrt(normv12*normv12.T)