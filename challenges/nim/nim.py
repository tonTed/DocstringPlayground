
STICK_CHARACTER = '#'
STICK_HEIGHT = 3
STICK_START = 20
INPUT_COMPUTER = ""

def	stickDisplay(amount :int):
	[print(f"{(STICK_CHARACTER + ' ') * amount}") for _ in range(STICK_HEIGHT)]
	
class Game:
	def __init__(self):
		self.sticks = STICK_START

	def turnComputer(self):
		pass

	def turnPlayer(self):
		pass
	
	def start(self):
		turnPlayer :bool = False
		while (self.sticks > 0):
			if (turnPlayer):
				self.turnPlayer()
			else:
				self.turnComputer()
			turnPlayer = not turnPlayer
	

if __name__ == '__main__':
	stickDisplay(5)
	