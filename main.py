from display import *
from draw import *
from random import *

screen = new_screen()
color = [ 0, 255, 0 ]

x = 0
while x < randint(200, 300):
    i = randint(0, 500)
    i1 = randint(0, 500)
    j = randint(0, 500)
    j1 = randint(0, 500)
    color[randrange(3)] = randrange(256)
    draw_line( i, j, i1, j1, screen, color)
    x += 1

display(screen)
save_extension(screen, 'img.png')
