import sys


def is_invalid_id(id:str):
    id = str(id)
    if len(id) % 2 == 1:
        # can't repeat if you have odd number of characters
        return False
    else:
        split = int(len(id) / 2)
        id_b = id[0:split]
        id_a = id[split:len(id)+1]
        if id_a == id_b:
            return True
        else:
            return False


def get_invalid_ids(str_range:str):
    start = int(str_range.split("-")[0])
    end = int(str_range.split("-")[1])

    rng_list = range(start, end + 1)
    length = len(rng_list)

    invalid = []

    print(f"range from {start} to {end} has {length} elements")
    for id in rng_list:
        # print(r)
        if is_invalid_id(id):
            invalid.append(id)
            print(f"  - found invalid id: {id}")

    return invalid

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        line = f.readline()
        all_invalid_ids = []
        for rng in line.split(","):
            new_invalid_ids = get_invalid_ids(rng)
            all_invalid_ids.extend(new_invalid_ids)
        print(all_invalid_ids)
        print(sum(all_invalid_ids))
