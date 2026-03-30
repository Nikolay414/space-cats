import pygame as pg
import random

class Captain(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("space_cat/images/captain.png")
        self.image = pg.transform.scale(self.image,(400,400))

        self.rect = self.image.get_rect()
        self.rect.topleft = (-30,600)

        self.mode = "up"

    def update(self):
        if self.mode == "up":
            self.rect.y -= 3
            if self.rect.y <= 300:
                self.mode = self


class Starship(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("space_cat/images/cat_starship_horizontal.png")
        self.image = pg.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.midleft = (0, 300)

        self.mode = "vertical"
    
    def update(self):
        keys = pg.key.get_pressed()

        if self.mode == "vertical":
            if keys[pg.K_w] and self.rect.y > 0:
                self.rect.y -= 2
            if keys[pg.K_s] and self.rect.bottom < 600:
                self.rect.y += 2

        if self.mode == "horizontal":
            if keys[pg.K_a] and self.rect.x > 0:
                self.rect.x -= 2
            if keys[pg.K_d] and self.rect.x < 700:
                self.rect.x += 2 

    def switch_mode(self):
        self.image = pg.image.load("space_cat/images/cat_starship.png")
        self.image = pg.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()
        self.rect.midbottom = (400, 580)

        self.mode = "horizontal"

class Meteorites(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("space_cat/images/meteorite.png")
        size = random.randint(70, 150)

        self.image = pg.transform.scale(self.image, (size, size))

        self.rect = self.image.get_rect()
        self.rect.topleft = (800, random.randint(0, 600 - size))

        self.speedx = random.randint(1,2)
        self.speedy = random.randint(-2,2)

    def update(self):
        self.rect.x -= self.speedx
        self.rect.y += self.speedy

class Alien (pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("space_cat/images/alien_cat.png")
        self.image = pg.transform.scale(self.image,(400,400))

        self.rect = self.image.get_rect()
        self.rect.topleft = (-30,600)

        self.mode = "up"

    def update(self):
        if self.mode == "up":
            self.rect.y -= 3
            if self.rect.y <= 300:
                self.mode = self

class Mouse_starship(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("space_cat/images/mouse_starship.png")
        size = random.randint(70, 100)

        self.image = pg.transform.scale(self.image, (size, size))

        self.rect = self.image.get_rect()
        self.rect.midbottom = (random.randint(0, 800 - size), 0)

        self.image = pg.transform.flip(self.image, False, True)

        self.speedx = random.randint(-1,1)
        self.speedy = random.randint(1,2)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Laser(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("space_cat/images/laser.png")
        self.image = pg.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = 3
    
    def update(self):
        self.rect.y -= self.speed
