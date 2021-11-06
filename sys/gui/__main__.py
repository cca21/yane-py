print('--- If this crashes, you need to install pygame through pip\n\
pip install pygame')
# cartridges are .zip files with this structure:
# __main__.py
# sprites/
### bg (128x128 file, each pixel only requiring 4 bytes (for 16 colors); background sprites from 0-255)
### fg (128x128 file, each pixel only requiring 4 bytes (for 16 colors); foreground sprites from 256-511)
# instrument/
### (i have no idea how im going to represent samples in file format, for now just use .wav lol)
import pygame,zipfile,math,os
from sys import argv
pygame.init()
pygame.display.init()
screen_size=(320,240)
screen = pygame.display.set_mode(size=screen_size,flags=pygame.RESIZABLE|pygame.SCALED)
screen_surface = pygame.display.get_surface()
clock = pygame.time.Clock()
font = pygame.font.SysFont('Courier New',20)
fontsurface = font.render('Cart needed!',0,'#00ff00')
c = 0
running = True
if len(argv) > 1:
    cart = True
else:
    cart = False
while running: # cart(.zip file, will be a module) loaded (will read from stdio); 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if cart == False: # i dont like that check every single frame, but i dont know how else to put it
        screen.fill('#000000')
        screen.blit(fontsurface,(
        screen_size[0]/2+math.sin(c/500)*16-fontsurface.get_size()[0]/2,
        screen_size[1]/2+math.cos(c/480)*16-fontsurface.get_size()[1]/2
        ))
        pygame.display.flip()
        c+=1
        clock.tick(600)
    else:
        try:
            run("python "+" ".join(argv[1:]))
        except Exception as err:
            print('Something went wrong!\n',err)
            exit()