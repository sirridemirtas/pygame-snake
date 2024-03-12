import pygame as pg

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Snake")

tile_size = 10
virtual_screen = [SCREEN_WIDTH // tile_size, SCREEN_HEIGHT // tile_size]

snake = [[0, 19], [1, 19], [2, 19], [3, 19]]

def play(snake, direction = "right"):
    snake.pop(0)

    if direction == "left":
        snake.append([snake[-1][0] - 1, snake[-1][1]])
    elif direction == "right":
        snake.append([snake[-1][0] + 1, snake[-1][1]])
    elif direction == "up":
        snake.append([snake[-1][0], snake[-1][1] - 1])
    elif direction == "down":
        snake.append([snake[-1][0], snake[-1][1] + 1])

    return snake

def draw(snake, screen):
    for segment in snake:
        pg.draw.rect(
            screen, (255, 255, 255), (
            segment[0] * tile_size, 
            segment[1] * tile_size,
            tile_size, tile_size))

pg.init()

clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    screen.fill((0, 0, 0))

    snake = play(snake)
    draw(snake, screen)
    
    clock.tick(10)
    
    pg.display.update()
