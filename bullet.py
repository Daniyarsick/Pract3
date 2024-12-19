import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления пулями, выпущенными кораблем."""

    def __init__(self, ai_game):
        """Создает объект пули в текущей позиции корабля."""
        super().__init__()
        self.screen = ai_game.screen  # Экран игры
        self.settings = ai_game.settings  # Настройки игры
        self.color = self.settings.bullet_color  # Цвет пули

        # Создаем прямоугольник пули в позиции (0, 0), затем устанавливаем правильную позицию.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop  # Устанавливаем пулю в верхней части корабля

        # Сохраняем позицию пули в виде десятичного числа.
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает пулю вверх по экрану."""
        # Обновляем десятичную позицию пули.
        self.y -= self.settings.bullet_speed
        # Обновляем позицию прямоугольника пули.
        self.rect.y = self.y

    def draw_bullet(self):
        """Отрисовывает пулю на экране."""
        pygame.draw.rect(self.screen, self.color, self.rect)