import pygame
import random
pygame.init()

width = 900
height = 500

screen = pygame.display.set_mode((width, height))

# rgb format
# primary colors - red green blue
# rgb value - 0-255
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 42
blue = 0, 55, 255
screen.fill(green)

bg_music = pygame.mixer.Sound('assets/music_1.wav')
# bg_music.play(-1)

snake_bg = pygame.image.load('assets/snake_bg.png')
screen.blit(snake_bg, (0, 0))

msg = "Press SPACE to Start Game"
font = pygame.font.SysFont("assets/font_1.ttf", 60)
text = font.render(msg, True, red)
screen.blit(text, (180, 450))


def homeScreen():
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()  # quits pygame
                quit()  # quits python
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mainScreen()
                    # print("Main screen called...")

        pygame.display.update()


def mainScreen():

    x = 100
    y = 100
    moveX = 1
    moveY = 1

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()  # quits pygame
                quit()  # quits python

        screen.fill(white)

        # surface, color, (x,y), radius
        # pygame.draw.circle(screen, blue, (x, y), 50)

        # surface, color, (x,y,length,breadth)
        pygame.draw.rect(screen, blue, (x, y, 100, 100))
        x += moveX
        y += moveY

        pygame.display.update()


homeScreen()
