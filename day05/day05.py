import typer

app = typer.Typer()


def parse_file(filename):

    fresh_ranges = []
    available_ids = []
    completed_fresh = False

    with open(filename) as file:
        for row in file:
            if row.strip() == "":
                completed_fresh = True
            elif not completed_fresh:
                fresh_ranges.append(row.strip())
            else:
                available_ids.append(row.strip())

    return fresh_ranges, available_ids


def is_fresh_lazy(id:int, fresh_ranges:list[str]):
    # lazily find a hit
    match = False
    for r in fresh_ranges:
        r_start, r_end = r.split("-")
        r_start = int(r_start)
        r_end = int(r_end)
        # print(f"  -> checking if {id} between {r_start} and {r_end}")

        if (id >= r_start) & (id <= r_end):
            match = True
            return match
    return match


@app.command()
def solve_p1(filename:str):
    fresh_ranges, available_ids = parse_file(filename)
    
    print("--- FRESH RANGES ---")
    for r in fresh_ranges:
        print(r)

    _ = input("Press [ENTER] to check: ")

    print()
    print("--- AVAILABLE IDS ---")
    ct_fresh = 0
    for i in available_ids:
        if is_fresh_lazy(int(i), fresh_ranges):
            ct_fresh += 1
            print(f"id = {i} is fresh!")
        else: 
            print(f"id = {i}")

    print(f"found {ct_fresh} fresh ingredients")


if __name__ == "__main__":
    app()
