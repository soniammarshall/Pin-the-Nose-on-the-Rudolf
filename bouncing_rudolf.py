"""
Created on Sat Dec  2 10:49:12 2017

@authors: sonia and caterina


"""

import pygame, sys, random, time

RED = (255, 0, 0)
WHITE = (255, 255, 255)
image = pygame.image.load("blackNosedRudolf.png")
woohooImage = pygame.image.load("woohoo.png")


pygame.init()

# Set the width and height of the screen [width, height]
size = (width, height) = image.get_size()
sizeWoo = (widthWoo, heightWoo) = woohooImage.get_size()
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pin the nose on the Rudolf!")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

R = 35
woohooVis = False

center = [x,y] = [random.randint(0 + R, width - R), random.randint(0 + R, height - R)]
direction = [incX, incY] = [5, 2]

pygame.mixer.music.load("night.mp3")
pygame.mixer.music.play(loops = -1)

# -------- Main Program Loop -----------
while not done:

    [xT, yT] = [x, y - R]
    [xR, yR] = [x + R, y]
    [xB, yB] = [x, y + R]
    [xL, yL] = [x - R, y]

    # --- Main event loop


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if (incX == 0 and incY == 0):
                incX = random.randint(2,width//20)
                incY = random.randint(2,height//20)
            else:
                incX = 0
                incY = 0
                # if user stops nose in right place
                if (yT <= 210 and yB >= 210 and xL <= 175 and xR >= 175):
                    woohooVis = True
                    incX = random.randint(2,width//20)
                    incY = random.randint(2,height//20)


    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    #screen.fill(backgroundColour)

    screen.blit(image, [0, 0])


    if woohooVis:
        screen.blit(woohooImage, [(width - widthWoo)//2, (height - heightWoo)//2])
        pygame.display.flip()
        print("image displayed")
        time.sleep(3)
        print("sleep finished")
        woohooVis = False
    else:
        pygame.draw.circle(screen, RED, [x, y], R)

    # -- work out new direction

    if yT <= 0:
        incY = (-1) * incY + 1
    elif yB >= height:
        incY = (-1) * incY - 1

    if xL<= 0:
        incX = (-1) * incX + 1
    elif xR >= width:
        incX = (-1) * incX - 1


    # -- update position of cirle

    x += incX
    y += incY

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

print("Wooooohoooo!")
# Close the window and quit.
pygame.quit()
