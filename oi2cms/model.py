class Testcase:
    def __init__(self, subtask, test, input_path = None, output_path = None):
        self.subtask = subtask
        self.test = test
        self.input_path = input_path
        self.output_path = output_path

class Problem:
    def __init__(self, code, name, testcases = []):
        self.code = code
        self.name = name
        self.testcases = testcases
        self.checker = "~/.oi2cms/default.cpp"
