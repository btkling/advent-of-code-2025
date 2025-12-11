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



def get_range_bounds(rng: str):
    r_start, r_end = rng.split("-")
    return int(r_start), int(r_end)


def do_ranges_intersect(s1, e1, s2, e2):

    # 1-3 intersects 2-4
    if (s1 <= s2) & (e1 >= s2):
        return True
    # 2-4 intersects 1-3
    if (s1 >= s2) & (s1 <= e2):
        return True
    # 1-4 intersects 2-3
    if (s1 <= s2) & (e1 >= e2):
        return True
    # 2-3 intersects 1-4
    if (s1 >= s2) & (e1 <= e2):
        return True

    return False





def count_fresh_amount(fresh_ranges:list[str]):
    ranges_list = []
    for r in fresh_ranges:
        overlapping_ranges = []
        r_start, r_end = get_range_bounds(r)
        print(f"checking {r_start}-{r_end}")
        # print(f"checking {r_start=}, {r_end=} against {ranges_list}")
        if len(ranges_list) == 0:
            ranges_list.append([r_start, r_end])
        else:
            for rng_to_check in ranges_list:
                s1 = r_start
                e1 = r_end
                s2 = rng_to_check[0]
                e2 = rng_to_check[1]
                if do_ranges_intersect(s1, e1, s2, e2):
                    print(f"  -> {s1}-{e1} overlaps with         {s2}-{e2}")
                    r_start = min(s1, s2)
                    r_end = max(e1, e2)
                    overlapping_ranges.append([s2,e2])
                else:
                    print(f"  -> {s1}-{e1} does not overlap with {s2}-{e2}")

            # print(f"overlapping_ranges are {overlapping_ranges}")
            print(f"  -> removing {overlapping_ranges}")
            ranges_list = [r for r in ranges_list if r not in overlapping_ranges]
            ranges_list.append([r_start, r_end])

    ids = 0
    for r in ranges_list:
        vals = r_end - r_start + 1
        print(f"{r_start:20} - {r_end:20} has {vals:20} ids")
        r_start, r_end = r
        ids += vals

    print(f"total number of ids that are fresh = {ids}")

    return ids


@app.command()
def p2(filename:str):
    fresh_ranges, _ = parse_file(filename)
    count_fresh_amount(fresh_ranges)


@app.command()
def p1(filename:str):
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
