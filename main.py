
#from database import connect_database, database_version
from constants import *
import pygame
import os
os.environ["SDL_VIDEODRIVER"]="x11"

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
