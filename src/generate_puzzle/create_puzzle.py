import random


def main():
    grid = create_puzzle()
    print(grid)


def create_puzzle():
    grid = [[0 for i in range(0, 9)] for j in range(0, 9)]
    generate_solution(grid)
    return grid


def generate_solution(grid):
    num_list = [i for i in range(1,10)]
    for i in range(0,81):
        row = i//9
        col = i%9
        if grid[row][col] == 0:
            random.shuffle(num_list)
            for num in num_list:
                if valid_location(grid, row, col, num):
                    grid[row][col] = num
                    if not find_empty_square(grid):
                        return True
                    else:
                        if generate_solution(grid):
                            return True
            break
    grid[row][col] = 0
    return False
        

def valid_location(grid, row, col, number):
    numCols = len(grid[0])
    numRows = len(grid)
    for i in range(0, numCols):
        currentCol = (col+i)%(numCols-1)
        if grid[row][currentCol] == number:
            return False
    for i in range(0, numRows):
        currentRow = (row+i)%(numRows-1)
        if grid[currentRow][col] == number:
            return False
    return True


def find_empty_square(grid):
    numCols = len(grid[0])
    numRows = len(grid)
    for i in range(0, numCols):
        for j in range(0, numRows):
            if grid[i][j] == 0:
                return True
    return False


def non_empty_squares(grid):
    non_empty = []
    numCols = len(grid[0])
    numRows = len(grid)
    for i in range(0, numCols):
        for j in range(0, numRows):
            if grid[i][j] != 0:
                non_empty.append((i, j))
    return non_empty


if __name__ == "__main__":
    main()
