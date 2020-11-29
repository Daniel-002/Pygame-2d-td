# Daniel Bloch og Mikkel Lind
# 2.D
# 29-11-2020



import pygame

pygame.init()

clock = pygame.time.Clock()




windowSize = (640, 360)

screen = pygame.display.set_mode(windowSize, 1600, 900)




map = [pygame.image.load('MarsMap.png'),
       pygame.image.load('lorteMoonMap.png')]

astronautR = [pygame.image.load('astronaut/astronaut-frame1.png'),
             pygame.image.load('astronaut/astronaut-frame2.png'),
             pygame.image.load('astronaut/astronaut-frame3.png'),
             pygame.image.load('astronaut/astronaut-frame4.png'),
             pygame.image.load('astronaut/astronaut-frame5.png'),
             pygame.image.load('astronaut/astronaut-frame6.png')]

astronautL = [pygame.image.load('astronaut/astronaut-frame1L.png'),
             pygame.image.load('astronaut/astronaut-frame2L.png'),
             pygame.image.load('astronaut/astronaut-frame3L.png'),
             pygame.image.load('astronaut/astronaut-frame4L.png'),
             pygame.image.load('astronaut/astronaut-frame5L.png'),
             pygame.image.load('astronaut/astronaut-frame6L.png')]

idelAstronaut = [pygame.image.load('astronaut/astronaut-frame1.png'),
                 pygame.image.load('astronaut/astronaut-frame1L.png')]



textFont = pygame.font.SysFont(None, 24)



def mainMenu():



    pygame.display.set_caption('main menu ')
    menu = False

    while not menu:
        screen.fill((75, 75, 75))
        choosemapText = textFont.render('choose map', True, (255, 255, 255))
        screen.blit(choosemapText, (50,50))

        mx, my = pygame.mouse.get_pos()

        button1 = pygame.Rect(100, 100, 200, 50)
        button2 = pygame.Rect(100, 200, 200, 50)

        if button1.collidepoint((mx, my)):
            if click:
                game(1)
        if button2.collidepoint((mx, my)):
            if click:
                game(2)

        pygame.draw.rect(screen, (100, 100, 100), button1)
        pygame.draw.rect(screen, (100, 100, 100), button2)

        button1Text = textFont.render('Mars', True, (255, 255, 255))
        button2Text = textFont.render('Moon', True, (255, 255, 255))

        screen.blit(button1Text, (180, 117))
        screen.blit(button2Text, (180, 217))

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.flip()
        clock.tick(60)




def game(maps):

    pygame.display.set_caption('epic mars game')

    done = False

    playerPosition = [600, 600]

    movingUp = False
    movingDown = False
    movingRight = False
    movingLeft = False
    right = True
    left = True

    aniTick = 0
    tickPuls = 0

    scroll = [0, 0]


    while not done:
        if right == True:
            astronaut = astronautR
        elif left == True:
            astronaut = astronautL

        scroll[0] += (playerPosition[0] - scroll[0] - 320)/5
        scroll[1] += (playerPosition[1] - scroll[1] - 180)/5


        if maps == 1:
            screen.blit(map[0], (0 - scroll[0], 0 - scroll[1]))
        else:
            screen.blit(map[1], (0 - scroll[0], 0 - scroll[1]))


        if movingUp == True or movingDown == True or movingLeft == True or movingRight == True:
            if aniTick >=6:
                aniTick = 0
            screen.blit(astronaut[aniTick], (320, 180))
            tickPuls += 1

            if tickPuls >= 6:
                aniTick += 1
                tickPuls = 0
        else:
            if right == True:
                screen.blit(idelAstronaut[0], (320, 180))
            elif left == True:
                screen.blit(idelAstronaut[1], (320, 180))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    movingUp = True
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    movingLeft = True
                    right = False
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    movingDown = True
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    movingRight = True
                    right = True
                elif event.key == pygame.K_ESCAPE:
                    done = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    movingUp = False
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    movingLeft = False
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    movingDown = False
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    movingRight = False
                elif event.key == pygame.K_ESCAPE:
                    done = False

        if movingUp == True and movingRight == False and movingLeft == False:
            playerPosition[1] -= 2
        if movingDown == True and movingRight == False and movingLeft == False:
            playerPosition[1] += 2
        if movingRight == True and movingUp == False and movingDown == False:
            playerPosition[0] += 2
        if movingLeft == True and movingUp == False and movingDown == False:
            playerPosition[0] -= 2
        if movingUp == True and movingRight == True and movingLeft == False:
            playerPosition[0] += 1.4
            playerPosition[1] -= 1.4
        if movingDown == True and movingRight == True and movingLeft == False:
            playerPosition[0] += 1.4
            playerPosition[1] += 1.4
        if movingLeft == True and movingUp == True and movingDown == False:
            playerPosition[0] -= 1.4
            playerPosition[1] -= 1.4
        if movingLeft == True and movingUp == False and movingDown == True:
            playerPosition[0] -= 1.4
            playerPosition[1] += 1.4

        if playerPosition[0] < 320:
            playerPosition[0] = 320

        if playerPosition[1] < 180:
            playerPosition[1] = 180

        if playerPosition[0] > 1180:
            playerPosition[0] = 1180

        if playerPosition[1] > 1320:
            playerPosition[1] = 1320










        pygame.display.flip()
        clock.tick(60)

mainMenu()