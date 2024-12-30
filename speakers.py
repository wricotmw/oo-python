
# This demonstates the creation of classes, instances, encapsulation using underscore
# and inheriatance
# Ref FreeCose Camp https://www.freecodecamp.org/news/how-to-use-oop-in-python/

class Speaker:
	brand = "Beatpill" # class attribute

	def __init__(self, colour, model):
		self._colour = colour  # no _ is instance attribute
		self._model = model		# _ makes the attribute Private

	def power_on(self):  # instance methods
		print(f"Powering on {self._colour} {self._model} speaker.")

	def power_off(self):
		print(f"Powering off {self._colour} {self._model} speaker.")

	def get_colour(self):
		return self._colour

	def set_colour(self, new_colour):
		self._colour = new_colour

speaker_one = Speaker("black", "85XB5")
speaker_two = Speaker("red", "Y8F33")


 
speaker_one.power_on()   #calls instance method in class
speaker_two.power_off()

# Accessing a private attribute directly (not recommended)
print(f"speaker_one is {speaker_one.brand} in {speaker_one._colour} and speaker_two is {speaker_two.brand} in {speaker_two._colour} ")
print(speaker_one._colour)

# Accessing a private attribute using the getter method (recommended)
print(speaker_one.get_colour())

# Modifying a private attribute using the setter method (recommended)
speaker_one.set_colour("white")
print(speaker_one.get_colour())

#Inheritance

# Add a SmartSpeaker class and make it inherit from the Speaker class

class SmartSpeaker(Speaker):
	def __init__(self, colour, model, voice_assistant):
		super().__init__(colour, model) # calls init method of Speaker Class
		self._voice_assistant = voice_assistant # Attiribute of SmartSpeaker Class

	def say_hello(self):
		print(f"Hello, I am {self._voice_assistant}")

# Create an instance of the SmartSpeaker class
smart_speaker = SmartSpeaker("black", "XYZ123", "Alexa")
smart_speaker.power_on()  # Inherited from Speaker
smart_speaker.say_hello()