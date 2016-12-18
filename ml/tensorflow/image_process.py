from PIL import Image
import struct

def read_image(filename):
	f = open(filename, "rb")

	index = 0
	buf = f.read()
	f.close()

	magic, images, rows, columns = struct.unpack_from('>IIII', buf, index)
	index += struct.calcsize('>IIII')

	for i in xrange(images):

		image = Image.new('L', (columns, rows))

		for x in xrange(rows):
			for y in xrange(columns):
				image.putpixel((y, x), int(struct.unpack_from('>B', buf, index)[0]))
				index += struct.calcsize('>B')

		print 'save ' + str(i) + ' image'
		image.save('/home/liudong/free/mnitest/'+ str(i)+'.png')

def read_label(filename, saveFilename):
	f = open(filename, 'rb')
	index = 0
	buf = f.read()
	f.close()

	magic, labels = struct.unpack_from('>II', buf, index)
	index += struct.calcsize('>II')

	labelArr = [0]* labels
	for x in xrange(labels):
		labelArr[x] = int(struct.unpack_from('>B', buf, index)[0])
		index += struct.calcsize('>B')
		print x

	save = open(saveFilename, 'w')
	save.write(','.join(map(lambda x: str(x), labelArr)))
		# print ','.join(map(lambda x: str(x), labelArr))
	
	save.write('\n')
	save.close()
	print 'save labels success'


if __name__ == '__main__':
	# read_image('/home/liudong/Downloads/train-images.idx3-ubyte')
	read_label('/home/liudong/Downloads/train-labels.idx1-ubyte', '/home/liudong/free/mnistdata/train-label.txt')