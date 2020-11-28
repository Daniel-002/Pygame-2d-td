import pygame

pygame.init()

clock = pygame.time.Clock()

done = False

pygame.display.set_caption('epic mars game')
windowSize = (640, 360)
screen = pygame.display.set_mode(windowSize, 1600, 900)

camera = [0, 0]


background = pygame.image.load('MarsMap.png')

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


playerPosition = [320, 240]

movingUp = False
movingDown = False
movingRight = False
movingLeft = False
right = True
left = True

aniTick = 0
tickPuls = 0


while not done:
    screen.blit(background, (0, 0))
    if right == True:
        astronaut = astronautR
    elif left == True:
        astronaut = astronautL

    srfes = pygame.Surface((32,32), False, (255, 255, 255))
    srfesrect = pygame.Rect(50, 50, 32, 32)
    pygame.draw.rect(srfes, (0, 0, 255), srfesrect)

    camera[0] += (camera[0] - playerPosition[0])/2
    camera[1] += (camera[1] - playerPosition[1])/2

    if movingUp == True or movingDown == True or movingLeft == True or movingRight == True:
        if aniTick >=6:
            aniTick = 0
        screen.blit(astronaut[aniTick], (playerPosition))
        tickPuls += 1

        if tickPuls >= 6:
            aniTick += 1
            tickPuls = 0
    else:
        if right == True:
            screen.blit(idelAstronaut[0], (playerPosition))
        elif left == True:
            screen.blit(idelAstronaut[1], (playerPosition))


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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                movingUp = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                movingLeft = False
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                movingDown = False
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                movingRight = False

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

    if playerPosition[1] < 0:
        playerPosition[1] = 0

    if playerPosition[0] < 0:
        playerPosition[0] = 0









    pygame.display.update()
    clock.tick(60)