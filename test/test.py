import arcade
import random
from path import ROOT_DIR

# Set the dimensions of the game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set the dimensions of the player sprite
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

# Set the dimensions of the coin sprite
COIN_WIDTH = 25
COIN_HEIGHT = 25

# Set the dimensions of the obstacle sprite
OBSTACLE_WIDTH = 75
OBSTACLE_HEIGHT = 75

MOVEMENT_SPEED = 5

class Player(arcade.Sprite):
    def __init__(self, x, y , window):
        super().__init__(ROOT_DIR / "player.png", 0.5)
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0
        self._window = window

    def update(self):
        if arcade.key.LEFT in self._window.keys_pressed:
            self.change_x = -MOVEMENT_SPEED
        elif arcade.key.RIGHT in self._window.keys_pressed:
            self.change_x = MOVEMENT_SPEED
        else:
            self.change_x = 0

        if arcade.key.UP in self._window.keys_pressed:
            self.change_y = MOVEMENT_SPEED
        elif arcade.key.DOWN in self._window.keys_pressed:
            self.change_y = -MOVEMENT_SPEED
        else:
            self.change_y = 0

        self.center_x += self.change_x
        self.center_y += self.change_y

class Coin(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__(ROOT_DIR / 'coin.png', 0.5)
        self.center_x = center_x
        self.center_y = center_y

class Obstacle(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__(ROOT_DIR / 'obstacle.png', 0.5)
        self.center_x = center_x
        self.center_y = center_y

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "My Arcade Game")
        self.player = None
        self.coins = None
        self.obstacles = None
        self.score = 0
        self.keys_pressed = []
        self.frame_count = 0

    def setup(self):
        self.player = Player(SCREEN_WIDTH // 2,SCREEN_HEIGHT // 2, self)
        self.coins = arcade.SpriteList()
        self.obstacles = arcade.SpriteList()

        # Create 10 coins at random locations
        for i in range(10):
            coin = Coin(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
            self.coins.append(coin)

        # Create 5 obstacles at random locations
        for i in range(5):
            obstacle = Obstacle(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
            self.obstacles.append(obstacle)
    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.coins.draw()
        self.obstacles.draw()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 14)

    def update(self, delta_time):
        self.frame_count += 1
        print((arcade.get_fps()))
        self.player.update()
        self.coins.update()
        self.obstacles.update()

        coin_hit_list = arcade.check_for_collision_with_list(self.player, self.coins)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        obstacles_hit = arcade.check_for_collision_with_list(self.player, self.obstacles)
        if obstacles_hit:
            arcade.close_window()

    def on_key_press(self, key, modifiers):
        if key not in self.keys_pressed:
            self.keys_pressed.append(key)

    def on_key_release(self, key, modifiers):
        if key in self.keys_pressed:
            self.keys_pressed.remove(key)


def main():
    arcade.enable_timings()
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()