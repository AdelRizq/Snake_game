#!/usr/bin/env python

import pygame
import time
import random

display_height = 600
display_width = 800

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
burble = (185,88,211)

gameExit = True

snake_length = 10
snake_width = 10
snakeLen = 1

block_size = 20
AppleThickness = 30

FPS = 15
Screen_FPS = 50

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont('comicsansms', 25)
uppersmallfont = pygame.font.SysFont('comicsansms', 35)
medfont = pygame.font.SysFont('comicsansms', 50)
largefont = pygame.font.SysFont('comicsansms', 75)

img = pygame.image.load('Snake Head.png')
apple_img = pygame.image.load('Apple.png')
tail_img = pygame.image.load('Snake Tail.png')
icon = pygame.image.load('Snake Head.png')
pygame.display.set_icon(icon)

direction = 'up'

def rotate_tail(x1,y1,x2,y2):
    x = x1 - x2
    y = y1 - y2
    if x > 0:
        return pygame.transform.rotate(tail_img, 90)
    elif x < 0:
        return pygame.transform.rotate(tail_img, 270)
    elif y > 0:
        return pygame.transform.rotate(tail_img, 360)
    elif y < 0:
        return pygame.transform.rotate(tail_img, 180)
    
    
def snake(block_size, snakeList, snakeTail):
    tail = tail_img
    if direction == 'up':
        head = img
        #tail = tail_img
    elif direction == 'right':
        head = pygame.transform.rotate(img, 270)
        #tail = pygame.transform.rotate(tail_img, 270)
#        snakeTail = [snakeList[-1][0] - snakeLen * 20, snakeList[-1][1]]
    elif direction == 'left':
        head = pygame.transform.rotate(img, 90)
        #tail = pygame.transform.rotate(tail_img, 90)
#        snakeTail = [snakeList[-1][0] + snakeLen * 20, snakeList[-1][1]]
    elif direction == 'down':
        head = pygame.transform.rotate(img, 180)
        #tail = pygame.transform.rotate(tail_img,180)
#        snakeTail = [snakeList[-1][0], snakeList[-1][1] - snakeLen * 20]
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    #gameDisplay.blit(tail, (snakeTail[0], snakeTail[1]))
    #gameDisplay.blit(tail_img, ())
#    snakeList.append([snakeTail[0], snakeTail[1]])
#    snakeList([snakeTail[0], snakeTail[1]])
    count = 0
    for XnY in snakeList[:-1]:
        if count == 0:
            tail = rotate_tail(snakeList[0][0],snakeList[0][1],snakeList[1][0],snakeList[1][1])
            gameDisplay.blit(tail, (snakeList[0][0], snakeList[0][1]))
            count += 1
        else:
            pygame.draw.rect(gameDisplay, black, [XnY[0], XnY[1], block_size, block_size])
        
#    gameDisplay.blit(tail, (snakeList[0][0], snakeList[0][1]))
    #pygame.draw.rect(gameDisplay, black, [snakeList[0][0], snakeList[0][1], block_size, block_size])

def Apple_Gen(snakeList):
    Valid = False
    while Valid == False:
        appleX = random.randrange(0, display_width-AppleThickness, AppleThickness)
        appleY = random.randrange(0, display_height-AppleThickness, AppleThickness)
        appleXY = [appleX, appleY]
        Valid = Valid_apple(appleXY, snakeList)
                
    return appleX, appleY


def Valid_apple(appleXY, snakeList):
    for eachpiece in snakeList[:-1]:
        if eachpiece == appleXY:
            return False
    return True
    
        

def intro_screen():
    intro = True
    
    while intro:
        gameDisplay.fill(white)
        msg_to_screen('Welcome to El7ansh', blue, -150, 'large')
        msg_to_screen('The Objective is to eat Apples as much as U can.', green, -60, 'upsmall')
        msg_to_screen('The more U eat, the longer U get.', green, -30, 'upsmall')
        msg_to_screen('if U hit edges or yourself, U die.', green, -0, 'upsmall')
        msg_to_screen('Press C to play :) P to pause -_- Q to Quit :(', blue, 80, 'medium')
        msg_to_screen('Press Escape at anytime to Leave :[', blue, 130, 'medium')
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                    
        clock.tick(Screen_FPS)


def score(score):
    show = uppersmallfont.render("Score: " + str(score), True, blue)
    gameDisplay.blit(show, (10, 10))
    

def pause():
    paused = True
    
    msg_to_screen('Paused', blue, -100, 'large')
    msg_to_screen('Press C to Start OR Q to Quit :)', blue, 20, 'upsmall')
    pygame.display.update()
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        #gameDisplay.fill(white)
        clock.tick(FPS)

def textObjects(msg, color, size = 'small'):
    if size == 'small':
        textSurface = smallfont.render(msg, True, color)
    elif size == 'medium':
        textSurface = medfont.render(msg, True, color)
    elif size == 'upsmall':
        textSurface = uppersmallfont.render(msg, True, color)
    elif size == 'large':
        textSurface = largefont.render(msg, True, color)
    return textSurface, textSurface.get_rect()


def msg_to_screen(msg, color, y_display = 0, size = 'small'):
    textSurface, textRect = textObjects(msg, color, size)
    textRect.center = (display_width // 2), (display_height // 2) + y_display
    gameDisplay.blit(textSurface, textRect)
    #screen_msg = font.render(msg, True, color)
    #gameDisplay.blit(screen_msg, [display_width//2, display_height//2])


def gameloop():    
    
    gameExit = True
    gameover = True

    change_x = 0
    change_y = 0

    lead_x = display_width // 2
    lead_y = display_height // 2

    snakeList = []
    global snakeLen
    snakeLen = 1
    appleX, appleY = Apple_Gen(snakeList)
    
    global direction
    global Screen_FPS

    event_key_temp = ''
    
    while gameExit:
        if gameover == False:
            msg_to_screen('Game Over', red, -30, 'large')
            msg_to_screen('Press C to play again or Q to Quit', black, 60, 'medium')
            pygame.display.update()
            
        while not gameover:
            #gameDisplay.fill(white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = True
                    gameExit = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameloop()
                    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        gameover = True
                        gameExit = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if event_key_temp == 'left':
                        direction = 'left'
                        change_x = -block_size
                    else:
                        direction = 'right'
                        change_x = block_size
                    change_y = 0
                elif event.key == pygame.K_LEFT:
                    if event_key_temp == 'right':
                        direction = 'right'
                        change_x = block_size
                    else:
                        direction = 'left'
                        change_x = -block_size
                    change_y = 0
                elif event.key == pygame.K_UP:
                    if event_key_temp == 'down':
                        direction = 'down'
                        change_y = block_size
                    else:
                        direction = 'up'
                        change_y = -block_size
                    change_x = 0
                elif event.key == pygame.K_DOWN:
                    if event_key_temp == 'up':
                        direction = 'up'
                        change_y = -block_size
                    else:
                        direction = 'down'
                        change_y = block_size
                    change_x = 0
                elif event.key == pygame.K_p:
                    pause()

                event_key_temp = direction

            #if event.type == pygame.KEYUP: #for Moving if holding the key only
                #if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    #change_x = 0
                #if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    #change_y = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

        if lead_x >= display_width or lead_x <= -1 or lead_y >= display_height or lead_y <= -1:
            gameover = False

        lead_x += change_x
        lead_y += change_y

         #if appleX == lead_x and appleY == lead_y: # 1st Edition
            #appleX = random.randrange(0, display_width - block_size, 10)
            #appleY = random.randrange(0, display_height - block_size, 10)
           # snakeLen += 1

        #if lead_x >= appleX and lead_x <= appleX+AppleThickness: # 2nd Edition
            #if lead_y >= appleY and lead_y <= appleY + AppleThickness:
                #appleX = random.randrange(0, display_width - block_size, 10)
                #appleY = random.randrange(0, display_height - block_size, 10)
                #snakeLen += 1

        if lead_x >= appleX and lead_x <= appleX + AppleThickness or lead_x + block_size >= appleX and lead_x + block_size <= appleX + AppleThickness: # 3rd Edition
            if lead_y >= appleY and lead_y <= appleY + AppleThickness or lead_y + block_size >= appleY and lead_y + block_size <= appleY + AppleThickness:
                appleX, appleY = Apple_Gen(snakeList)
                snakeLen += 1

        gameDisplay.fill(white)
        #pygame.draw.rect(gameDisplay, red, [appleX, appleY, AppleThickness, AppleThickness])
        gameDisplay.blit(apple_img, (appleX, appleY))

        snakeHead = [lead_x, lead_y]
        snakeTail = [lead_x , lead_y + snakeLen*20]
        snakeList.append(snakeHead)
        
        #snakeList.append(snakeTail)
        if len(snakeList) > snakeLen:
            del snakeList[0]
        snake(block_size, snakeList, snakeTail)

        for eachpiece in snakeList[:-1]:
            if eachpiece == snakeHead:
                gameover = False
        
        score(snakeLen - 1)
        
        pygame.display.update()
        clock.tick(FPS) #or pygame.time.delay(MilleSeconds)

    pygame.quit()
    quit()
    
intro_screen()
gameloop()
