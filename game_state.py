from enum import Enum
import random

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE

class GameState:
    class Direction(Enum):
        RIGHT = "right"
        LEFT = "left"
        UP = "up"
        DOWN = "down"

    def __init__(self):
        self.virtual_screen = [
            SCREEN_WIDTH // TILE_SIZE, 
            SCREEN_HEIGHT // TILE_SIZE]

        self.snake = [[0, 19], [1, 19], [2, 19], [3, 19]]
        self.food = self.create_food()
        self.score = 0

        self.status = 1 # 1: playing, 0: game over

        self.current_direction = self.Direction.RIGHT

    def update_snake_positon(self, x_change, y_change):
        if self.snake[-1][0] + x_change < 0:
            x_change = self.virtual_screen[0] - 1
        elif self.snake[-1][0] + x_change >= self.virtual_screen[0]:
            x_change = -self.virtual_screen[0] + 1
        elif self.snake[-1][1] + y_change < 0:
            y_change = self.virtual_screen[1] - 1
        elif self.snake[-1][1] + y_change >= self.virtual_screen[1]:
            y_change = -self.virtual_screen[1] + 1
        
        self.snake.append(
            [self.snake[-1][0] + x_change,
            self.snake[-1][1] + y_change])
        self.snake.pop(0)

    def play(self, direction=None):
        if direction is None:
            direction = self.current_direction

        if (direction == self.Direction.LEFT
            and self.current_direction != self.Direction.RIGHT):
            self.update_snake_positon(-1, 0)
            self.current_direction = self.Direction.LEFT
        elif (direction == self.Direction.RIGHT
            and self.current_direction != self.Direction.LEFT):
            self.update_snake_positon(1, 0)
            self.current_direction = self.Direction.RIGHT
        elif (direction == self.Direction.UP
            and self.current_direction != self.Direction.DOWN):
            self.update_snake_positon(0, -1)
            self.current_direction = self.Direction.UP
        elif (direction == self.Direction.DOWN
            and self.current_direction != self.Direction.UP):
            self.update_snake_positon(0, 1)
            self.current_direction = self.Direction.DOWN

        if self.check_self_collision():
            self.status = 0

        if self.check_food_collision():
            self.snake.insert(0, self.food)
            self.food = self.create_food()
        return self.snake

    def check_self_collision(self):
        head = self.snake[-1]
        if (head[0] < 0
            or head[0] >= self.virtual_screen[0]
            or head[1] < 0
            or head[1] >= self.virtual_screen[1]):
            return True

        for segment in self.snake[:-1]: # check all segments except the head
            if head == segment:
                return True
        return False

    def check_food_collision(self):
        if self.snake[-1] == self.food:
            self.snake.insert(0, self.food)
            self.score += 1
            return True
        return False

    def create_food(self):
        while True:
            x = random.randint(0, self.virtual_screen[0] - 1)
            y = random.randint(0, self.virtual_screen[1] - 1)
            position = [x, y]
            if position not in self.snake:
                return position
