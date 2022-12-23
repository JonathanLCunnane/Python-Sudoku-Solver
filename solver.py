def get_col(grid: list[list[int]], colidx: int) -> list[int]:
    return [grid[rowidx][colidx] for rowidx in range(9)]
    

def get_row(grid: list[list[int]], rowidx: int) -> list[int]:
    return grid[rowidx]


def get_square(grid: list[list[int]], rowidx: int, colidx: int) -> list[int]:
    square = []
    for x in range(colidx//3 * 3, colidx//3 * 3 + 3):
        for y in range(rowidx//3 * 3, rowidx//3  * 3 + 3):
            square.append(int(grid[y][x]))
    return square


def has_duplicates(vals: list[int]) -> bool:
    vals = vals.copy()
    original_vals = vals.copy()
    for val in original_vals:
        if val == 0:
            continue
        vals.remove(val)
        if val in vals:
            return True
    return False


def possible_cell_values(grid: list[list[int]]) -> list[list[int]]:
    cell_vals = []
    for rowidx, rowvals in enumerate(grid):
        for colidx, colval in enumerate(rowvals):
            if colval != 0:
                cell_vals.append([-1])
                continue

            possible = set(range(1, 10))

            row_set = set(get_row(grid, rowidx))
            possible -= row_set

            col_set = set(get_col(grid, colidx))
            possible -= col_set

            square = set(get_square(grid, rowidx, colidx))
            possible -= square

            if not possible:
                return False
            cell_vals.append(list(possible))
    return cell_vals


def soln_available(grid: list[list[int]]) -> bool:
    for row in grid:
        if row.count(0) != 0:
            return False
    return True

def is_valid_grid(grid: list[list[int]]) -> bool:
    for idx in range(81):
        row = get_row(grid, idx//9)
        if has_duplicates(row):
            return False
        col = get_col(grid, idx%9)
        if has_duplicates(col):
            return False
        if idx%27 == 0 or (idx - 3)%27 == 0 or (idx - 6)%27 == 0:
            square = get_square(grid, idx%9, idx//9)
            if has_duplicates(square):
                return False
    return True


def solve_sudoku(grid: list[list[int]]) -> list[list[int]]:
    deduction_complete = False
    soln = False
    while not (deduction_complete or soln):
        curr_possible_cell_values = possible_cell_values(grid)
        deduction_complete = True
        for idx, val in enumerate(curr_possible_cell_values):
            if val == [-1]:
                continue
            if len(val) == 1:
                val = val[0] # Unpacking list
                grid[idx//9][idx%9] = val
                deduction_complete = False
        soln = soln_available(grid)
        if soln:
            break
    if soln:
        return grid

    # If the solution cannot be found from direct deduction, 
    # then go through the possible cell values one at a time, 
    # checking each time a value is used if the sudoku is
    # solvable. Using a backtracking/pointer method.
    all_cell_values = possible_cell_values(grid)
    pointeridx = 0
    cell_pointer_idxs = [0] * 81
    solved_cells = 0
    while solved_cells < 81:
        curr_vals = all_cell_values[pointeridx]
        if cell_pointer_idxs[pointeridx] == len(curr_vals):
            if curr_vals != [-1]:
                grid[pointeridx//9][pointeridx%9] = 0
            cell_pointer_idxs[pointeridx] = 0
            cell_pointer_idxs[pointeridx-1] += 1
            pointeridx -= 1
            solved_cells -= 1
            continue
                
        if curr_vals == [-1]:
            pointeridx += 1
            solved_cells += 1
            continue

        grid[pointeridx//9][pointeridx%9] = curr_vals[cell_pointer_idxs[pointeridx]]
        if has_duplicates(get_row(grid, pointeridx//9)):
            cell_pointer_idxs[pointeridx] += 1
        elif has_duplicates(get_col(grid, pointeridx%9)):
            cell_pointer_idxs[pointeridx] += 1
        elif has_duplicates(get_square(grid, pointeridx//9, pointeridx%9)):
            cell_pointer_idxs[pointeridx] += 1
        else:
            solved_cells += 1
            pointeridx += 1
            continue
        
        if cell_pointer_idxs[pointeridx] == len(curr_vals):
            grid[pointeridx//9][pointeridx%9] = 0
            cell_pointer_idxs[pointeridx] = 0
            cell_pointer_idxs[pointeridx-1] += 1
            pointeridx -= 1
            solved_cells -= 1
    return grid