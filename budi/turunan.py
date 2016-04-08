class People(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Student(People):
	def __init__(self, name, age, nilai):
		People.__init__(self, name, age)
		self.nilai = nilai

class Teacher(People):
	def __init__(self, name, age, gaji):
		People.__init__(self, name, age)
		self.gaji = gaji

rizky = Student("Rizky", 17, 100)
vai = Student("Vai", 18, 90)
budi = Student("Budi", 16, 95)

list_Student = [rizky, vai, budi]
for Student in list_Student:
	print "-- Data {} --".format(Student.name)
	print "Name 	: {}".format(rizky.name)
	print "age 		: {}".format(rizky.age)
	print "nilai 	: {}".format(rizky.nilai)
	print "-----------------------"	