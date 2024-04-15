class Triangulo:
	def __init__(self, base, altura1, altura2, a, p):
		self.base = base
		self.altura1 = altura1
		self.altura2 = altura2
		self.a = a
		self.p = p
	def area(self):
		return f"a sua área é de: {self.a}"
	def perimetro(self):
		return f"seu perímetro é de: {self.p}"

if __name__ == "__main__":
	triangulo1 = Triangulo("10", "5", "5", "25", "20")

	print(triangulo1.area())
	print(triangulo1.perimetro())