import gui, math
re = gui.Gui() # mk it so that the coder does not have to do re. constantly
c=0
while re.running:
    c+=1
    re.cls((127,127,127))
    re.pix(math.cos(c/200)*12+48,84+math.sin(c/250)*20,(255,0,0))
    re.pix(math.cos(10-c/200)*12+48,84+math.sin(10-c/250)*20,(255,255,0))
    re.pix(math.cos(20-c/180)*12+48,84+math.sin(20-c/250)*20,(0,255,0))
    re.pix(math.cos(30-c/160)*12+48,84+math.sin(30-c/250)*20,(0,255,255))
    re.pix(math.cos(40-c/140)*12+48,84+math.sin(40-c/250)*20,(0,0,255))
    re.pix(math.cos(50-c/120)*12+48,84+math.sin(50-c/250)*20,(255,0,255))
    re.txt('Welcome to YANEpy',12,12,(0,0,0,255))
    re.tick()