import sys
import asyncio
import pygame
from constants import *
from logger import *
from player import *
from asteroidfield import AsteroidField
from asteroid import *

async def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 64)
    small_font = pygame.font.Font(None, 32)

    while True:
        result = await run_game(screen, clock)
        if result == "quit":
            return
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    waiting = False
            screen.fill("black")
            game_over_text = font.render("GAME OVER", True, "white")
            restart_text = small_font.render("Press R to restart", True, "white")
            screen.blit(game_over_text, game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 20)))
            screen.blit(restart_text, restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 30)))
            pygame.display.flip()
            clock.tick(60)
            await asyncio.sleep(0)

async def run_game(screen, clock):
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,updatable,drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                return "game_over"
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        await asyncio.sleep(0)

print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    asyncio.run(main())
