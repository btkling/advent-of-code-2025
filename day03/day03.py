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


@app.command()
def get(file_name:str):
    print(file_name)
    with open(file_name) as banks:
        idx = 0
        jolt_sum = 0
        for bank in banks:
            bank = bank.strip()
            max_j = get_max_joltage(bank)
            print(f"Bank #: {idx:5} = '{bank}' -> max joltage {max_j}")
            idx += 1
            jolt_sum += max_j

        print(jolt_sum)
    return


if __name__ == "__main__":
    app()
