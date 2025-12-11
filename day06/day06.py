import typer

app = typer.Typer()


def total_line(ln: list[str]):
    #assume all initial elements are ints
    end = len(ln) - 1
    new_list = ln[:end]

    operator = ln[-1]

    expression = operator.join(new_list)
    result = eval(expression)

    # print(f"applying {operator} to {new_list}")
    # print(f"{expression}")
    # print(f"{eval(expression)}")
    return result


def pivot_list(li: list[list[str]]):
    new_list = []

    #rows = len(li)
    #cols = len(li[0])

    #newrow = col0 from all rows
    #newrow1 = col1 from all rows

    print(f"there are {len(li)} rows to pivot into {len(li[0])} cols")

    for i in range(0, len(li[0])):
        pivoted_row = [row[i] for row in li]
        # print(len(pivoted_row))
        # print(pivoted_row)
        new_list.append(pivoted_row)

    print(f"I have pivoted into {len(new_list)} rows and {len(new_list[0])} cols")
    return new_list

def parse_file(name):
    file_aslist = []
    with open(name) as file:
        for line in file:
            line_list = line.strip().split(" ")
            line_list = [elem for elem in line_list if elem not in ["", " "]]
            # print(line_list)
            file_aslist.append(line_list)

    return file_aslist

@app.command()
def main(file):
    print("hey")
    input = parse_file(file)
    print()
    print(f"input has {len(input)} rows and {len(input[0])} columns")
    print()
    input_pivoted = pivot_list(input)
    print()
    print(f"input_pivoted has {len(input_pivoted)} rows and {len(input_pivoted[0])} columns.")
    print()
    print(sum([total_line(l) for l in input_pivoted]))
    print("hey")

if __name__ == "__main__":
    app()
