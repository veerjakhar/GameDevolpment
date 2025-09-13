import pygame

pygame.init()

#globsl varables
screen = pygame.display.set_mode([500, 500])
red = (255, 0 ,0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

screen.fill(white)

class My_circle():
    def __init__(self, color, pos, rad, wid = 0):
        self.color = color
        self.pos = pos
        self.rad = rad
        self.wid = wid
        self.scrn = screen

    def draw(self):
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid)

    def grow(self, x):
        self.rad += x
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid)

#how to draw a circle

position = (250, 250)
radius = 50
wid = 2
pygame.draw.circle(screen, blue, position, radius, wid)
pygame.display.update()

#creating instances

blueCircle = My_circle(blue, position, radius + 60)
redCircle = My_circle(red, position, radius + 40)
yellowCircle = My_circle(yellow, position, radius, 5)
greenCircle = My_circle(green, position, 20)

while(1):
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            blueCircle.draw()
            redCircle.draw()
            yellowCircle.draw()
            greenCircle.draw()
            pygame.display.update()
        elif (event.type == pygame.MOUSEBUTTONUP):
            blueCircle.grow(2)
            redCircle.grow(2)
            yellowCircle.grow(2)
            greenCircle.grow(2)
            pygame.display.update()
        elif (event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            blackCircle = My_circle(black, pos, 5)
            blackCircle.draw()
            pygame.display.update()
            

