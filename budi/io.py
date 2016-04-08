print "-- Program Biodata Murid --"
name 	= raw_input("masukan nama 		: ")
address = raw_input("masukan alamat 		: ")
phone 	= raw_input("masukan no telepon 	: ")

text = "{}|{}|{}\n".format(name, address, phone)

f = open('biodata.txt', 'a')
f.write(text)
f.close()

print "-- Hasil Baca File --"
with open('biodata.txt', 'r') as f:
	for line in f.readlines():
		print line