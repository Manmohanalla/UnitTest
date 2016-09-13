
class Add:
	def add(self,a,b):
		if type(a) == int:
			return a+b
		else:
			c= a+' ' +b
			return c
result = Add()
result.add('hello','world')
result.add(4,3)