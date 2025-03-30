import subprocess
import sys


def run_linter():
    sys.exit(subprocess.call(["poetry", "run", "pylint", "cv_model/"]))
