import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
player_size = 50

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pixel Pal")
clock = pygame.time.Clock()
tick_event = pygame.USEREVENT
pygame.time.set_timer(tick_event, 3000) # 3 seconds
font = pygame.font.SysFont("Arial", 24)

WHITE = (255, 255, 255)

class PixelPal:
    def __init__(self, name, hunger, happiness, energy, max_value):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.max_value = max_value
        self.hunger_decay = random.uniform(0.1, 0.2)
        self.happiness_decay = random.uniform(0.05, 0.1)
        self.energy_decay = random.uniform(0.2, 0.3)

    def feed(self, hunger_up):
        self.hunger = int(min(self.max_value, self.hunger + hunger_up))

    def tick(self):
        self.hunger -= int(self.hunger_decay * self.max_value)
        self.happiness -= int(self.happiness_decay * self.max_value)
        self.energy -= int(self.energy_decay * self.max_value)

    def is_dead(self):        
        if self.hunger <= 0 or self.happiness <= 0 or self.energy <= 0:
            return True
        else:
            return False
        
## NEED TO GENERATE SPRITE BASED ON STATS ##       
    def get_sprite(self):
        if self.hunger < self.max_value * 0.5 and self.happiness < self.max_value * 0.5 and self.energy < self.max_value * 0.5:
            return "pal_neutral.png"
        elif self.hunger < self.max_value * 0.5:
            return "pal_neutral.png"
        elif self.happiness < self.max_value * 0.5:
            return "pal_neutral.png"
        elif self.energy < self.max_value * 0.5:
            return "pal_neutral.png"
        elif self.hunger > self.max_value * 0.7 and self.happiness > self.max_value * 0.7 and self.energy > self.max_value * 0.7:
            return "pal_neutral.png"
        else: 
            return "pal_neutral.png"

class Player:
    def __init__(self, x, y, hp, image, size):
        self.x = x
        self.y = y
        self.hp = hp
        self.image = pygame.image.load("assets/pal_neutral.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.size = size
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

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

class Food:
    def __init__(self, x, y, image, size, hunger_up):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.size = size
        self.hunger_up = hunger_up
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

draw_player = Player(400, 300, 100, "assets/pal_neutral.png", player_size)

draw_food = Food(150, 250,"assets/asset_meat_x8.png", 50, 10)
pal = PixelPal("Pixel", 100, 100, 100, 100)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == tick_event:
            pal.tick()
    
    if pal.is_dead():
        running = False

    screen.fill(WHITE)
    clock.tick(60)
    text = font.render(f"Hunger: {pal.hunger}  Happiness: {pal.happiness}  Energy: {pal.energy}", True, (0, 0, 0))

    screen.blit(text, (10, 10))
    draw_player.movement()
    draw_player.draw(screen)
    draw_food.draw(screen)
    pygame.display.flip()

    if draw_player.rect.colliderect(draw_food):
        pal.feed(draw_food.hunger_up)
        print("Collision detected!")
        draw_food = Food(random.randint(0, screen_width - 50), random.randint(0, screen_height - 50), "assets/asset_meat_x8.png", 50, 10)

pygame.quit()
