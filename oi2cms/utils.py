import os
import re

from oi2cms.model import Problem, Testcase

def add_testcase(testcases, subtask, test, input_path, output_path):
    flag = False
    for testcase in testcases:
        if(testcase.subtask == subtask and testcase.test == test):
            if(input_path != None):
                testcase.input_path = input_path
            if(output_path != None):
                testcase.output_path = output_path
            flag = True
    if(not flag):
        testcases.append(Testcase(subtask, test, input_path, output_path))

def find_testcases(path, in_pattern, out_pattern):
    testcases = []
    in_prog = re.compile(in_pattern)
    out_prog = re.compile(out_pattern)
    for dir, folders, files in os.walk(path):
        for filename in files:
            path = os.path.join(dir, filename)
            in_result = in_prog.match(path)
            out_result = out_prog.match(path)
            if(in_result != None):
                subtask = in_result.group("subtask")
                test = in_result.group("test")
                add_testcase(testcases, subtask, test, path, None)
            if(out_result != None):
                subtask = out_result.group("subtask")
                test = out_result.group("test")
                add_testcase(testcases, subtask, test, None, path)
    for testcase in testcases:
        print(testcase.subtask, testcase.test, testcase.input_path, testcase.output_path)
    return testcases

def find_specific_subtask(path, subtask, in_pattern, out_pattern):
    testcases = []
    in_prog = re.compile(in_pattern)
    out_prog = re.compile(out_pattern)
    for dir, folders, files in os.walk(path):
        for filename in files:
            path = os.path.join(dir, filename)
            in_result = in_prog.match(path)
            out_result = out_prog.match(path)
            if(in_result != None):
                test = in_result.group("test")
                add_testcase(testcases, subtask, test, path, None)
            if(out_result != None):
                test = out_result.group("test")
                add_testcase(testcases, subtask, test, None, path)
    for testcase in testcases:
        print(testcase.subtask, testcase.test, testcase.input_path, testcase.output_path)
    return testcases