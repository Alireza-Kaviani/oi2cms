import typer
import oi2cms.db.team as team_db
import ruamel.yaml

yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)

app = typer.Typer()

@app.command(name="create")
def create_cms_contest(name: str, description:str = "", teams: str = ""):
    if description == "":
        description = name

    teams = teams.split("|") if not teams == "" else []
    users = []

    for team in teams:
        users = users + team_db.get_users(team)
    
    users = list(set(users))   

    contest_json = {}
    contest_json['name'] = name
    contest_json['description'] = description
    contest_json['users'] = users

    with open('test/contest.yaml', 'w') as f:
        yaml.dump(contest_json, f)
    

@app.command()
def hello():
    print("hi")