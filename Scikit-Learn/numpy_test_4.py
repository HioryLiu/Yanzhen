# 1. Correlation Coefficient & Correlation Distance
# 2. Mahalanobis Distance

from numpy import *

featuremat = mat([
	[1,2,3,4,5,6,7,8,9],[10,20,30,40,50,60,70,80,90]])
# 1.
mv1 = mean(featuremat[0])
mv2 = mean(featuremat[1])

dv1 = std(featuremat[0])
dv2 = std(featuremat[1])

corref = mean(multiply(featuremat[0]-mv1,featuremat[1]-mv2))/(dv1*dv2)
print corref
print corrcoef(featuremat)

# 2.
covinv = linalg.inv(cov(featuremat))
tp = featuremat.T[0]-featuremat.T[1]
distma = sqrt(dot(tp, covinv), tp.T)

print distma