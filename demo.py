from pyhiero.pygamefont import PyGameHieroFont



import pygame, sys
from pygame.locals import *


pygame.init()

screen = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Hello World!')


fnt = PyGameHieroFont("examples/CabinSketch/CabinSketch.fnt")

txt = fnt.render("Hello World! *g* - semi", color=(128,0,0))

while True: 
	for event in pygame.event.get():

		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	screen.fill((255,255,255))

	screen.blit(txt, (0,0))

	pygame.display.update()

