import pygame

def main():
    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku Solver")
    run = True
    while run:
        for event in pygame.event.get():
            win.fill((255, 255, 255))
            if event.type == pygame.QUIT:
                run = False
            pygame.display.update()

main()