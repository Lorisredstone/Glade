import subprocess
import os

mypy_command = "mypy main.py"
python_command = "python main.py"

# run mypy with subprocess
p = subprocess.Popen(mypy_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
if p.stdout.read() == b'Success: no issues found in 1 source file\r\n':
    print("Mypy passed ! running python...")
    os.system(python_command)
else:
    print("Mypy failed !")
    os.system(mypy_command)