import random

grid_backend = [["_" for _ in range(10)] for _ in range(10)]
grid_frontend = [["_" for _ in range(10)] for _ in range(10)]
mines = int(input("Enter the number of mines (1-99): "))
def print_backend():
    for row in grid_backend:
        print(row)
    print("--------------------")

def print_frontend():
    for row in grid_frontend:
        print(row)
    print("--------------------")

start_row = int(input("Select starting row (1-10): "))
start_col = int(input("Select starting column (1-10): "))
grid_frontend[start_row-1][start_col-1] = "X"
grid_backend[start_row-1][start_col-1] = "X"

def place_mines(num_mines):
    count = 0
    while count < num_mines:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if grid_backend[row][col] != "M" and grid_frontend[row][col] != "X":
            grid_backend[row][col] = "M"
            count += 1

place_mines(mines) #generate the specified number of mines in the backend grid, avoiding the starting position
print("Generating mines in backend grid...")
#print_backend()#testing
def count_adjacent_mines():
    for row in range(10):
        for col in range(10):
            if grid_backend[row][col] == "M":
                continue
            mine_count = 0
            for r in range(max(0, row-1), min(10, row+2)): #start from one row above the current one but never lower than 0, stop before row+2 so it includes at most current row and one below
                for c in range(max(0, col-1), min(10, col+2)):
                    if grid_backend[r][c] == "M":
                        mine_count += 1
            grid_backend[row][col] = str(mine_count)
count_adjacent_mines() #fill the backend grid with the number of adjacent mines for each cell
print("Counting adjacent mines...")
grid_frontend[start_row-1][start_col-1] = grid_backend[start_row-1][start_col-1] #reveal the starting position adjacent mines in the frontend grid

#reveal area around
def reveal_first_click(col,row):
    for r in range(max(0, row-1), min(10, row+2)):
        for c in range(max(0, col-1), min(10, col+2)):
            if grid_backend[r][c] == "0" and grid_frontend[r][c] == "_":
                grid_frontend[r][c] = grid_backend[r][c]
            elif grid_backend[r][c] == "M":
                continue
            else:
                grid_frontend[r][c] = grid_backend[r][c]
                    

#print_frontend()#testing
reveal_first_click(start_col-1, start_row-1)
#print_frontend()#testing

def reveal():
    available_cells = 0
    for row in grid_frontend:
        for cell in row:
            if cell == "_":
                available_cells += 1 #count the number of unrevealed cells in the frontend grid before the game starts proper
    while True:
        row = int(input("Select row to reveal (1-10): "))
        col = int(input("Select column to reveal (1-10): "))
        if row < 1 or row > 10 or col < 1 or col > 10:
            print("Invalid input. Please select a row and column between 1 and 10.")
            continue
        if grid_frontend[row-1][col-1] != "_":
            print("Cell already revealed. Please select another cell.")
            continue
        if grid_backend[row-1][col-1] == "M":
            print("Game Over! You hit a mine.")
            return False
        else:
            grid_frontend[row-1][col-1] = grid_backend[row-1][col-1]
            available_cells -= 1
            if available_cells == mines:
                print("Congratulations! You have revealed all safe cells.")
                print_frontend() #display the full frontend grid with all revealed cells
                return True
        print_frontend()
        

reveal() #start game