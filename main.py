import bot
from bot import  Monkey
from speed import  SPEED
from dino import DinoBot
from selection import Selection

if __name__=='__main__':
    game = Selection()
    game_selected = game.main_menu()
    print(game_selected)
    if game_selected == 'dino_bot':
        dino = DinoBot()
        dino.main()
    else:
        speed = SPEED()
        x=speed.mainfunc()
        monkey = Monkey(x)
        monkey.run_bot()

