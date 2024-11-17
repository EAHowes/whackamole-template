import pygame
import random

def rand_mole_pos():
    rand_x = random.randrange(0, 20)
    rand_y = random.randrange(0, 16)
    return (rand_x, rand_y)

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        grid = 32
        mole_position = (0,0)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    #map to the grid
                    grid_x = x // grid
                    grid_y = y // grid
                    click_position = (grid_x, grid_y)
                    if click_position == mole_position:
                        mole_position = rand_mole_pos()

                    

            screen.fill("pink")

            #line drawing
            for i in range(32, 32 * 21, 32):
                pygame.draw.line(screen, "black", (i, 0), (i, 512))
            for i in range(32, 32 * 17, 32):
                pygame.draw.line(screen, "black", (0, i), (640, i))

            #mole drawing:
            mole_pixel_position = (mole_position[0] * grid, mole_position[1] * grid)
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_pixel_position)))

            
            
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
