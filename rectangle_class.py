class Rectangle:
	def __init__(self, height, width):
		self.__height = height
		self .__width = width

	def set_height(self, height):
		self.__height = height

	def get_height(self):
		return self.__height

	def set_width(self, width):
		self.__width = width

	def get_height(self):
		return self.__width

	def area(self):
		return self.__height * self.__width

rect1 = Rectangle(20, 60)

print(rect1.area())





