import pygame, pygame.gfxdraw, math
class Gui:
    screen = pygame.display.set_mode(size=(256,192),flags=pygame.RESIZABLE|pygame.SCALED)
    blits = [] # self.blits is how you refer to it in functions
    event = None
    running = True
    def __init__(self):
        pygame.init()
    def tick(self):
        self.screen.blits(self.blits)
        pygame.display.flip()
        self.blits = []
        if self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.event = event
    def txt(self, string, x, y, color):
        font = pygame.font.SysFont('monospace',20) # can be prerendered but whatever
        fonts = font.render(string,0,color)
        self.blits += [(fonts, (x, y))]
    def spr(self, spr_id, x, y): # sprite
        pass
    def pix(self, x, y, color): # draw a single pixel
        pygame.gfxdraw.pixel(self.screen, int(x), int(y), color)
    def cls(self, color): # clear screen with desired color
        self.screen.fill(color)
    def key(self): # get current key pressed; returns 2 bytes (16 bits), checks if QWERASDF YUIOHJKL are pressed
        pass
    # line function?
# cart(.zip file, will be a module) loaded (will read from stdio); 
#while running: # make this a builtin method of class 
#    for event in pygame.event.get(): # figure out how to abstract event checks out of existance
#        if event.type == pygame.QUIT:
#            running = False 
#    re.blits = []
#    re.cls('#116644')
#    re.txt('Test',math.sin(c/1000)*100+108,math.cos(c/1000)*50+80,'#55ff33')
#    re.screen.blits(re.blits)
#    pygame.display.flip() # this too, i guess/want
#    c+=1