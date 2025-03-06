import subprocess
import sys


def run_linter():
    sys.exit(subprocess.call(["poetry", "run", "pylint", "foaimodel/"]))


def run_type_checker():
    sys.exit(subprocess.call(["poetry", "run", "mypy", "foaimodel/"]))


def run_tests():
    sys.exit(subprocess.call(["poetry", "run", "pytest"]))
