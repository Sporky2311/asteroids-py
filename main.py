
#from database import connect_database, database_version
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import pygame, sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    #create Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #assign player to the Groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    #init player
    player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    field = AsteroidField()
    #Game loop
    while True:
        #allows player to Quit by clicking the X on the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #update the player object
        updatable.update(dt)
        #fill the screen with black
        screen.fill("black")
        #draw the player on the screen
        for entity in drawable:
            entity.draw(screen)
        for asteroid in asteroids:
            if(asteroid.collision(player1)):
                print("Game Over!")
                sys.exit()
        pygame.display.flip()
        #"calculate" delta Time
        dt = clock.tick(60) / 1000

        

if __name__ == "__main__":
    main()
