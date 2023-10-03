import os
import shutil
import datetime
import json

from oi2cms.model import Problem

def export_cms(problem:Problem):
    time = datetime.datetime.now()
    name = "{0}-{1}-{2}".format(problem.name, "CMS", 
                                time.strftime("%y-%m-%d-%H-%M-%S"))
    os.mkdir(name)
    problem.testcases.sort(key=lambda testcase: (testcase.subtask, testcase.test))
    export_problem(name, problem)
    export_testcases(name, problem)
    export_checker(name, problem)
    export_subtasks(name, problem)
    shutil.make_archive(name, "zip", name)

def export_problem(path, problem:Problem):
    problem_path = os.path.join(path, "problem.json")
    result = {}
    result["code"] = problem.code
    result["name"] = problem.name
    result["time_limit"] = float(input("Enter time limit (seconds): "))
    result["memory_limit"] = int(input("Enter memory limit (MB): ")) * 1024 * 1024
    result["score_precision"] = 2
    result["task_type"] = "Batch"
    result["task_type_params"] = json.dumps({"task_type_parameters_Batch_compilation":"alone"})
    with open(problem_path, "w") as outfile:
        json.dump(result, outfile)

def export_testcases(path, problem:Problem):
    test_path = os.path.join(path, "tests")
    os.mkdir(test_path)
    for testcase in problem.testcases:
        name = "{0}-{1}".format(testcase.subtask, testcase.test)
        shutil.copyfile(testcase.input_path, os.path.join(test_path, name + ".in"))
        shutil.copyfile(testcase.output_path, os.path.join(test_path, name + ".out"))

def export_checker(path, problem:Problem):
    checker_path = os.path.join(path, "checker")
    os.mkdir(checker_path)
    shutil.copyfile(os.path.expanduser(problem.checker),
                     os.path.join(checker_path, "checker.cpp"))
    shutil.copyfile(os.path.expanduser("~/.oi2cms/testlib.h"),
                     os.path.join(checker_path, "testlib.h"))
    
def export_subtasks(path, problem:Problem):
    subtask_path = os.path.join(path, "subtasks")
    os.mkdir(subtask_path)
    subtasks = []
    for testcase in problem.testcases:
        if(testcase.subtask not in subtasks):
            subtasks.append(testcase.subtask)
    print("Subtask:", subtasks)
    for subtask in subtasks:
        result = {}
        print("Subtask :", subtask)
        result["score"] = int(input("Enter score: "))
        result["testcases"] = []
        included_subtasks = input("Enter included subtasks (separated by ,): ").split(",")
        for testcase in problem.testcases:
            if(testcase.subtask in included_subtasks):
                name = "{0}-{1}".format(testcase.subtask, testcase.test)
                result["testcases"].append(name)
        file_path = os.path.join(subtask_path, subtask + ".json")
        with open(file_path, "w") as outfile:
            json.dump(result, outfile)