# str.title()

import re
def  titlecase(s):
	return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
		lambda mo: mo.group(0)[0].upper() +
					mo.group(0)[1:].lower(),
					s)

print titlecase("this is liudong's time")

print 'read this short text'.translate(None, 'aeiou')