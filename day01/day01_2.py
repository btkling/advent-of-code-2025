import sys

def get_pass(file):
    start = 50
    pwd = 0
    with open(filename) as file:
        linenum = 1
        current_pos = start
        for rotation in file:
            rotation = rotation.strip()

            direction = rotation[0]
            rotation_as_int = int(rotation[1:len(rotation)])

            if direction == "L":
                rotation_as_int = -rotation_as_int

            zeros = 0
            while abs(rotation_as_int) > 0:
                # perform one tick of the rotation
                if rotation_as_int < 0:
                    current_pos -= 1
                    rotation_as_int += 1
                else:
                    current_pos += 1
                    rotation_as_int -= 1

                # eval current position
                if (current_pos == 100): 
                    current_pos = 0
                if (current_pos == -1):
                    current_pos = 99
                if current_pos == 0:
                    zeros += 1


            print_stm = f"{linenum:5} | {start:3} + {rotation:>6} -> {current_pos:3}"
            print_stm += f" | HITS: {zeros:3}"
            linenum += 1

            pwd += zeros
            print_stm += f" | PWD: {pwd:5}"
            print(print_stm)

            start = current_pos

    print(f"The password is {pwd}")
    return pwd

if __name__ == "__main__":
    filename = sys.argv[1]
    get_pass(filename)
