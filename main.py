import pygame

pygame.init()

screen_width = 800
screen_height = 600
player_size = 50
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pixel Pal")

WHITE = (255, 255, 255)
x = 100
y = 100

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= 5
    if keys[pygame.K_RIGHT] and x < screen_width - player_size:
        x += 5
    if keys[pygame.K_UP] and y > 0:
        y -= 5
    if keys[pygame.K_DOWN] and y < screen_height - player_size:
        y += 5

    screen.fill(WHITE)
    pygame.draw.rect(screen, (225, 0, 0), (x, y, player_size, player_size))
    pygame.display.flip()

pygame.quit()