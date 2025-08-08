#!/usr/bin/env python3
"""
Тест запуска игры с проверкой инициализации основного цикла.
Останавливает игру сразу после инициализации для проверки работоспособности.
"""

import os
import sys
import pygame
from time import sleep

# Устанавливаем видеодрайвер для headless среды
os.environ['SDL_VIDEODRIVER'] = 'dummy'

def test_game_initialization():
    """Тестирует инициализацию игры без запуска основного цикла."""
    try:
        print("Тестирование инициализации игры...")
        
        # Импорт основного класса игры
        from alien_invasion import AlienInvasion
        
        # Создание объекта игры
        print("- Создание объекта игры...", end=" ")
        game = AlienInvasion()
        print("✓")
        
        # Проверка, что все компоненты инициализированы
        print("- Проверка компонентов:")
        print(f"  • Settings: {'✓' if hasattr(game, 'settings') else '✗'}")
        print(f"  • Screen: {'✓' if hasattr(game, 'screen') else '✗'}")
        print(f"  • Ship: {'✓' if hasattr(game, 'ship') else '✗'}")
        print(f"  • Aliens group: {'✓' if hasattr(game, 'aliens') else '✗'}")
        print(f"  • Bullets group: {'✓' if hasattr(game, 'bullets') else '✗'}")
        print(f"  • Stats: {'✓' if hasattr(game, 'stats') else '✗'}")
        print(f"  • Scoreboard: {'✓' if hasattr(game, 'score_board') else '✗'}")
        print(f"  • Play button: {'✓' if hasattr(game, 'play_button') else '✗'}")
        
        # Проверка звука
        print(f"  • Sound system: {'✓' if hasattr(game, 'sound_enabled') else '✗'}")
        if hasattr(game, 'sound_enabled'):
            print(f"    (Sound enabled: {game.sound_enabled})")
        
        # Проверка количества пришельцев
        alien_count = len(game.aliens.sprites())
        print(f"  • Aliens created: {alien_count} ({'✓' if alien_count > 0 else '✗'})")
        
        # Проверка позиции корабля
        ship_pos = (game.ship.rect.x, game.ship.rect.y)
        print(f"  • Ship position: {ship_pos} ({'✓' if ship_pos[1] > 0 else '✗'})")
        
        pygame.quit()
        
        print("\n🎉 Игра успешно инициализирована!")
        return True
        
    except Exception as e:
        print(f"\n❌ Ошибка при инициализации игры: {e}")
        return False

if __name__ == "__main__":
    print("=== Тест инициализации Alien Invasion ===")
    success = test_game_initialization()
    
    if success:
        print("\nИгра готова к запуску!")
        print("Для полного запуска с GUI используйте: python alien_invasion.py")
    else:
        print("\nОбнаружены проблемы при инициализации игры.")
        sys.exit(1)