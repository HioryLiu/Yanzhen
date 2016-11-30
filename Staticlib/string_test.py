
print '{2}, {1}, {0}'.format(*'abc')

print 'Coordinates: {latitude}'.format(latitude="1200")

coord = {'latitude':'37.2N','longitude':'-115.81W'}
print 'Coordinates: {latitude},{longitude}'.format(**coord)

class Point(object):
	def __init__(self, x, y):
		self.x, self.y = x, y
	def __str__(self):
		return 'Point({self.x}, {self.y})'.format(self=self)

print str(Point(2, 4))

coord2 = (23, 30)
print "X:{0[0]},Y:{0[1]}".format(coord2)

print "{:.^30}".format("this is liudong")
print "{:>30}".format("this is filled")

print "{0:x}:{0:b}".format(234)

print "{:,}".format(12345678)

print "{:.4%}".format(1004/345)

for num in range(5, 12):
	for base in 'dXob':
		print '{0:{width}{base}}'.format(num, base=base,width=5)
