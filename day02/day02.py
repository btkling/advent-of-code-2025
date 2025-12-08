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

def split_string(string, num_pieces):
    # evenly split string into num_pieces
    pieces = []

    for i in range(0, len(string), num_pieces):
        pieces.append(string[0 + i: num_pieces + i])

    return pieces


def is_invalid_id_v2(id):
    # print(f"  -> checking {id}")
    flag = False
    id = str(id)
    slice_len = 1  # start with a slice of length 1
    id_len = len(id)

    while slice_len <= int(id_len / 2):
        # if slice length doesn't evenly divide across the whole string,
        # it's not possible to only repeat on the slice
        if id_len % slice_len == 0:
            sliced_id = split_string(id, slice_len)
            if len(set(sliced_id)) == 1:
                flag = True
            slice_len += 1
        else:
            slice_len += 1

    return flag



def get_invalid_ids(str_range:str):
    start = int(str_range.split("-")[0])
    end = int(str_range.split("-")[1])

    rng_list = range(start, end + 1)
    length = len(rng_list)

    invalid = []

    print(f"range from {start} to {end} has {length} elements")
    for id in rng_list:
        if is_invalid_id_v2(id):
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
        print(sum(all_invalid_ids))
