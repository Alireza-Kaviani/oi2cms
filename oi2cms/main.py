import typer

from oi2cms.problem import app as problem_app

app = typer.Typer()
app.add_typer(problem_app, name="problem")

if __name__ == "__main__":
    app()