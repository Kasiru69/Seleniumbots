import bot
from bot import  Monkey
from speed import  SPEED

if __name__=='__main__':
    speed = SPEED()
    x=speed.mainfunc()
    monkey = Monkey(x)
    monkey.run_bot()
