import sys

file = sys.argv[1]
start = 50
pwd = 0

with open(file) as f:
    for l in f:
        combo = l.strip()
        direction = combo[0]
        amount = int(combo[1:len(combo)])
        if direction == "L":
            amount = -amount

        end = start + amount

        while (end < 0) | (end > 99):
            if end < 0:
                end += 100
            if end > 99:
                end -= 100

        print_stm = f"{start:3} | {amount:3} | {end:3}"
        if end == 0:
            pwd += 1
            print_stm += "  <-- HIT!!!!!!!"
            print(print_stm)
        else:
            print(print_stm)

        start = end

print(f"The password is {pwd}")
