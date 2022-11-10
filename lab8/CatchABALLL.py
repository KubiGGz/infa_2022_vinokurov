from math import sin, cos
from random import randint
import pygame
from pygame.draw import *

speed_min = 1
speed_max = 5

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLOR = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def collision(obj_db, mouse_butt, mouse_posit):
    """
    Проверяет попадание по объектам из obj_db (обджэкт датабэйз)
    :param obj_db: база данных с объектами
    :param mouse_butt: кнопка мыши, которая была нажата
    :param mouse_posit: массив с координатами мыши в момент нажатия
    :return: обновлённая база данных с объектами
    """
    for i in range(len(obj_db) - 1, -1, -1):
        lenght = (obj_db[i].pos[0] - mouse_posit[0]) ** 2 + (
                    obj_db[i].pos[1] - mouse_posit[1]) ** 2  # померили расстояние до объекта
        mouse_butt += 1
        if lenght <= obj_db[i].rad ** 2:
            global score
            score += obj_db[i].score
            del obj_db[i]
    return obj_db


class Ball:
    def __init__(self, scr):
        """
        Отвечает за создание объекта класса Ball. Создаёт шарик
        :param scr: текущий экран
        """
        self.pos = [randint(100, 1200), randint(100, 700)]
        self.color = COLOR[randint(0, 5)]
        self.angle = randint(0, 359)
        self.screen = scr
        self.speed = randint(speed_min, speed_max)
        self.speed_x = self.speed * cos(self.angle / 57.3)
        self.speed_y = self.speed * sin(self.angle / 57.3)
        self.rad = randint(50, 100)
        self.score = 10

    def move(self, tic):
        """
        Отвечает за обновление координат объекта и соударение со стенками
        :param tic: текущий тик (номер обновления экрана)
        :return: nothing
        """
        self.pos[0] += self.speed_x
        self.pos[1] += self.speed_y
        tic += 1

        if self.pos[0] >= 1500 - self.rad:
            self.angle = randint(90, 270)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)
        if self.pos[0] <= self.rad:
            self.angle = randint(-90, 90)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)

        if self.pos[1] >= 800 - self.rad:
            self.angle = randint(180, 360)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)
        if self.pos[1] <= self.rad:
            self.angle = randint(0, 180)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)

    def draw(self):
        """
        Рисует объект
        :return: nothing
        """
        circle(self.screen, self.color, self.pos, self.rad)


class Square:
    def __init__(self, scr):
        """
        Отвечает за создание объекта класса Square. Создаёт квадратик
        :param scr: текущий экран
        """
        self.pos = [randint(100, 1200), randint(100, 700)]
        self.color = COLOR[randint(0, 5)]
        self.angle = randint(0, 359)
        self.screen = scr
        self.speed = randint(speed_min, speed_max)
        self.speed_x = self.speed * cos(self.angle / 57.3)
        self.speed_y = self.speed * sin(self.angle / 57.3)
        self.rad = randint(50, 100)
        self.score = 50

    def move(self, tic):
        """
        Отвечает за обновление координат объекта и соударение со стенками
        :param tic: текущий тик (номер обновления экрана)
        :return: nothing
        """
        self.pos[0] += self.speed_x
        self.pos[1] += self.speed_y
        if tic % (fps) == 0:
            self.angle = randint(0, 359)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)

        if self.pos[0] >= 1500 - self.rad:
            self.angle = randint(90, 270)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)
        if self.pos[0] <= self.rad:
            self.angle = randint(-90, 90)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)

        if self.pos[1] >= 800 - self.rad:
            self.angle = randint(180, 360)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)
        if self.pos[1] <= self.rad:
            self.angle = randint(0, 180)
            self.speed_x = self.speed * cos(self.angle / 57.3)
            self.speed_y = self.speed * sin(self.angle / 57.3)

    def draw(self):
        """
        Рисует объект
        :return: nothing
        """
        a = [self.pos[0] - self.rad // (2 ** 0.5), self.pos[1] - self.rad // (2 ** 0.5),
             2 * self.rad // (2 ** 0.5), 2 * self.rad // (2 ** 0.5)]
        rect(self.screen, self.color, a)


pygame.init()
pygame.font.init()
fps = 60
screen = pygame.display.set_mode([1500, 800])
pygame.display.update()

finished = False
clock = pygame.time.Clock()
obj = []
tick = 0
score = 0
while not finished:
    clock.tick(fps)
    '''
    Пробегаем циклом for по всем текущим ивентам (по всем текущим событиям pygame).
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == 27:
                finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_button = event.button
            mouse_pos = list(event.pos)
            obj = collision(obj, mouse_button, mouse_pos)
    '''
    Отвечает за создание объектов класса Ball
    '''
    if tick % (1 * fps) == 0:
        obj.append(Ball(screen))
    '''
    Отвечает за создание объектов класса Square
    '''
    if tick % (2 * fps) == 0:
        obj.append(Square(screen))

    screen.fill((222, 120, 203))
    '''
    Отвечает за запуск методов move и draw для всех объектов в базе данных
    '''
    for i in obj:
        i.move(tick)
        i.draw()
    '''
    Отвечает за показ количества очков на экране
    '''
    font = pygame.font.Font(None, 40)
    text = font.render("SCORE:" + str(score), True, (0, 0, 0))
    place = text.get_rect(center=(150, 100))
    screen.blit(text, place)
    pygame.display.update()

    tick += 1
