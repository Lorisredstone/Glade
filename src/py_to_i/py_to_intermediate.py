from typing import List, Dict, Union, Tuple, Any, Optional
from enum import Enum, IntEnum
import subprocess
import os
import re

from src.py_to_i.lexer import Lexer
import src.py_to_i.py_parser as Py_parser

import mod.colorprint as colorprint
import mod.inter.interlib as Ilib

class LocalTokens(IntEnum):
    INDENT = 0
    DEDENT = 1
    NEWLINE = 2
    EOF = 3
    NAME = 4
    TYPE = 5
    ASSIGN = 6

class Value:
    def __init__(self, value:str):
        self.value:str = value
    def __repr__(self):
        return f"Value({self.value})"

class Pytointermediate:
    def __init__(self, file):
        self.file = file
        
    def py_to_intermediate(self) -> Ilib.Programme:
        # first we test the input file with mypy
        # if it passes, we convert the python file
        mypy_command = f"mypy {self.file}"
        p = subprocess.Popen(mypy_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if p.stdout is None:
            colorprint.colorprint("Error : couldnt open a subprocess", color = "red")
            exit(1)
        if p.stdout.read() == b'Success: no issues found in 1 source file\r\n':
            colorprint.colorprint(f"Mypy passed for {self.file} !", color = "green")
            return self.convert()
        else:
            colorprint.colorprint(f"Mypy failed for {self.file} !", color = "red")
            os.system(mypy_command)
            exit(1)
            
    def convert(self) -> Ilib.Programme:
        # we convert the python file to an intermediate representation
        # we open the input file
        with open(self.file, "r") as f:
            # we read the input file
            raw_content = f.readlines()
        raw_content[-1] = raw_content[-1]+"\n" # beacuse we get eof otherwise
        # we lex it
        lexer = Lexer(raw_content)
        parser = Py_parser.Parser(lexer.run())
        return parser.run()