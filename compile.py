import subprocess
import os

import mod.colorprint as colorprint

mypy_command = "mypy main.py"
mypy_command = "mypy main.py"
python_command = "python main.py"
gcc_command = "gcc output.c -o output.exe"
run_command = "output.exe"

# run mypy with subprocess
p = subprocess.Popen(mypy_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
if p.stdout is None:
    colorprint.colorprint("Error : couldnt open a subprocess", color = "red")
    exit(1)
if p.stdout.read() == b'Success: no issues found in 1 source file\r\n':
    colorprint.colorprint("Mypy passed for the whole project !", color = "green")
    os.system(python_command)   
    os.system(gcc_command)         
    os.system(run_command)         

else:
    print("Mypy failed !")
    colorprint.colorprint("Mypy failed for the whole project !", color = "red")
    os.system(mypy_command)