import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Overall class to manager game assets and behavior """
    def __init__(self):
        """ init the game, and create game resources """
        """ 初始化背景設定 """
        pygame.init()
        self.settings = Settings();

        """ 設定遊戲螢幕大小 """
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.game_name)
        # 這裡的 self 指到的是 AlienInvsion instance
        self.ship = Ship(self)

    def run_game(self):
        """ start the main loop for the game """
        while True:
            # Watch for keyboard and mouse events
            # 當按下遊戲視窗的關閉按鈕會偵測到 pygame.QUIT 的產生
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            # pygame 背景色預設為黑色, 此行是幫背景色換顏色
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible
            # display.flip 會更新螢幕讓 pygame 最新繪製的螢幕畫面顯示, 因此當我們在移動時, 會把舊的畫面隱藏, 新的畫面顯示
            pygame.display.flip()

# 當程式被直接執行時, 呼叫 run_game
if __name__ == '__main__':
    # Make the game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
