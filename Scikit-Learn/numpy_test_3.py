from numpy import *
import scipy.spatial.distance as dist

m1 = mat([1,2,3])
m2 = mat([4,7,5])
m3 = mat([[1,1,0,1,0,1,0,0,1],[0,1,1,0,0,0,1,1,1]])

# Euclidean Distance
Eudis = sqrt((m1-m2)*((m1-m2).T))
print Eudis

# Manhattan Distance
Madis = sum(abs(m1-m2))
print Madis

# Chebyshev Distance
Chdis = abs((m1-m2)).max()
print Chdis

# Cosine
# dot(m1, m2)error?
Cosm12 = sum(multiply(m1, m2))/(linalg.norm(m1)*linalg.norm(m2))
print Cosm12

# Hanmming Distance
smstr = nonzero(m3[0]-m3[1])
Hadis = shape(smstr)[1]
print Hadis

# Jaccard Distance & Jaccard Cimilarity Coefficient
Jadis = dist.pdist(m3, 'jaccard')
print Jadis
