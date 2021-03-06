import random

from game.actor import Actor
from game.gems import Gem
from game.stones import Stone
from game.cast import Cast

from game.Director import Director

from game.keyboard_service import KeyboardService
from game.video_service import VideoService

from game.color import Color
from game.point import Point

# def grow_number(number):
#       number = 10
 #      i = 0
  #      while(i < number):
   #         number = number + 1
    #    i = i + 1
     #   return number */ 
#The Basic Variables for the program.
FRAME_RATE = 80
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
GREEN = Color(0,255,0)
RED = Color(255,0,0)
GEM_COUNT = 35
STONE_COUNT = 30


def main():
    
    # create the cast
    cast = Cast()
    
    # create the points
    points = Actor()
    points.set_text("")
    points.set_font_size(FONT_SIZE)
    points.set_color(WHITE)
    points.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("points", points)
    
    # create the robot
    x = int(MAX_X / 2)
    y = 570
    position = Point(x, y)

    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("player", player)

    #Create the Gems
    for n in range(GEM_COUNT):

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        gems = Gem()
        gems.set_text('*')
        gems.set_font_size(FONT_SIZE)
        gems.set_color(GREEN)
        gems.set_position(position)
        cast.add_actor("gems", gems)
    #Create the Stones
    for n in range(STONE_COUNT):

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        stones = Stone()
        stones.set_text('D')
        stones.set_font_size(FONT_SIZE)
        stones.set_color(RED)
        stones.set_position(position)
        cast.add_actor("stones", stones)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

#Call main()
if __name__ == "__main__":
    main()