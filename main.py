import pygame as pg
from enum import Enum

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Snake")

tile_size = 10
virtual_screen = [SCREEN_WIDTH // tile_size, SCREEN_HEIGHT // tile_size]

class Direction(Enum):
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"

def draw_food(food, screen):
    pg.draw.rect(screen, (255, 0, 0), (
        food[0] * tile_size, 
        food[1] * tile_size,
        tile_size, tile_size))

snake = [[0, 19], [1, 19], [2, 19], [3, 19]]

current_direction = Direction.RIGHT

def play(snake, direction = current_direction):
    global current_direction
    snake.pop(0)

    if direction == Direction.LEFT and current_direction != Direction.RIGHT:
        snake.append([snake[-1][0] - 1, snake[-1][1]])
        current_direction = Direction.LEFT
    elif direction == Direction.RIGHT and current_direction != Direction.LEFT:
        snake.append([snake[-1][0] + 1, snake[-1][1]])
        current_direction = Direction.RIGHT
    elif direction == Direction.UP and current_direction != Direction.DOWN:
        snake.append([snake[-1][0], snake[-1][1] - 1])
        current_direction = Direction.UP
    elif direction == Direction.DOWN and current_direction != Direction.UP:
        snake.append([snake[-1][0], snake[-1][1] + 1])
        current_direction = Direction.DOWN

    return snake

def draw(snake, screen):
    for segment in snake:
        pg.draw.rect(
            screen, (4, 4, 4), (
            segment[0] * tile_size, 
            segment[1] * tile_size,
            tile_size, tile_size))

pg.init()

clock = pg.time.Clock()

running = True
while running:
    screen.fill((171, 222, 44))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                play(snake, Direction.LEFT)
            elif event.key == pg.K_RIGHT:
                play(snake, Direction.RIGHT)
            elif event.key == pg.K_UP:
                play(snake, Direction.UP)
            elif event.key == pg.K_DOWN:
                play(snake, Direction.DOWN)
    
    draw_food([10, 10], screen)
    snake = play(snake, current_direction)
    draw(snake, screen)
    
    clock.tick(8)
    
    pg.display.update()
