import pygame

pygame.init()

screen_width = 800
screen_height = 600
player_size = 50

enemy = pygame.Rect(200, 150, player_size, player_size)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pixel Pal")
clock = pygame.time.Clock()

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

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= 5
        if keys[pygame.K_RIGHT] and self.x < screen_width - self.size:
            self.x += 5
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= 5
        if keys[pygame.K_DOWN] and self.y < screen_height - self.size:
            self.y += 5

        self.rect.x = self.x
        self.rect.y = self.y

draw_player = Player(400, 300, 100, (255, 0, 0), player_size)
draw_enemy = Player(200, 150, 100, (0, 0, 255), player_size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    clock.tick(60)

    draw_player.movement()
    draw_player.draw(screen)
    draw_enemy.draw(screen)
    pygame.display.flip()

    if draw_player.rect.colliderect(draw_enemy):
        print("Collision detected!")
        running = False

pygame.quit()