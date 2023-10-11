import typer
import oi2cms.db.team as team_db

app = typer.Typer()

@app.command(name="create")
def create_team(name: str):
    try:
        team_db.create_team_table(name)
        print("team created successfully")
    except:
       print("Execution Failed")

@app.command(name="add")
def add_user(name: str, team: str):
    try:
        team_db.add_user_to_team(team, name)
    except:
        print("Operation Failed")

@app.command()
def list(team: str):
    print(team_db.get_users(team))