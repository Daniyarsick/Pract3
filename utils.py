import os
import sys

import pygame


def resource_path(relative_path):
    """Получает абсолютный путь к ресурсу."""
    try:
        # PyInstaller создает временную папку и сохраняет путь к ней в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Если _MEIPASS не существует, используем текущую директорию
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def hide_mouse_cursor():
    """Скрывает курсор мыши на экране."""
    pygame.mouse.set_visible(False)
