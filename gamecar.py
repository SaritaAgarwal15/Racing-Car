import pygame
import time
import random
pygame.init()

W=400
H=500

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)


gameDisplay=pygame.display.set_mode((W,H))
pygame.display.set_caption("FIRST GAME")

clock=pygame.time.Clock()

carImg=pygame.image.load("car.png")
carImg=pygame.transform.scale(carImg,(100,80))
carImg=pygame.transform.rotozoom(carImg,90,0.5)
wall=pygame.image.load("brwall.jpg")
wall=pygame.transform.scale(wall,(40,500))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def t_object(text, font):
    tsurface=font.render(text, True, black)
    return tsurface, tsurface.get_rect()

def msg_display(text):
    l_text=pygame.font.Font('The Fourth Avenue Sans.otf', 100)
    tsurf, trect=t_object(text, l_text)
    trect.center=((W/2), (H/2))
    gameDisplay.blit(wall,(0,0))
    gameDisplay.blit(wall,(W-40,0))
    gameDisplay.blit(tsurf, trect)


    pygame.display.update()


    time.sleep(3)

    game_loop()

def crashed():
    msg_display('You Crashed')


def game_loop():

    X=(W*0.45)
    Y=(H*0.8)
    x_change=0

    thing_startx=random.randrange(40, W-90)
    thing_starty=-600
    thing_speed=7
    thing_width=50
    thing_height=50

    crash= False
    while not crash:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                print("BYE")
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                elif event.key==pygame.K_RIGHT:
                    x_change=5
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
        X+=x_change

        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, black)

        thing_starty += thing_speed
        car(X,Y)

        if X>W-40-40 or X<40:
            crashed()
        if thing_starty > H:
            thing_starty=0-thing_height
            thing_startx=random.randrange(40, W-90)

        if Y < thing_starty + thing_height:
            print('y crossover')

            if X > thing_startx and X < thing_startx + thing_width or X+40 > thing_startx and X+40 < thing_startx + thing_width:
                print('y crossover')
                crashed()



        gameDisplay.blit(wall,(0,0))
        gameDisplay.blit(wall,(W-40,0))

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
print("BYE")
quit()
