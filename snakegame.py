import pygame as pg
import sys as sy
import random as r

pg.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Spaceship(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

class Asteroid(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = r.randrange(WIDTH - self.rect.width)
        self.rect.y = r.randrange(-100, -40)
        self.speed = r.randrange(3, 8)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.y = r.randrange(-100, -40)
            self.rect.x = r.randrange(WIDTH - self.rect.width)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("RPG Space Game")

all_sprites = pg.sprite.Group()
asteroids = pg.sprite.Group()

player = Spaceship()
all_sprites.add(player)

clock = pg.time.Clock()
running = True
shooting = False
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            elif event.key == pg.K_SPACE:
                shooting = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                shooting = False

    all_sprites.update()
    asteroids.update()
    hits = pg.sprite.spritecollide(player, asteroids, False)
    if hits:
        print("Game Over!")
        running = False

    if shooting:
        bullet = Asteroid()
        all_sprites.add(bullet)
        asteroids.add(bullet)

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pg.display.flip()
    clock.tick(FPS)

pg.quit()
sy.exit()
