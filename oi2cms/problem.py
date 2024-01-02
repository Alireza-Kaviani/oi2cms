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

@app.command(name="usaco-problem")
def export_coci_problem(path:str, checker:str = None):
    name = path.split("/")[-1]
    all_testcases = []
    n_subtasks = int(input("Enter number of subtasks: "))
    for i in range(n_subtasks + 1):
        pattern = input(f"Enter testcases in subtask {i}. (separate ranges by , if needed e.g 1-5,7-10)\n")
        testcases = []
        for test_range in pattern.split(","):
            trange = list(map(int, test_range.split("-")))
            if(len(trange) == 1):
                testcases.append(str(trange[0]))
            else:
                for j in range(trange[0], trange[1] + 1):
                    testcases.append(str(j))
        in_pattern = f"{path}/(?P<test>{'|'.join(testcases)})\\.in"
        out_pattern = f"{path}/(?P<test>{'|'.join(testcases)})\\.out"
        all_testcases += find_specific_subtask(path, str(i), in_pattern, out_pattern)
    problem = Problem(name, name, all_testcases)
    if(checker != None):
        problem.checker = checker
    export_cms(problem)

@app.command()
def hello():
    print("Hello World!")