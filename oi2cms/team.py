import typer

app = typer.Typer()

@app.command(name="create")
def create_team(name: str):
    pass  

@app.command(name="add")
def add_user(name: str, team: str):
    pass

@app.command()
def hello():
    print("Hello World!")