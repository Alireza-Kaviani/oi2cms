import typer

from oi2cms.problem import app as problem_app
from oi2cms.contest import app as contest_app
from oi2cms.team import app as team_app

app = typer.Typer()
app.add_typer(problem_app, name="problem")
app.add_typer(contest_app, name="contest")
app.add_typer(team_app, name="team")

if __name__ == "__main__":
    app()