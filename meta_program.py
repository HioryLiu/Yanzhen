#########################
# this is a class factory
def class_with_method(func):
	class klass():pass
	# return a class that related to klass
	setattr(klass,func.__name__, func)
	klass.number = 10
	return klass

def say_hello(self):
	print 'foo'

# change the say_hello to wanted, Foo is a class
Foo = class_with_method(say_hello)
# it can make a instance
foo = Foo()
foo.say_hello()
print foo.number

#######################
## inherit type 
class ChattyType(type):
	def __new__(cls, name, bases, dct):
		print 'memory for class ', name
		return type.__new__(cls, name, bases, dct)
	def __init__(cls, name, bases, dct):
		print 'Init class ', name
		super(ChattyType, cls).__init__(name, bases, dct)

X = ChattyType('X', (), {'foo': lambda self: 'foo'})

print X

print '''

###################################
## here are some example of type ##
'''
class Foo(object):
	bar = 'liudong'
		
def echo_bar(self):
		print self.bar

FooChild = type('FooChild', (Foo, ), {'echo_bar':echo_bar})

print hasattr(Foo, 'echo_bar')
print hasattr(FooChild, 'echo_bar')

my_foo = FooChild()
my_foo.echo_bar()

print '''

#########################################
## a metaclass. uppercase all property ##
'''
def  upper_attr(class_name, class_parent, class_attr):
	attrs = ((name, value) for name, value in class_attr.items() if not name.startswith('__'))
	uppercase_attr = dict((name.upper(), value) for name, value in attrs)
	return type(class_name, class_parent, uppercase_attr)


class CaseFoo(object):
	__metaclass__ = upper_attr
	bar = 'tip'
print hasattr(CaseFoo, 'bar')
print hasattr(CaseFoo, 'BAR')

f= CaseFoo()
print f.BAR;

print '''

#########################################
## inherit type. uppercase all property ##
'''
class UpperAttrMetaClass(type):
	def __init__(self, arg):
		print 'init UpperAttrMetaClass'
		super(UpperAttrMetaClass, self).__init__()
		self.arg = arg
	def __new__(upperattr_metacls, future_cls_name, future_cls_parents, future_cls_attr):
		print 'new UpperAttrMetaClass'
		attrs = ((name, value) for name, value in future_cls_attr.items() if not name.startswith('__'))
		## dict(): change a generator to dictionary
		uppercase_attr = dict((name.upper(), value) for name, value in attrs)
		return type(future_cls_name, future_cls_parents, uppercase_attr)
class GoodFoo(object):
	# __metaclass__ = 
	bar = 'tip'

Y = UpperAttrMetaClass('Y', (GoodFoo, ), {'bar':'liudong','name':23})

print hasattr(Y, "BAR")
# print hasattr(GoodFoo, 'BAR')
			