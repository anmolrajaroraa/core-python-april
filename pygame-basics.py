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
# bg_music.play(-1)  # -1 means keep playing the sound continuously

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
    # moveX = random.randint(5, 10)
    # moveY = random.randint(5, 10)
    moveX = 0
    moveY = 0
    counter = 0
    # font = pygame.font.SysFont("assets/font_1.ttf", 30)
    font = pygame.font.SysFont(None, 30)
    x2 = random.randint(0, width - 50)
    y2 = random.randint(0, height - 50)
    frog = pygame.image.load("assets/frog_2.png")
    coinSound = pygame.mixer.Sound("assets/point.wav")
    snakeWidth = 50
    snakeBody = []
    snakeLength = 1

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()  # quits pygame
                quit()  # quits python
            if event.type == pygame.KEYDOWN:  # control snake using keys
                if event.key == pygame.K_UP:
                    moveY = -10
                    moveX = 0
                if event.key == pygame.K_DOWN:
                    moveY = 10
                    moveX = 0
                if event.key == pygame.K_LEFT:
                    moveX = -10
                    moveY = 0
                if event.key == pygame.K_RIGHT:
                    moveX = 10
                    moveY = 0

        screen.fill(white)

        scoreMsg = f"Score : {counter}"
        scoreText = font.render(scoreMsg, True, red)
        screen.blit(scoreText, (20, 20))

        # surface, color, (x,y), radius
        # pygame.draw.circle(screen, blue, (x, y), 50)

        # surface, color, (x,y,length,breadth)
        # rect1 = pygame.draw.rect(screen, blue, (x, y, snakeWidth, 50))
        # rect2 = pygame.draw.rect(screen, red, (x2, y2, 50, 50))
        rect1 = pygame.Rect((x, y, 50, 50))
        rect2 = pygame.Rect((x2, y2, 50, 50))
        screen.blit(frog, (x2, y2))
        x += moveX
        y += moveY

        # snakeBody.append([x, y])
        snakeBody.insert(0, [x, y])
        if len(snakeBody) > snakeLength:
            del snakeBody[-1]
            # pass

        print(snakeBody)

        for bodyPart in snakeBody:
            color = random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255)
            pygame.draw.rect(screen, color, (bodyPart[0], bodyPart[1], 50, 50))

        if rect1.colliderect(rect2):
            x2 = random.randint(0, width - 50)
            y2 = random.randint(0, height - 50)
            coinSound.play()
            counter += 1
            # snakeWidth += 50
            snakeLength += 1

        if y < -50:   # snake game animation
            y = height
        if x < -50:
            x = width
        if x > width:
            x = -50
        if y > height:
            y = -50

        # if x + 100 > width:   # ball game animation
        #     moveX = random.randint(-10, -5)
        # elif x < 0:
        #     moveX = random.randint(5, 10)
        # elif y < 0:
        #     moveY = random.randint(5, 10)
        # elif y + 100 > height:
        #     moveY = random.randint(-10, -5)

        pygame.display.update()


homeScreen()
