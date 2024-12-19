import pygame
import sys


def manage_events(ship):
    """
    Обрабатывает события, такие как закрытие окна и нажатие клавиш.
    :param ship: Объект корабля, который нужно обновлять.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если пользователь закрыл окно
            sys.exit()  # Завершаем программу
        elif event.type == pygame.KEYDOWN:  # Если клавиша нажата
            if event.key == pygame.K_RIGHT:  # Если нажата клавиша вправо
                ship.rect.centerx += 1  # Перемещаем корабль вправо


def draw_screen(screen, ship, bg_color):
    """
    Отрисовывает экран с фоном и кораблем.
    :param screen: Объект экрана для отрисовки.
    :param ship: Объект корабля для отрисовки.
    :param bg_color: Цвет фона экрана.
    """
    screen.fill(bg_color)  # Заполняем экран цветом фона
    ship.draw()  # Отрисовываем корабль
    pygame.display.flip()  # Обновляем экран, чтобы отобразить изменения