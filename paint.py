import sys, pygame
from rdp import rdp
from pygame.locals import *
pygame.init() #Starts pygame
screen = pygame.display.set_mode((600, 600), pygame.NOFRAME) #window, and sets the size
screen.fill((255,255,255)) # Fills background color
brush = pygame.image.load("brush.jpg") #Loads the image into a variable
brush = pygame.transform.scale(brush, (10,10)) #Scales the image into a more useable
clock = pygame.time.Clock() #Makes a clock to track the ticks within the game
z = 0
lines = [[] for i in range(100)]
cur = 0

def runRdp(arr):
    arr = [rdp(p,epsilon=10) for p in arr]
    return arr

def showFinal(arr):
    for line in arr:
        for pos in line:
            screen.blit(brush,(pos[0],pos[1]))

while True:
    clock.tick(120) #Limits the ticks to 60 (FPS)
    x,y = pygame.mouse.get_pos() #Sets two variables for the mouse position
    for event in pygame.event.get(): #Recieves events
        if event.type == QUIT: #Checks if the event is a QUIT event
            pygame.quit()  ##Quits##
            sys.exit()     ##Quits##
        elif event.type == MOUSEBUTTONDOWN:
            z = 1 #If you press the mouse button down, it sets the screen blit to true
        elif event.type == MOUSEBUTTONUP:
            cur+=1
            z = z - 1 #Does the opposite of the above elif statement
        if z == 1: #Cheks if the variable z is true, if it is; updates the screen with the brush
            lines[cur].append([x,y])
            screen.blit(brush,(x-5,y-5))
        if event.type == KEYDOWN:
            if event.key == pygame.K_p:
                lines = runRdp(lines)
                screen.fill((255,255,255))
                showFinal(lines)
                pygame.display.update()
            if event.key == pygame.K_r:
                screen.fill((255,255,255))
                lines = [[] for i in range(100)]
                pygame.display.update()
            if event.key == pygame.K_x:
                pygame.quit()  ##Quits##
                sys.exit()

    pygame.display.update()

