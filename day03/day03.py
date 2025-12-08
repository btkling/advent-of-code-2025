import typer

app = typer.Typer()

def get_max_joltage(bank:str):
    # print(f"getting max for {bank}")
    max_joltage = 0

    # for each element up to the second to last
    # get the max remaining element and compare to current max jolt
    # replace if higher
    for i in range(0, len(bank) - 1):
        bat1 = int(bank[i])
        for j in range(i+1, len(bank)):
            bat2 = int(bank[j])
            joltage = int(f"{bat1}{bat2}")
            if joltage > max_joltage:
                max_joltage = joltage

    return max_joltage



def get_max_joltage_recursive(bank:str, bats_left:int):
    biggest_bat = 0
    biggest_joltage = ""

    # if you hit the bottom, come back up
    if bats_left == 0:
        return ""

    # get the largest number across the range we have
    for i in range(0, len(bank) - bats_left + 1):
        bat = int(bank[i])
        # print(f"-> iteration {i}, battery = {bat}, bank = {bank}")
        if bat > biggest_bat:
            # recursively check the joltage only if we are seeing a bigger battery than one already checked at this depth
            biggest_bat = bat

            # start with the slice of the bank starting with the battery
            # look for n-1 other batteries
            # print(f"bank_slice for {bat} = {bank[i:len(bank)+1]}")

            # delve and get the joltage of the next layer in
            joltage = (f"{bat}{get_max_joltage_recursive(bank[i+1:], bats_left -1)}")
            # print(f"{' '*i} joltage at index {i}: {joltage}")

            if biggest_joltage == "":
                bj = 0
            else:
                bj = int(biggest_joltage)
            if int(joltage) > int(bj):
                biggest_joltage = joltage
                # print(f"{bat} -> {joltage}")
    return str(biggest_joltage)


@app.command()
def get(file_name:str):
    print("------------------------- START -------------------------")
    with open(file_name) as banks:
        idx = 1
        jolt_sum = 0
        for bank in banks:
            bank = bank.strip()
            max_j = get_max_joltage_recursive(bank, 12)
            print(f"Bank #: {idx:5} = '{bank}' -> max joltage {max_j}")
            idx += 1
            jolt_sum += int(max_j)

        print(jolt_sum)
    print("------------------------- END -------------------------")
    return


if __name__ == "__main__":
    app()
