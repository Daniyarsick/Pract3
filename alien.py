import os
import sys

import pygame
from pygame.sprite import Sprite

from utils import resource_path


class Alien(Sprite):
    """Класс, представляющий пришельца в игре."""

    def __init__(self, game):
        """Инициализирует пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = game.screen  # Экран игры
        self.settings = game.settings  # Настройки игры

        # Загрузка изображения
        self.image = pygame.image.load(resource_path("images/alien.bmp"))
        self.rect = self.image.get_rect()

        # Устанавливаем начальную позицию пришельца в верхнем левом углу экрана.
        self.rect.x = self.rect.width  # Отступ слева
        self.rect.y = self.rect.height  # Отступ сверху

        # Сохраняем точное горизонтальное положение пришельца.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана."""
        screen_rect = self.screen.get_rect()  # Получаем прямоугольник экрана
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True  # Пришелец достиг края экрана

    def update(self):
        """Перемещает пришельца влево или вправо."""
        # Обновляем горизонтальную позицию с учетом скорости и направления флота
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x  # Применяем изменение к прямоугольнику пришельца