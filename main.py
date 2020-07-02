import pygame
pygame.font.init()

class Grid:
    board =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def __init__(self, rows, cols, width, height, win):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.model = None
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        #self.update_model()
        self.selected = None
        self.win = win

    def draw(self):
        # Draw grid lines
        gap = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.win, (0, 0, 0), (0, i * gap), (self.width, i * gap), thick)
            pygame.draw.line(self.win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(self.win)

    def solve_gui(self):
        find = find_empty(self.board)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(self.board, i, (row, col)):
                self.board[row][col] = i
                self.cubes[row][col].set(i)
                self.cubes[row][col].draw_change(self.win, True)
                pygame.display.update()
                pygame.time.delay(100)

                if self.solve_gui():
                    return True

                self.board[row][col] = 0
                self.cubes[row][col].set(0)
                self.cubes[row][col].draw_change(self.win, False)
                pygame.display.update()
                pygame.time.delay(100)

        return False


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if not (self.value == 0):
            text = fnt.render(str(self.value), True, (0, 0, 0))
            win.blit(text,(x +  (gap / 2 - text.get_width() / 2), y + gap / 2 - text.get_height() / 2))

    def set(self, val):
        self.value = val

    def draw_change(self, win, g = True):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        pygame.draw.rect(win, (255, 255, 255), (x, y, gap, gap), 0)

        text = fnt.render(str(self.value), True, (0, 0, 0))
        win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + gap / 2 - text.get_height() / 2))

        if g:
            pygame.draw.rect(win, (0, 255, 0), (x, y, gap, gap), 3)
        else:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None


def valid(board, num, pos):
    # Checking the row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Checking the col
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Checking the 3 X 3 box
    box_x = (pos[1] // 3) * 3
    box_y = (pos[0] // 3) * 3

    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if board[i][j] == num and pos != (i, j):
                return False

    return True


def redraw(win, board):
    win.fill((255, 255, 255))
    fnt = pygame.font.SysFont("comicsans", 30)
    start_label = fnt.render("Press Space Bar to start", True, (0, 0, 0))
    win.blit(start_label, (270 - start_label.get_width() / 2, 560))
    #Draw Board
    board.draw()


def main():
    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku Solver")
    board = Grid(9, 9, 540, 540, win)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    board.solve_gui()

        redraw(win, board)
        pygame.display.update()

main()