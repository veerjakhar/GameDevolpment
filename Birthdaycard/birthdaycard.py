import pygame
import time

pygame.init()

WIDTH = 900
HEIGHT = 600

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
img = pygame.image.load("backgroundimg.jpg")
image = pygame.transform.scale(img, (WIDTH, HEIGHT))

img2 = pygame.image.load("backgroundimg2.jpg")
image2 = pygame.transform.scale(img2, (WIDTH, HEIGHT))

font = pygame.font.SysFont("Times New Roman", 72)
font2 = pygame.font.SysFont("Times New Roman", 42)

#available_fonts = pygame.font.get_fonts()
#for font in available_fonts:
    #print(font)

while (True):
    display_surface.fill((255, 255, 255))
    display_surface.blit(image, (0, 0))

    text = font.render("Happy Birthday", True, (0, 0, 0))
    display_surface.blit(text, (210, 190))
    pygame.display.update()
    time.sleep(4)

    display_surface.fill((255, 255, 255))
    display_surface.blit(image2, (0, 0))
    text2 = font2.render("Being happy doesn't mean", True, (0, 0, 0))
    display_surface.blit(text2, (210, 190))
    text4 = font2.render("that everything is perfect.", True, (0, 0, 0))
    display_surface.blit(text4, (210, 250))
    text3 = font2.render("   It means that you've decided", True, (0, 0, 0))
    display_surface.blit(text3, (210, 310))
    text5 = font2.render("   to look beyond the imperfections ", True, (0, 0, 0))
    display_surface.blit(text5, (210, 370))
    pygame.display.update()
    time.sleep(4)
    