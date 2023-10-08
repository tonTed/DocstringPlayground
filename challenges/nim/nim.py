import random

STICK_CHARACTER = '#'
STICK_HEIGHT = 3
STICK_START = 20
INPUT_COMPUTER = ""

# TODO create class display

class GameDisplay:
	@staticmethod
	def	stickDisplay(amount: int):
		[print(f"{(STICK_CHARACTER + ' ') * amount}") for _ in range(STICK_HEIGHT)]

	@staticmethod
	def __winDisplay(playerName: str):
		print(f"{playerName} win's!")
	
	def computerWinDisplay(self):
		self.__winDisplay("Computer")

	def playerWinDisplay(self):
		self.__winDisplay("Player")


class Game(GameDisplay):
	def __init__(self):
		self.sticks = STICK_START

	def turnComputer(self):
		randomSticks = random.randint(1, 3)
		#TODO manage amounts au sticks can't be less of 0
		print(f"computer takes {randomSticks} sticks.")
		self.sticks -= randomSticks

	#TODO implement
	def turnPlayer(self):
		self.turnComputer()

	def end(self, turnPlayer: bool):
		turnPlayer if self.playerWinDisplay() else self.computerWinDisplay()
	
	def start(self):
		turnPlayer: bool = False
		while (self.sticks > 0):
			self.stickDisplay(self.sticks)
			if (turnPlayer):
				self.turnPlayer()
			else:
				self.turnComputer()
			turnPlayer = not turnPlayer
		self.end(turnPlayer)
	

if __name__ == '__main__':
	game: Game = Game()
	game.start()
	