import pygame

pygame.init()

screen_width = 800
screen_height = 600
player_size = 50

enemy = pygame.Rect(200, 150, player_size, player_size)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pixel Pal")

WHITE = (255, 255, 255)

class Player:
    def __init__(self, x, y, hp, color, size):
        self.x = x
        self.y = y
        self.hp = hp
        self.color = color
        self.size = size
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

draw_player = Player(100, 100, 100, (0, 0, 255), 50)
draw_enemy = Player(200, 200, 100, (255, 0, 0), 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and draw_player.x > 0:
        draw_player.x -= 5
    if keys[pygame.K_RIGHT] and draw_player.x < screen_width - player_size:
        draw_player.x += 5
    if keys[pygame.K_UP] and draw_player.y > 0:
        draw_player.y -= 5
    if keys[pygame.K_DOWN] and draw_player.y < screen_height - player_size:
        draw_player.y += 5

    draw_player.rect.x = draw_player.x
    draw_player.rect.y = draw_player.y

    screen.fill(WHITE)
    draw_player.draw(screen)
    draw_enemy.draw(screen)
    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60)
    if draw_player.rect.colliderect(draw_enemy):
        print("Collision detected!")
        running = False

pygame.quit()