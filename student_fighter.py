class StudentFighter(object):
	def __init__(self, strength, health,name):
		self.strength = strength
		self.name = name
		self.health = health
	def attack(self, opponent):
		opponent.health -= self.strength
		message = "{} has {} health points remaining".format(opponent.name, opponent.health)		
	print(messsege)
kalu = StudentFighter(strength=3, health=100, name="Kalu")
David = StudentFighter(strength=5, health=100, name="David")
kalu.attack(David)