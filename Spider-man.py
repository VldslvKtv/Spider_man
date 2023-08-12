#!/usr/bin/env python
# -*- coding: utf-8 -*
import pygame, random, sys, time
from pygame.locals import *


WINDOW1 = 1000
WINDOW2 = 580
TEXTCOLOR = (255, 255, 255)
BACKCOLOR = (255, 255, 255)
FPS = 60
BADminSize = 20
BADmaxSize = 60
BADminSpeed = 3
BADmaxSpeed = 6
ADDNEWBADDIERATE = 6
PLAYERMOVE = 5
x = WINDOW1 / 2
y = WINDOW2 - 80


def terminate():
    pygame.quit()
    sys.exit()


def waitForPlayerPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return


def exit():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return


def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False


def drawText(text, font, surface, x, y):
    textOBJ = font.render(text, 1, TEXTCOLOR)
    textrect = textOBJ.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textOBJ, textrect)


pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOW1, WINDOW2))
pygame.display.set_caption(' The amazing Spider-man ')
pygame.mouse.set_visible(False)

font = pygame.font.Font('sh4.ttf', 27)
font2 = pygame.font.Font('sh4.ttf', 35)
font3 = pygame.font.Font('sh1.ttf', 48)
font4 = pygame.font.Font('sh1.ttf', 55)

gameOverSound = pygame.mixer.Sound('gameover1.wav')
musicHit = pygame.mixer.Sound('hit1.wav')
pygame.mixer.music.load('fon1.wav')
intro = pygame.mixer.Sound('mus1.wav')

transColor = pygame.Color(255, 255, 255)
transColor1 = pygame.Color(0, 0, 0)
transColor2 = pygame.Color(255, 0, 0)

playerImage = pygame.image.load('Sman.1.png')
l1 = pygame.image.load('left1.1.png')
l2 = pygame.image.load('left2.2.png')
l3 = pygame.image.load('left3.3.png')
r1 = pygame.image.load('right1.1.png')
r2 = pygame.image.load('right2.2.png')
r3 = pygame.image.load('right3.3.png')
j1 = pygame.image.load('jump1.png')
j2 = pygame.image.load('jump2.png')

h1 = pygame.image.load('h1.png')
h1 = pygame.transform.scale(h1, (40, 40))
h2 = pygame.image.load('h2.png')
h2 = pygame.transform.scale(h2, (40, 40))
h3 = pygame.image.load('h3.png')
h3 = pygame.transform.scale(h3, (40, 40))
d = pygame.image.load('d.png')
d = pygame.transform.scale(d, (40, 40))
d1 = pygame.image.load('d.png')
d1 = pygame.transform.scale(d, (40, 40))
d2 = pygame.image.load('d.png')
d2 = pygame.transform.scale(d, (40, 40))

playerImage.set_colorkey(transColor1)
l1.set_colorkey(transColor1)
l2.set_colorkey(transColor1)
l3.set_colorkey(transColor1)
r1.set_colorkey(transColor1)
r2.set_colorkey(transColor1)
r3.set_colorkey(transColor1)
j1.set_colorkey(transColor1)
j2.set_colorkey(transColor1)

playerL = [l1, l2, l3, l1, l2, l3]
playerR = [r1, r2, r3, r1, r2, r3]
jumpR = [j1, j1, j1, j1, j1, j1]
jumpL = [j2, j2, j2, j2, j2, j2]

playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('Venom2.png').convert()
baddieImage.set_colorkey(transColor)
goblin = pygame.image.load('goblin.png').convert()
goblin.set_colorkey(transColor1)
karnage = pygame.image.load('kar2.png').convert()
karnage.set_colorkey(transColor1)
FirstFon = pygame.image.load('FirstFon.png').convert()
FirstFon = pygame.transform.scale(FirstFon, (1200, 620))
Fon = pygame.image.load('town.jpg').convert()
Fon = pygame.transform.scale(Fon, (1100, 600))
Emblema = pygame.image.load('emb.png').convert()
Emblema = pygame.transform.scale(Emblema, (250, 120))

windowSurface.blit(FirstFon, (0, 0))
windowSurface.blit(Emblema, (580, 370))
drawText('Spider-man', font4, windowSurface, (WINDOW1 / 1.9), (WINDOW2 / 2))
drawText('Нажмите любую клавишу для начала игры', font, windowSurface, (WINDOW1 / 2) - 30, (WINDOW2 / 5) + 50)
intro.play()
pygame.display.update()
waitForPlayerPressKey()

BestScore = 0
while True:
    intro.stop()
    baddies = []
    cheat1 = cheat2 = False
    score = 0
    playerRect.topleft = (x, y)
    moveLeft = False
    moveRight = False
    jump = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)
    animcount = 0
    dead = 0
    jumpcount = 9
    lastmove = 'right'


    def newWin():
        global animcount
        if animcount + 1 >= 60:
            animcount = 0
        if moveLeft:
            windowSurface.blit(playerL[animcount // 10], (x, y))
            animcount += 1
        elif moveRight:
            windowSurface.blit(playerR[animcount // 10], (x, y))
            animcount += 1
        elif jump:
            if lastmove == 'right':
                windowSurface.blit(jumpR[animcount // 10], (x, y))
                animcount += 1
            else:
                windowSurface.blit(jumpL[animcount // 10], (x, y))
                animcount += 1
        else:
            windowSurface.blit(playerImage, (x, y))


    while True:

        score += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    jump = True
                if event.key == K_y:
                    cheat1 = True
                if event.key == K_i:
                    cheat2 = True
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                    lastmove = 'left'

                elif event.key == K_RIGHT or event.key == K_d:
                    moveRight = True
                    moveLeft = False
                    lastmove = 'right'
                else:
                    moveLeft = False
                    moveRight = False
                    animcount = 0

            if event.type == KEYUP:
                if event.key == K_y:
                    cheat1 = False
                if event.key == K_i:
                    cheat2 = False
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False

        if not cheat1 and not cheat2:
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE * 2:
            baddieAddCounter = 0
            baddieSize = random.randint(BADminSize, BADmaxSize)
            if score % 9 == 0:
                newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOW1 - baddieSize), 0 - baddieSize, baddieSize,
                                                 baddieSize),
                             'speed': random.randint(BADminSpeed, BADmaxSpeed),
                             'surface': pygame.transform.scale(goblin, (baddieSize, baddieSize))}
            elif score % 10 == 0:
                newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOW1 - baddieSize), 0 - baddieSize, baddieSize,
                                                 baddieSize),
                             'speed': random.randint(BADminSpeed, BADmaxSpeed),
                             'surface': pygame.transform.scale(karnage, (baddieSize, baddieSize))}
            else:
                newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOW1 - baddieSize), 0 - baddieSize, baddieSize,
                                                 baddieSize),
                             'speed': random.randint(BADminSpeed, BADmaxSpeed),
                             'surface': pygame.transform.scale(baddieImage, (baddieSize, baddieSize))}
            baddies.append(newBaddie)

        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVE, 0)
            x -= PLAYERMOVE
        if moveRight and playerRect.right < WINDOW1:
            playerRect.move_ip(PLAYERMOVE, 0)
            x += PLAYERMOVE
        if jump:
            if jumpcount >= -9:
                if jumpcount < 0:
                    y += (jumpcount ** 2) / 1.8
                else:
                    y -= (jumpcount ** 2) / 1.8
                jumpcount -= 0.5
            else:
                jump = False
                jumpcount = 9

        windowSurface.blit(Fon, (0, 0))

        for b in baddies:
            if not cheat1 and not cheat2:
                b['rect'].move_ip(0, b['speed'])

        for b in baddies[:]:
            if b['rect'].top > WINDOW2:
                baddies.remove(b)

        newWin()

        drawText('Счет: %s' % (score), font, windowSurface, 10, 0)
        drawText('Рекорд: %s' % (BestScore), font, windowSurface, 10, 40)

        windowSurface.blit(h1, (800, 30))
        windowSurface.blit(h2, (850, 30))
        windowSurface.blit(h3, (900, 30))

        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

        for b in baddies:
            if b['rect'].top == y and b['rect'].centerx == x and y < WINDOW2 - 80 and jump == True:
                dead += 1
                musicHit.play()
        if playerHasHitBaddie(playerRect, baddies) and jump == False:
            dead += 1
            musicHit.play()
        if dead > 15:
            windowSurface.blit(d, (800, 30))
        if dead > 45:
            windowSurface.blit(d, (800, 30))
            windowSurface.blit(d1, (850, 30))
        if dead > 75:
            musicHit.stop()
            pygame.mixer.music.stop()
            windowSurface.blit(d, (800, 30))
            windowSurface.blit(d1, (850, 30))
            windowSurface.blit(d2, (900, 30))
            if score > BestScore:
                BestScore = score
            break
        pygame.display.update()
        mainClock.tick(FPS)

    gameOverSound.play()
    x = WINDOW1 / 2
    y = WINDOW2 - 80

    drawText('GAME OVER', font3, windowSurface, (WINDOW1 / 2.6), (WINDOW2 / 3))
    drawText('Нажмите на SPACE, если хотите сыграть еще', font2, windowSurface, (WINDOW1 / 3.8) - 120,
             (WINDOW2 / 2.8) + 50)
    pygame.display.update()

    exit()
