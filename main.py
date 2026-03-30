import pygame as pg
import time
import random
from sprite import Captain, Starship, Meteorites, Alien, Mouse_starship, Laser


def dialoge_mode(sprite, text):
    sprite.update()
    screen.blit(space, (0,0))
    screen.blit(sprite.image, sprite.rect)
    # вывод текста
    text1 = f1.render(text[text_number], True, "white")
    screen.blit(text1,(280,450))
    if text_number < len(text) - 1:
        text2 = f1.render(text[text_number + 1], True, "white")
        screen.blit(text2, (280,470))

pg.init()

# создаем музыку
pg.mixer.music.load("space_cat/sounds/sounds/Tense Intro.wav")
pg.mixer.music.set_volume(0.1)
pg.mixer.music.play(-1)

laser_sound = pg.mixer.Sound("space_cat/sounds/sounds/11377 ice cannon shot.wav")
laser_sound.set_volume(0.1)

win_sound = pg.mixer.Sound("space_cat/sounds/sounds/Victory Screen Appear 01.wav")

size = (800, 600)
screen = pg.display.set_mode(size)
pg.display.set_caption("Космические коты")

# группа спрайтов
meteorites = pg.sprite.Group()
mouse_ship = pg.sprite.Group()
laser = pg.sprite.Group()

# создаем объект 
captain = Captain()
starship = Starship()
alien = Alien()

heart = pg.image.load("space_cat/images/heart.png")
heart = pg.transform.scale(heart, (30, 30))
heart_count = 3


FPS = 120
clock = pg.time.Clock()
is_running = True
mode = "start_scene"


space = pg.image.load("space_cat/images/space.png")
space = pg.transform.scale(space, size)

start_text = ["Мы засекли сигнал с планеты Мур.",
              "",
              "Наши друзья, инопланетные коты,",
              "нуждаются в помощи.",
              "Космические мыши хотят съесть их луну,",
              "потому что она похожа на сыр.",
              "Как долго наш народ страдал от них, ",
              "теперь и муряне в беде...",
              "Мы должны помочь им.",
              "Вылетаем прямо сейчас.",
              "Спасибо, что починил звездолёт, штурман. ",
              "Наконец-то функция автопилота работает.",
              "Поехали!"]

alien_text = ["СПАСИТЕ! МЫ ЕЛЕ ДЕРЖИМСЯ!",
              "",
              "Мыши уже начали грызть луну...",
              "Скоро куски луны будут падать на нас.",
              "Спасите муриан!", ]

final_text = ["Огромное вам спасибо,",
              "друзья с планеты Мяу!",
              "Как вас называть? Мяуанцы? Мяуриане?",
              "В любом случае, ",
              "теперь наша планета спасена!",
              "Мы хотим отблагодарить вас.",
              "Капитан Василий и его штурман получают",
              "орден SKYSMART.",
              "А также несколько бутылок нашей",
              "лучшей валерьянки."
            ]

text_number = 0

f1 = pg.font.Font("space_cat/fonts/FRACTAL.otf", 25)

while is_running:
    # событие
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
        if event.type == pg.KEYDOWN:
            if mode == "start_scene":
                text_number += 2
                if text_number > len(start_text):
                    mode = "meteorites"
                    text_number = 0 
                    start_time = time.time()
            if mode == "alien_scene":
                text_number += 2
                if text_number > len(alien_text):
                    mode = "moon"
                    starship.switch_mode()
                    text_number = 0
                    start_time = time.time()
            if mode == "moon":
                if event.key == pg.K_SPACE:
                    laser.add(Laser(starship.rect.midtop))
                    laser_sound.play()
            if mode == "final_scene":
                text_number += 2
                if text_number >= len(final_text):
                    text_number = 0
                    start_time = time.time()
                    is_running = False



    if mode == "start_scene":
        dialoge_mode(captain, start_text)

    if mode == "meteorites":
        
        chance = random.randint(1,30)
        if time.time() - start_time > 15:

            mode = "alien_scene"
            

        if chance == 1:
            # добовляем в группу спрайтов объект Meteorites
            meteorites.add(Meteorites())
        screen.blit(space,(0,0))
        screen.blit(starship.image, starship.rect)
        for i in range(heart_count):
            screen.blit(heart, (i * 25, 0))



        hits = pg.sprite.spritecollide(starship,meteorites,True)
        for hit in hits:
            heart_count -= 1
            if heart_count <= 0:
                is_running = False

        # вызываем метод draw для группы спрайтов
        meteorites.draw(screen)
        starship.update()

        # вызываем метод update для группы спрайтов
        meteorites.update()
    if mode == "alien_scene":
        dialoge_mode(alien,alien_text)

    if mode == "moon":
        chance = random.randint(1,50)
        if time.time() - start_time > 15:
            mode = "final_scene"
            pg.mixer.music.fadeout(3)
            win_sound.play()
        if chance == 1:
            mouse_ship.add(Mouse_starship())
                
        screen.blit(space,(0,0))
        screen.blit(starship.image, starship.rect)
        mouse_ship.draw(screen)
        starship.update()
        mouse_ship.update()
        laser.update()
        for i in range(heart_count):
            screen.blit(heart, (i * 25, 0))
        hits = pg.sprite.spritecollide(starship,mouse_ship,True)
        pg.sprite.groupcollide(laser,mouse_ship,True,True)
        for hit in hits:
            heart_count -= 1
            if heart_count <= 0:
                is_running = False
        laser.draw(screen)

    if mode == "final_scene":
        dialoge_mode(alien, final_text)
    


    pg.display.flip()
    clock.tick(FPS)