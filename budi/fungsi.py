'''
simple method untuk mencetak nilai, method tidak pernah kembalikan nilai
'''
def cetak_hello_world():
	print "hello world"

def cetak_nilai(nama, nilai):
	print "nilai dari {} adalah: {}".format(nama, nilai)

'''
fungsi selalu mengembalikna suatu nilai, ditandai dengan statement `return`
'''
def get_grade(nilai):
	value = int(nilai)
	if (value >90 <=100):
		return "A"
	elif (value >70 <=90):
		return "B"
	elif (value >50 <=70):
		return "C"
	else :
		return "D"


cetak_hello_world()
cetak_nilai("Agust Budiyanto", 100)
print get_grade(90)