from time import perf_counter
from solver import solve_sudoku


def main():
    print("\t\tWelcome to the sudoku solver!\nEnter each row as a string of 9 integers with the following formatting:\n\t- Use a 0 to represent an empty space\n\t- Use a digit from 1-9 to represent that digit in the current square\n\t- Read from left to right along each row.")
    grid = []
    
    for row in range(1, 10):
        curr_row = input(f"Enter row #{row}: ")
        while not (curr_row.isdigit() and len(curr_row) == 9):
            curr_row = input(f"Make sure you inputted a string of 9 integers. Enter row #{row}: ")
        grid.append([int(digit) for digit in curr_row])

    start = perf_counter()
    solved_grid = solve_sudoku(grid)
    end = perf_counter()
    elapsed_ms = (((end - start)*100000)//1)/100

    print(
        f"""
        {[digit for digit in solved_grid[0][0:3]]}|{[digit for digit in solved_grid[0][3:6]]}|{[digit for digit in solved_grid[0][6:9]]}
        {[digit for digit in solved_grid[1][0:3]]}|{[digit for digit in solved_grid[1][3:6]]}|{[digit for digit in solved_grid[1][6:9]]}
        {[digit for digit in solved_grid[2][0:3]]}|{[digit for digit in solved_grid[2][3:6]]}|{[digit for digit in solved_grid[2][6:9]]}
        _____________________________
        {[digit for digit in solved_grid[3][0:3]]}|{[digit for digit in solved_grid[3][3:6]]}|{[digit for digit in solved_grid[3][6:9]]}
        {[digit for digit in solved_grid[4][0:3]]}|{[digit for digit in solved_grid[4][3:6]]}|{[digit for digit in solved_grid[4][6:9]]}
        {[digit for digit in solved_grid[5][0:3]]}|{[digit for digit in solved_grid[5][3:6]]}|{[digit for digit in solved_grid[5][6:9]]}
        _____________________________
        {[digit for digit in solved_grid[6][0:3]]}|{[digit for digit in solved_grid[6][3:6]]}|{[digit for digit in solved_grid[6][6:9]]}
        {[digit for digit in solved_grid[7][0:3]]}|{[digit for digit in solved_grid[7][3:6]]}|{[digit for digit in solved_grid[7][6:9]]}
        {[digit for digit in solved_grid[8][0:3]]}|{[digit for digit in solved_grid[8][3:6]]}|{[digit for digit in solved_grid[8][6:9]]}
        """
    )
    print(f"This sudoku was solved in {elapsed_ms}ms.")


if __name__ == "__main__":
    main()