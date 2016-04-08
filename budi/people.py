class people(object):
	def say_hello(self, name):
		print "hello {}".format(name)

# meng - inisiasi object dari class people
budi = people()
# memanggil method say_hello
budi.say_hello("Budi")

class people2(object):
	def __init__(self, name, address, kelas):
		self.name = name
		self.address = address
		self.kelas = kelas

	def get_name(self):
		return self.name

	def get_address(self):
		return self.address

	def get_kelas(self):
		return self.kelas

	def print_info(self):
		print "name 	: {}".format(self, name)
		print "address 	: {}".format(self, address)
		print "kelas 	: {}".format(self, kelas)

	def __str__(self):
		return "<{}>".format(self.name)

print "---------"
budi = people2("Agust Budiyanto", "Kediri - Dandangan", "XI RPL")
print budi.get_name()
print budi.get_address()
print budi.get_kelas()