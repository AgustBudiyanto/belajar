name = raw_input("masukan nama	: ")
nilai_str = raw_input("masukan nilai 	: ")

try:
	var_nilai = int(nilai_str)
	print "nilai dari {} adalah {}".format(name, var_nilai)
except ValueError, e:
	print "[ERROR] Nilai Harus Angka!"
else:
	print "Tidak Error"
finally:
	print "Proses Selesai !"
	