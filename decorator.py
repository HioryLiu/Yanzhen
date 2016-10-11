# decorator will be ran when function defined?
def showtimes(func):
	print "this is showtimes"
	return func

@showtimes
def do_something():
	print 'did something'

def showNames(name):
	print 'define decorator'
	def _func(func):
		print "this is " ,name
		return func
	return _func
@showNames('liudong')
def do_names():
	print "inside do_names"

def replace_name(name):
	def _dec(func):
		print "doing func" ,name
		def _wrapper(*args ,**kwargs):
			print "inside wrapper", args ,kwargs, name
			return func(*args, **kwargs)
		return _wrapper #return a func that used
	return _dec #return a func whoes args is decorated function

@replace_name("liudong")
def showname(*args, **kwargs):
	print "inside showname", args, kwargs
	return "Domsia"

showname(12,23)
print '''------------------------
#### decorator class ###
------------------------'''

class dec_class(object):
	"""docstring for dec_class"""
	def __init__(self, arg):
		super(dec_class, self).__init__()
		print "in dec_class init"
		self.arg = arg
	def __call__(self,func):
		print "in dec_class call ", self.arg
		return func
dec_instance = dec_class("foo")

@dec_instance
def do_class():
	print "this is do_class"

do_class()