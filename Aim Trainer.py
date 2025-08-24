import pygame
import random
pygame.init()

X, Y = 500, 550

window = pygame.display.set_mode((X, Y))
caption = pygame.display.set_caption("Aim Trainer")
target = pygame.image.load("C:\\Users\\Edwin\\Documents\\Python\\Pygame Module\\Target.PNG") #Only downside is setting your file directory
clock = pygame.time.Clock()

x, y = random.randint(0, X - 50), random.randint(50, Y - 50)
targetSize = (50, 50)
target = pygame.transform.scale(target, targetSize)

def draw():
    window.fill((0, 0, 0))
    window.blit(target, (x, y))
    pygame.draw.rect(window, (255, 255, 255), (0, 0, 500, 50))

    clickText = font.render(("Clicks: " + str(clicks)), 1, (0, 0, 0))
    timeText = font.render(("Time: " + str(current_time / 1000)), 1, (0, 0, 0))
    speedText = font.render(("CPS: " + str(clickSpeed)), 1, (0, 0, 0))

    window.blit(clickText, (0, 0))
    window.blit(timeText, (150, 0))
    window.blit(speedText, (350, 0))
    pygame.display.update()

font = pygame.font.SysFont("Comic Sans MS", 20, "Bold", True)
clicks = 0
current_time = 0
clickSpeed = 0

run = True
while run:
    clock.tick(60)
    current_time = pygame.time.get_ticks()

    if current_time >= 30000:
        current_time = 30000
        clickSpeed = round(clicks / (current_time / 1000), 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        #Needed help with this
        if event.type == pygame.MOUSEBUTTONDOWN and current_time < 30000: #detects when the mouse is clicked
            target_rect = pygame.Rect(x, y, 50, 50)
            background_rect = pygame.Rect(0, 50, X, Y-50)

            if target_rect.collidepoint(event.pos) and current_time < 30000:
                clicks += 1
                x, y = random.randint(0, X - 50), random.randint(50, Y - 50)

    draw()