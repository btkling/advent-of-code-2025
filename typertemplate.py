import typer

app = typer.Typer()

@app.command()
def main():
    print("hey")

if __name__ == "__main__":
    main()
