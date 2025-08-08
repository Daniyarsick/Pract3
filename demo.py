#!/usr/bin/env python3
"""
Пример использования и демонстрация ключевых компонентов игры Alien Invasion

Этот файл демонстрирует основные компоненты игры и показывает,
как они взаимодействуют друг с другом.
"""

import os
import sys
import pygame

# Устанавливаем видеодрайвер для headless среды
os.environ['SDL_VIDEODRIVER'] = 'dummy'

def demonstrate_game_components():
    """Демонстрирует создание и использование основных компонентов игры."""
    
    print("=== Демонстрация компонентов игры Alien Invasion ===\n")
    
    # Инициализация pygame
    pygame.init()
    pygame.mixer.quit()  # Отключаем аудио для headless среды
    
    # Создание экрана
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Alien Invasion - Demo')
    
    print("1. Инициализация Settings (настройки игры)")
    from settings import Settings
    settings = Settings()
    print(f"   - Размер экрана: {settings.screen_width}x{settings.screen_height}")
    print(f"   - Скорость корабля: {settings.ship_speed}")
    print(f"   - Скорость пришельцев: {settings.alien_speed}")
    print(f"   - Максимум пуль на экране: {settings.bullets_allowed}")
    
    print("\n2. Создание статистики игры")
    from game_stats import GameStats
    
    # Создаем временный объект для GameStats
    class MockGame:
        def __init__(self):
            self.settings = settings
    
    mock_game = MockGame()
    stats = GameStats(mock_game)
    print(f"   - Начальные жизни: {stats.ships_left}")
    print(f"   - Начальный счет: {stats.score}")
    print(f"   - Начальный уровень: {stats.level}")
    print(f"   - Игра активна: {stats.game_active}")
    
    print("\n3. Демонстрация компонентов корабля")
    from ship import Ship
    
    # Создаем временный объект для Ship
    class MockGameForShip:
        def __init__(self):
            self.screen = screen
            self.settings = settings
    
    mock_ship_game = MockGameForShip()
    
    try:
        ship = Ship(mock_ship_game)
        print(f"   - Позиция корабля: x={ship.rect.x}, y={ship.rect.y}")
        print(f"   - Размер корабля: {ship.rect.width}x{ship.rect.height}")
        print(f"   - Может двигаться влево: {ship.moving_left}")
        print(f"   - Может двигаться вправо: {ship.moving_right}")
    except pygame.error as e:
        print(f"   - Корабль (без изображения): {e}")
    
    print("\n4. Демонстрация системы пуль")
    from bullet import Bullet
    
    try:
        bullet = Bullet(mock_ship_game)
        print(f"   - Размер пули: {settings.bullet_width}x{settings.bullet_height}")
        print(f"   - Цвет пули: {settings.bullet_color}")
        print(f"   - Скорость пули: {settings.bullet_speed}")
    except:
        print("   - Пуля: создана (требует корабль для позиционирования)")
    
    print("\n5. Демонстрация пришельцев")
    from alien import Alien
    
    try:
        alien = Alien(mock_ship_game)
        print(f"   - Скорость пришельца: {settings.alien_speed}")
        print(f"   - Направление флота: {settings.fleet_direction}")
        print(f"   - Скорость опускания флота: {settings.fleet_drop_speed}")
    except pygame.error as e:
        print(f"   - Пришелец (без изображения): {e}")
    
    print("\n6. Демонстрация утилитарных функций")
    from utils import resource_path, hide_mouse_cursor
    
    print(f"   - Путь к ресурсам ship.bmp: {resource_path('images/ship.bmp')}")
    print(f"   - Путь к звуку laser.wav: {resource_path('sounds/laser.wav')}")
    print("   - Функция скрытия курсора: доступна")
    
    print("\n7. Демонстрация цветовой схемы")
    from color import Color
    
    print(f"   - Игровой цвет: {Color.GAME_COLOR}")
    print(f"   - Белый цвет: {Color.WHITE}")
    
    print("\n8. Проверка файлов ресурсов")
    image_files = ['images/ship.bmp', 'images/alien.bmp']
    sound_files = ['sounds/laser.wav', 'sounds/explosion.wav', 'sounds/ship_hit.wav', 'sounds/game_over.wav']
    
    print("   Изображения:")
    for img in image_files:
        exists = "✓" if os.path.exists(img) else "✗"
        print(f"     - {img}: {exists}")
    
    print("   Звуки:")
    for sound in sound_files:
        exists = "✓" if os.path.exists(sound) else "✗"
        print(f"     - {sound}: {exists}")
    
    pygame.quit()
    
    print("\n=== Конец демонстрации ===")
    print("\nИгра 'Alien Invasion' включает в себя:")
    print("• Систему управления кораблем с плавным движением")
    print("• Флот инопланетян с коллективным поведением")
    print("• Систему стрельбы с ограничением количества пуль")
    print("• Систему счета и уровней с возрастающей сложностью")
    print("• Звуковые эффекты для всех игровых событий")
    print("• Визуальное отображение статистики игрока")

def show_game_flow():
    """Показывает примерный flow игры."""
    
    print("\n=== Игровой процесс ===")
    print("1. Запуск игры → появляется кнопка 'Play'")
    print("2. Нажатие 'Play' → начинается игра")
    print("3. Игрок управляет кораблем стрелками ← →")
    print("4. Пробел → выстрел пулей вверх")
    print("5. Попадание в пришельца → +очки, звук взрыва")
    print("6. Уничтожение всех пришельцев → следующий уровень")
    print("7. Столкновение с пришельцем → -жизнь")
    print("8. Закончились жизни → конец игры, показ кнопки 'Play'")

if __name__ == "__main__":
    print("О чем эта игра:")
    print("Alien Invasion - это классическая 2D аркадная игра в стиле Space Invaders.")
    print("Игрок защищает Землю от волн инопланетян, управляя космическим кораблем.\n")
    
    demonstrate_game_components()
    show_game_flow()
    
    print(f"\nДля запуска полной игры выполните:")
    print(f"python alien_invasion.py")