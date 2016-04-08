def keyword_argument(a, b, c=20):
	print "a:  " +str(a)
	print "b:  " +str(b)
	print "c:  " +str(c)

keyword_argument(b=2, a=1, c=3)

def function_args(*datas, **keywords):
	print datas
	print keywords
	for d in datas:
		print d
	print keywords["buah"]
	print keywords["harga"]
	print '-------------------------'
	for k in keywords:
		print keywords [k]

function_args(1,2,3,4,5, buah="mangga", harga="20000")