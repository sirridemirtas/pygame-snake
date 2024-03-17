import pygame as pg

from game_state import GameState
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE

class GameView:
    def __init__(self):
        self.game_state = GameState()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Snake")

    def draw(self, snake):
        for segment in snake:
            pg.draw.rect(
                self.screen,
                (255, 255, 255),
                (segment[0] * TILE_SIZE,
                 segment[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def draw_food(self):
        food = self.game_state.food
        pg.draw.rect(
            self.screen,
            (255, 255, 255),
            (food[0] * TILE_SIZE, food[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def play(self):
        pg.init()
        clock = pg.time.Clock()

        running = True
        while running:
            self.screen.fill((0, 0, 0))

            if self.game_state.status == 0:
                print("Game Over Score:", self.game_state.score)
                self.game_state = GameState()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT:
                        self.game_state.play(
                            self.game_state.Direction.LEFT)
                    elif event.key == pg.K_RIGHT:
                        self.game_state.play(
                            self.game_state.Direction.RIGHT)
                    elif event.key == pg.K_UP:
                        self.game_state.play(
                            self.game_state.Direction.UP)
                    elif event.key == pg.K_DOWN:
                        self.game_state.play(
                            self.game_state.Direction.DOWN)

            self.game_state.play()
            self.draw_food()
            self.draw(self.game_state.snake)

            clock.tick(8)
            pg.display.update()
        pg.quit()
