import typer

from oi2cms.utils import *
from oi2cms.model import Problem
from oi2cms.export import export_cms

app = typer.Typer()

@app.command(name="coci-problem")
def export_coci_problem(path:str, checker:str = None):
    name = path.split("/")[-1]
    in_pattern = path + "/" + name + "\\.in\\.(?P<subtask>\\d+)(?P<test>\\w+)"
    out_pattern = path + "/" + name + "\\.out\\.(?P<subtask>\\d+)(?P<test>\\w+)"
    testcases = find_testcases(path, in_pattern, out_pattern)
    in_pattern = path + "/" + name + "\\.dummy\\.in\\.(?P<test>\\w+)"
    out_pattern = path + "/" + name + "\\.dummy\\.out\\.(?P<test>\\w+)"
    samples = find_specific_subtask(path, "0", in_pattern, out_pattern)
    all_testcases = testcases + samples
    problem = Problem(name, name, all_testcases)
    if(checker != None):
        problem.checker = checker
    export_cms(problem) #TODO: Add path

@app.command()
def hello():
    print("Hello World!")