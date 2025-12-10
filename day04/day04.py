import typer
import copy

app = typer.Typer()


PAPER_ROLL = '@'
SUCCESS = "x"


def make_array_from_file(inputfile: str):
    input_array=[]

    with open(inputfile) as file:
        for line in file:
            next_row = []
            for char in line.strip():
                next_row.append(char.strip())
            input_array.append(next_row)

    return input_array


def get_neighbors(row, col, min_x, max_x, min_y, max_y):
    neighbors = []
    left = False
    right = False
    up = False
    down = False

    # can we go left
    if col - 1 >= min_x:
        left = True

    # can we go right
    if col + 1 <= max_x:
        right = True

    # can we go up
    if row - 1 >= min_y:
        up = True

    # can we go down
    if row + 1 <= max_y:
        down = True

    # UL UM UR
    if up:
        # UM
        neighbors.append([row-1, col])

        # UL
        if left:
            neighbors.append([row-1, col-1])

        # UR
        if right:
            neighbors.append([row-1, col+1])

    # ML XX MR
    if left:
        # ML
        neighbors.append([row, col-1])

    if right:
        # MR
        neighbors.append([row, col+1])


    # DL DM DR
    if down:
        # DM
        neighbors.append([row+1, col])

        if left:
            # DL
            neighbors.append([row+1, col-1])
        if right:
            # DR:
            neighbors.append([row+1, col+1])

    return neighbors


def check_acceptable(array, row, col):

    if array[row][col] != PAPER_ROLL:
        return array[row][col]
    else:

        min_x = 0
        min_y = 0
        max_x = len(array[row]) - 1
        max_y = len(array) - 1

        neighbors = get_neighbors(row, col, min_x, max_x, min_y, max_y)

        adjacent_rolls = 0

        for neighbor in neighbors:
            r, c = neighbor[0], neighbor[1]
            if array[r][c] == PAPER_ROLL:
                adjacent_rolls += 1

        if adjacent_rolls < 4:
            return SUCCESS
        else:
            return PAPER_ROLL

def mark_array_for_removal(array):
    accessible_ct = 0
    marked_array = copy.deepcopy(array)

    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            val = array[i][j]
            return_val = check_acceptable(array, i, j)
            if (val != SUCCESS) & (return_val in [0, 1, 2, 3, SUCCESS]):
                accessible_ct += 1
            marked_array[i][j] = return_val

    return marked_array, accessible_ct



def print_array(array):
    for row in array:
        print("".join([str(val) for val in row]))
    return


@app.command()
def solve_p1(input: str):
    array = make_array_from_file(input)

    print("------------------------- ORIGINAL STATE ------------------------")
    print_array(array)


    marked_array = copy.deepcopy(array)
    accessible_ct = 1
    total_removed = 0

    while accessible_ct > 0:
        marked_array, accessible_ct = mark_array_for_removal(marked_array)
        total_removed += accessible_ct

        print()
        print(f"Remove {accessible_ct} rolls of paper. (Total = {total_removed})")
        print_array(marked_array)

    return total_removed


if __name__ == "__main__":
    app()
