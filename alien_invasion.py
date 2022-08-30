import sys, pygame


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.screen = pygame.display.set_mode((2200, 1300))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            """Отслеживание событийклавиатуры и мыши"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # отображение последнего прорисованного экрана
            pygame.display.flip()



if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
