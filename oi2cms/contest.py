import typer

app = typer.Typer()

@app.command(name="create")
def create_cms_contest(name: str, teams: str = ""):
    pass;  

@app.command()
def hello():
    print("Hello World!")