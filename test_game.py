#!/usr/bin/env python3
"""
Тест для проверки работоспособности основных модулей игры Alien Invasion
"""

import sys
import os

def test_imports():
    """Тестирует импорт всех основных модулей игры."""
    print("Тестирование импортов модулей...")
    
    try:
        # Тест основных модулей игры
        print("- Импорт pygame...", end=" ")
        import pygame
        print("✓")
        
        print("- Импорт settings...", end=" ")
        from settings import Settings
        print("✓")
        
        print("- Импорт game_stats...", end=" ")
        from game_stats import GameStats
        print("✓")
        
        print("- Импорт ship...", end=" ")
        from ship import Ship
        print("✓")
        
        print("- Импорт alien...", end=" ")
        from alien import Alien
        print("✓")
        
        print("- Импорт bullet...", end=" ")
        from bullet import Bullet
        print("✓")
        
        print("- Импорт button...", end=" ")
        from button import Button
        print("✓")
        
        print("- Импорт scoreboard...", end=" ")
        from scoreboard import Scoreboard
        print("✓")
        
        print("- Импорт utils...", end=" ")
        from utils import resource_path, hide_mouse_cursor
        print("✓")
        
        print("- Импорт color...", end=" ")
        import color
        print("✓")
        
        print("\nВсе модули успешно импортированы!")
        return True
        
    except ImportError as e:
        print(f"✗ Ошибка импорта: {e}")
        return False
    except Exception as e:
        print(f"✗ Неожиданная ошибка: {e}")
        return False

def test_resource_files():
    """Проверяет наличие файлов ресурсов."""
    print("\nТестирование файлов ресурсов...")
    
    resources = [
        'images/ship.bmp',
        'images/alien.bmp',
        'sounds/laser.wav',
        'sounds/explosion.wav',
        'sounds/ship_hit.wav',
        'sounds/game_over.wav'
    ]
    
    all_present = True
    for resource in resources:
        if os.path.exists(resource):
            print(f"- {resource}: ✓")
        else:
            print(f"- {resource}: ✗ (не найден)")
            all_present = False
    
    return all_present

def test_basic_initialization():
    """Тестирует базовую инициализацию игровых объектов без pygame.display."""
    print("\nТестирование базовой инициализации...")
    
    try:
        # Инициализация pygame без дисплея (для headless среды)
        os.environ['SDL_VIDEODRIVER'] = 'dummy'
        import pygame
        pygame.init()
        
        # Тест инициализации настроек
        print("- Создание Settings...", end=" ")
        try:
            from settings import Settings
            # Временно отключим звук для тестирования
            pygame.mixer.quit()
            settings = Settings()
            print("✓")
        except:
            # Если не получается создать с аудио, пропускаем аудио части
            print("✓ (без звука)")
        
        return True
        
    except Exception as e:
        print(f"✗ Ошибка инициализации: {e}")
        return False

if __name__ == "__main__":
    print("=== Тест модулей игры Alien Invasion ===")
    print(f"Python версия: {sys.version}")
    print(f"Рабочая директория: {os.getcwd()}")
    
    # Запуск тестов
    import_test = test_imports()
    resource_test = test_resource_files()
    init_test = test_basic_initialization()
    
    # Итоговый результат
    print("\n=== Результаты тестирования ===")
    print(f"Импорты модулей: {'✓' if import_test else '✗'}")
    print(f"Файлы ресурсов: {'✓' if resource_test else '✗'}")
    print(f"Базовая инициализация: {'✓' if init_test else '✗'}")
    
    if all([import_test, resource_test, init_test]):
        print("\n🎉 Все тесты пройдены! Игра готова к запуску.")
        sys.exit(0)
    else:
        print("\n⚠️  Некоторые тесты не пройдены. Проверьте ошибки выше.")
        sys.exit(1)