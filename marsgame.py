import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Mars TD')

astronaut = pygame.image.load('astronaut/astronaut-frame1.png')
background = pygame.image.load('pixil-layer-Background.png')
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

def drawingscreen():
    screen.blit(background, (0,0))
    if is_blue:
        color = (255, 0, 0)
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    pygame.display.flip()
    clock.tick(60)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    drawingscreen()

