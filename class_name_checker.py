# class_name_checker.py
from pylint.checkers import BaseChecker

class CreateClassnameChecker(BaseChecker):
    name = 'class-name-checker'
    priority = -1
    msgs = {
        'C9999': (
            'Class name should start with a verb',
            'class-name-should-start-with-verb',
            'Class names should start with a verb.'
        ),
    }

    def visit_classdef(self, node):
        class_name = node.name.lower()
        verbs = ['create', 'initialize', 'generate', 'compute']  # Add more verbs as needed
        if not any(class_name.startswith(verb) for verb in verbs):
            self.add_message('class-name-should-start-with-verb', node=node)

def register(linter):
    linter.register_checker(CreateClassnameChecker(linter))
