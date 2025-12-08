import typer

app = typer.Typer()

def get_max_joltage(bank:int):
    # print(f"getting max for {bank}")
    return 0


@app.command()
def get(file_name:str):
    print(file_name)
    with open(file_name) as banks:
        idx = 0
        for bank in banks:
            bank = bank.strip()
            max_j = get_max_joltage(bank)
            print(f"Bank #: {idx:5} = '{bank}'")
            idx += 1
    return


if __name__ == "__main__":
    app()
