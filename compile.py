import subprocess
import os

import mod.colorprint as colorprint

import argparse

parser = argparse.ArgumentParser(description='Lance Glade')
parser.add_argument('-i', dest='input', type=str, help='The input file', required=True)
parser.add_argument('-o', dest='output', type=str, help='The output file', required=True)

args = parser.parse_args()

mypy_command = "mypy main.py"
mypy_command = "mypy main.py"
python_command = f"python main.py {args.input} {args.output}"

# run mypy with subprocess
p = subprocess.Popen(mypy_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
if p.stdout is None:
    colorprint.colorprint("Error : couldnt open a subprocess", color = "red")
    exit(1)
if p.stdout.read() == b'Success: no issues found in 1 source file\r\n':
    colorprint.colorprint("Mypy passed for the whole project !", color = "green")
    os.system(python_command)
else:
    print("Mypy failed !")
    colorprint.colorprint("Mypy failed for the whole project !", color = "red")
    os.system(mypy_command)