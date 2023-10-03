
STICK_CHARACTER = '#'
STICK_HEIGHT = 3

def	stickDisplay(amount :int):
    [print(f"{(STICK_CHARACTER + ' ') * amount}") for _ in range(STICK_HEIGHT)]
    

if __name__ == '__main__':
	stickDisplay(5)
    