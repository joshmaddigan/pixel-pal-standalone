import pygame

pygame.init()

screen_width = 800
screen_height = 600
player_size = 50
x = 100
y = 100
player = pygame.Rect(x, y, player_size, player_size)
enemy = pygame.Rect(200, 150, player_size, player_size)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pixel Pal")

WHITE = (255, 255, 255)


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

    player.x = x
    player.y = y

    screen.fill(WHITE)
    pygame.draw.rect(screen, (225, 0, 0), (x, y, player_size, player_size))
    pygame.draw.rect(screen, (0, 0, 255), (200, 150, player_size, player_size))
    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60)
    if player.colliderect(enemy):
        print("Collision detected!")
        running = False

pygame.quit()