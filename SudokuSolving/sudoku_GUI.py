import pygame
import time
import random

# Initial difficulty level (can be adjusted based on your preference)
current_difficulty = 5

def adjust_difficulty(won):
    global current_difficulty
    if won:
        current_difficulty -= 1  # Decrease difficulty if won
    else:
        current_difficulty += 1  # Increase difficulty if lost

    # Ensure difficulty level stays within reasonable bounds
    current_difficulty = max(1, min(current_difficulty, 9))
    save_difficulty()

def main():
    load_difficulty()
    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540, win)
    key = None
    run = True
    start = time.time()
    strikes = 0
    game_won = False

    while run:
        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_1:
                        key = 1
                    if event.key == pygame.K_2:
                        key = 2
                    if event.key == pygame.K_3:
                        key = 3
                    if event.key == pygame.K_4:
                        key = 4
                    if event.key == pygame.K_5:
                        key = 5
                    if event.key == pygame.K_6:
                        key = 6
                    if event.key == pygame.K_7:
                        key = 7
                    if event.key == pygame.K_8:
                        key = 8
                    if event.key == pygame.K_9:
                        key = 9
                    if event.key == pygame.K_DELETE:
                        board.clear()
                        key = None
                    if event.key == pygame.K_SPACE:
                        board.solve_gui()
                    if event.key == pygame.K_RETURN:
                        i, j = board.selected
                        if board.cubes[i][j].temp != 0:
                            if board.place(board.cubes[i][j].temp):
                                print("Success")
                            else:
                                print("Wrong")
                                strikes += 1
                            key = None
    
    if board.is_finished():
        print("Game over")
        run = False
        adjust_difficulty(won=True)
    if strikes == 3:
        print("Game over")
        run = False
        adjust_difficulty(won=False)


def save_difficulty():
    with open("difficulty.txt", "w") as f:
        f.write(str(current_difficulty))

def load_difficulty():
    global current_difficulty
    try:
        with open("difficulty.txt", "r") as f:
            current_difficulty = int(f.read().strip())
    except FileNotFoundError:
        current_difficulty = 5  # Default difficulty
    

class Grid:
    empty_board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def __init__(self, rows, cols, width, height, win):
        self.rows = rows
        self.cols = cols
        self.generate_board()
        self.width = width
        self.height = height
        self.model = None
        self.update_model()
        self.selected = None
        self.win = win

    def generate_board(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        for _ in range(81 - current_difficulty * 9):
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
            while (self.board, num, (row, col)) or self.board[row][col] != 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
                num = random.randint(1, 9)
            self.board[row][col] = num
        self.cubes = [[Cube(self.board[i][j], i, j, self.width, self.height) for j in range(self.cols)] for i in range(self.rows)]
        self.update_model()
    
class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
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

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128, 128, 128))
            win.blit(text, (x + 5, y + 5))
        elif not(self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))
        
        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)
    
    def set(self, val):
        self.value = val
    
    def set_temp(self, val):
        self.temp = val

main() 