import pygame


bg_color = (0, 0, 0)
x=500
y=100
MAX_X = 500
MAX_Y = 500
game_over = False

move_right = False
move_up = False
move_left = False
move_down = False
IMG_SIZW = 100

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
pygame.display.set_caption('hello man')

# print(pygame.image.get_extended())# проверка на форматы png, jpg

myimages = pygame.image.load('tests/fuckyou.jpg').convert()
myimages = pygame.transform.scale(myimages, (IMG_SIZW,IMG_SIZW))# уменьшить размер картинки

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: #есть кто-то нащл кнопку на клаве то все
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_w:
                move_up = True
            if event.key == pygame.K_s:
                move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_s:
                move_down = False

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos

    if move_left:
        x -= 1
        if x < 0:
            x = 0
    if move_right:
        x += 1
        if x > MAX_X - IMG_SIZW:
            x = MAX_X - IMG_SIZW
    if move_up:
        y -= 1
        if y < 0:
            y = 0
    if move_down:
        y += 1
        if y > MAX_Y - IMG_SIZW:
            y = MAX_Y - IMG_SIZW



    screen.fill(bg_color) # заполнить экран фоном
    screen.blit(myimages, (x, y)) # вывод нашей картинки на экран
    pygame.display.flip()#делает рендаринг и выводит на экран
