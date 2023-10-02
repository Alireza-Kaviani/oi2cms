import typer

app = typer.Typer()

@app.command(name="coci-problem")
def export_coci_problem(path:str="."):
    print(path)

@app.command()
def hello():
    print("Hello World!")