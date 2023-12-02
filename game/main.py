from pygame import *
from time import sleep
from math import floor
class GameSprite(sprite.Sprite):
    def __init__(self, x, y, image_sprite, size=(80, 100)):
        self.size = size
        self.image_sprite = image_sprite
        super().__init__()
        self.image = transform.scale(image.load(self.image_sprite), self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

    def render(self):
        self.image = transform.scale(image.load(self.image_sprite), self.size)
        window.blit(self.image, (self.x, self.y))


class Ckicker(GameSprite):
    def podarok_cur_pos(self, mouse_pos):

        if (mouse_pos[0] >= self.rect.x and mouse_pos[0] <= self.rect.bottomright[0]
                and mouse_pos[1] >= self.rect.y and mouse_pos[1] <= self.rect.bottomright[1]):
            if self.size != (284, 284):
                for i in range(15):
                    self.size = (256 + i * 2, 256 + i * 2)
                    self.x, self.y = 80 - i, 250 - i
                    self.render()
                    display.update()
                    sleep(0.006)
            self.render()

        else:
            self.size = (256, 256)
            self.x, self.y = 80, 250
            self.render()

    def update(self, mouse_pos, any_money):
        global money

        if (mouse_pos[0] > self.rect.x and mouse_pos[0] < self.rect.bottomright[0]
                and mouse_pos[1] > self.rect.y and mouse_pos[1] < self.rect.bottomright[1]):
            money += any_money
            podarokclick.play()
            self.size = (256, 256)
            self.x, self.y = 80, 250
            self.render()
            display.update()
            sleep(0.006)


def mouse_clicked_rect(mouse_pos, rect):
    if mouse_pos[0] > rect.x and mouse_pos[0] < rect.bottomright[0] and mouse_pos[1] > rect.y and mouse_pos[1] < \
            rect.bottomright[1]:
        a = True
    else:
        a = False
    return a


def mega_render(object_game, rect, rect_outline, rect_button):
    if object_game.y >= 140 and object_game.y <= 670:
        draw.rect(window, (0, 0, 0), rect_outline)
        draw.rect(window, (45, 15, 95), rect)
        draw.rect(window, (0, 150, 0), rect_button)
        object_game.render()


def store_move_def(i, object_game, rect, rect_outline, rect_button):
    any_move = 130
    object_game.y += i * any_move
    rect_outline.move_ip(0, i * any_move)
    rect.move_ip(0, i * any_move)
    rect_button.move_ip(0, i * any_move)


font.init()


def draw_text(x: object, y: object, string: object, col: object, size: object, window: object) -> object:
    font1 = font.SysFont("bahnschrift", size)
    text = font1.render(string, True, col)
    textbox = text.get_rect()
    textbox.center = (x, y)
    window.blit(text, textbox)


magnitudeDict={0:'', 1:'K', 2:'M', 3:'B', 4:'T', 5:'Qd', 6:'Qn', 7:'Sx', 8:'Sp', 9:'Oc', 10:'Nl', 11:'Dc'}
def simplify(num):
    num=floor(num)
    magnitude=0
    while num>=1000.0:
        magnitude+=1
        num=num/1000.0
    return(f'{floor(num*100.0)/100.0} {magnitudeDict[magnitude]}')

money = 987527502570
money_text = simplify(money)
money_ps = 0
height = 800
width = 1200

window = display.set_mode((width, height))
window.fill((0, 102, 0))
display.set_caption("santa_tycoon")

mixer.init()
mixer.music.load("fon_music.mp3")
mixer.music.play()
button = mixer.Sound('button.mp3')
podarokclick = mixer.Sound('podarokclick.mp3')

walls = sprite.Group()
for i in range(8):
    wall = GameSprite(400, i * 100, 'wall.png', (256, 200))
    walls.add(wall)
for i in range(8):
    wall = GameSprite(900, i * 100, 'wall.png', (256, 200))
    walls.add(wall)
for i in range(12):
    wall = GameSprite(i * 100, 100, 'rotate_wall.png', (256, 200))
    walls.add(wall)

# STORE
lavanda_fon = Rect(930, 120, 300, 700)
button_up = GameSprite(875, 128, 'button_up.png', (50, 50))
button_down = GameSprite(875, 750, 'button_down.png', (50, 50))

# COOOOOOOKE
rect_cooke = Rect(945, 140, 250, 120)
rect_cooke_outline = Rect(942, 137, 256, 126)
button_cooke = Rect(1085, 160, 80, 80)
cooke = GameSprite(955, 150, 'cooke.png', (80, 100))
# PODAROK_RED
rect_podarok_red = Rect(945, 270, 250, 120)
rect_podarok_red_outline = Rect(942, 267, 256, 126)
button_podarok_red = Rect(1085, 290, 80, 80)
podarok_red = GameSprite(955, 280, 'podarok_red.png', (80, 100))
# LED
rect_led = Rect(945, 400, 250, 120)
rect_led_outline = Rect(942, 397, 256, 126)
button_led = Rect(1085, 420, 80, 80)
led = GameSprite(955, 410, 'led.png', (80, 100))
# PODAROK_BLUE
rect_podarok_blue = Rect(945, 530, 250, 120)
rect_podarok_blue_outline = Rect(942, 527, 256, 126)
button_podarok_blue = Rect(1085, 550, 80, 80)
podarok_blue = GameSprite(955, 540, 'podarok_blue.png', (80, 100))
# DED_MOROZ
rect_ded_moroz = Rect(945, 660, 250, 120)
rect_ded_moroz_outline = Rect(942, 657, 256, 126)
button_ded_moroz = Rect(1085, 680, 80, 80)
ded_moroz = GameSprite(955, 670, 'ded_moroz.png', (80, 100))
# CASTLE
rect_castle = Rect(945, 790, 250, 120)
rect_castle_outline = Rect(942, 787, 256, 126)
button_castle = Rect(1085, 810, 80, 80)
castle = GameSprite(955, 800, 'castle.png', (80, 100))
# ROCKET
rect_rocket = Rect(945, 920, 250, 120)
rect_rocket_outline = Rect(942, 917, 256, 126)
button_rocket = Rect(1085, 940, 80, 80)
rocket = GameSprite(955, 930, 'rocket.png', (80, 100))
# UNIVERSITY
rect_university = Rect(945, 1050, 250, 120)
rect_university_outline = Rect(942, 1047, 256, 126)
button_university = Rect(1085, 1070, 80, 80)
university = GameSprite(955, 1060, 'university.png', (80, 100))
# clicker
podarok_click = Ckicker(80, 250, 'podarok_click.png', (256, 256))
game = True
FPS = 60
clock = time.Clock()
wait = 0
store_move = 1
# TYCOON
cooke_tycoon_money = 0
podarok_red_tycoon_money = 0
led_tycoon_money = 0
podarok_blue_tycoon_money = 0
ded_moroz_tycoon_money = 0
castle_tycoon_money = 0
rocket_tycoon_money = 0
university_tycoon_money = 0
while game:
    window.fill((0, 102, 0))
    draw.rect(window, (181, 165, 213), lavanda_fon)
    button_up.render()
    button_down.render()
    walls.draw(window)

    mega_render(cooke, rect_cooke, rect_cooke_outline, button_cooke)
    mega_render(podarok_red, rect_podarok_red, rect_podarok_red_outline, button_podarok_red)
    mega_render(led, rect_led, rect_led_outline, button_led)
    mega_render(podarok_blue, rect_podarok_blue, rect_podarok_blue_outline, button_podarok_blue)
    mega_render(ded_moroz, rect_ded_moroz, rect_ded_moroz_outline, button_ded_moroz)
    mega_render(castle, rect_castle, rect_castle_outline, button_castle)
    mega_render(rocket, rect_rocket, rect_rocket_outline, button_rocket)
    mega_render(university, rect_university, rect_university_outline, button_university)

    money_text = simplify(money)
    draw_text(200, 50, "Money:" + str(money_text), (255, 255, 255), 50, window)
    draw_text(200, 100, "Money (second):" + str(money_ps), (255, 255, 255), 30, window)
    draw_text(685, 60, "New Year's tycoon", (255, 255, 255), 55, window)
    draw_text(1070, 60, "Store", (255, 255, 255), 55, window)

    draw_text(510, 160, "Сookie:" + str(cooke_tycoon_money), (160, 255, 160), 25, window)
    draw_text(547, 190, "Podarok(red):" + str(podarok_red_tycoon_money), (160, 255, 160), 25, window)
    draw_text(494, 220, "Led:" + str(led_tycoon_money), (160, 255, 160), 25, window)
    draw_text(552, 250, "Podarok(blue):" + str(podarok_blue_tycoon_money), (160, 255, 160), 25, window)
    draw_text(533, 280, "Ded Moroz:" + str(ded_moroz_tycoon_money), (160, 255, 160), 25, window)
    draw_text(506, 310, "Сastle:" + str(castle_tycoon_money), (160, 255, 160), 25, window)
    draw_text(510, 340, "Rocket:" + str(rocket_tycoon_money), (160, 255, 160), 25, window)
    draw_text(527, 370, "University:" + str(university_tycoon_money), (160, 255, 160), 25, window)

    mouse_pos = mouse.get_pos()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            podarok_click.update(mouse_pos, 1)

            if mouse_clicked_rect(mouse_pos, button_down.rect):
                if university.y > 670:
                    button.play()
                    store_move_def(store_move * -1, cooke, rect_cooke, rect_cooke_outline, button_cooke)
                    store_move_def(store_move * -1, podarok_red, rect_podarok_red, rect_podarok_red_outline, button_podarok_red)
                    store_move_def(store_move * -1, led, rect_led, rect_led_outline, button_led)
                    store_move_def(store_move * -1, podarok_blue, rect_podarok_blue, rect_podarok_blue_outline, button_podarok_blue)
                    store_move_def(store_move * -1, ded_moroz, rect_ded_moroz, rect_ded_moroz_outline, button_ded_moroz)
                    store_move_def(store_move * -1, castle, rect_castle, rect_castle_outline, button_castle)
                    store_move_def(store_move * -1, rocket, rect_rocket, rect_rocket_outline, button_rocket)
                    store_move_def(store_move * -1, university, rect_university, rect_university_outline, button_university)

            if mouse_clicked_rect(mouse_pos, button_up.rect):
                if cooke.y <= 140:
                    button.play()
                    store_move_def(store_move, cooke, rect_cooke, rect_cooke_outline, button_cooke)
                    store_move_def(store_move, podarok_red, rect_podarok_red, rect_podarok_red_outline, button_podarok_red)
                    store_move_def(store_move, led, rect_led, rect_led_outline, button_led)
                    store_move_def(store_move, podarok_blue, rect_podarok_blue, rect_podarok_blue_outline, button_podarok_blue)
                    store_move_def(store_move, ded_moroz, rect_ded_moroz, rect_ded_moroz_outline, button_ded_moroz)
                    store_move_def(store_move, castle, rect_castle, rect_castle_outline, button_castle)
                    store_move_def(store_move, rocket, rect_rocket, rect_rocket_outline, button_rocket)
                    store_move_def(store_move, university, rect_university, rect_university_outline, button_university)

            if mouse_clicked_rect(mouse_pos, button_cooke) and money >= 15:
                money -= 15
                cooke_tycoon_money += 1
                money_ps += 1
                button.play()
            if mouse_clicked_rect(mouse_pos, button_podarok_red) and money >= 100:
                money -= 100
                podarok_red_tycoon_money += 1
                money_ps += 10
                button.play()
            if mouse_clicked_rect(mouse_pos, button_led) and money >= 400:
                money -= 400
                led_tycoon_money += 1
                money_ps += 40
                button.play()
            if mouse_clicked_rect(mouse_pos, button_podarok_blue) and money >= 1000:
                money -= 1000
                podarok_blue_tycoon_money += 1
                money_ps += 100
                button.play()
            if mouse_clicked_rect(mouse_pos, button_ded_moroz) and money >= 10000:
                money -= 10000
                ded_moroz_tycoon_money += 1
                money_ps += 1000
                button.play()
            if mouse_clicked_rect(mouse_pos, button_castle) and money >= 100000:
                money -= 100000
                castle_tycoon_money += 1
                money_ps += 10000
                button.play()
            if mouse_clicked_rect(mouse_pos, button_rocket) and money >= 10000000:
                money -= 10000000
                rocket_tycoon_money += 1
                money_ps += 100000
                button.play()
            if mouse_clicked_rect(mouse_pos, button_university) and money >= 1000000000:
                money -= 1000000000
                university_tycoon_money += 1
                money_ps += 123456789123456789
                button.play()


    if wait >= 45:
        money += podarok_red_tycoon_money * 10
        money += cooke_tycoon_money * 1
        money += led_tycoon_money * 40
        money += podarok_blue_tycoon_money * 100
        money += ded_moroz_tycoon_money * 1000
        money += castle_tycoon_money * 10000
        money += rocket_tycoon_money * 100000
        money += university_tycoon_money * 123456789123456789
        wait = 0

    podarok_click.podarok_cur_pos(mouse_pos)
    clock.tick(FPS)
    display.update()
    wait += 1