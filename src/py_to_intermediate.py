from typing import List, Dict, Union, Tuple, Any, Optional
from enum import Enum, IntEnum
import subprocess
import os
import re

from src.intermediate import *

import mod.colorprint as colorprint

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
        
    def py_to_intermediate(self) -> Dict[Any, Any]:
        # first we test the input file with mypy
        # if it passes, we convert the python file
        mypy_command = f"mypy {self.file}"
        p = subprocess.Popen(mypy_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if p.stdout is None:
            colorprint.colorprint("Error : couldnt open a subprocess", color = "red")
            exit(1)
        if p.stdout.read() == b'Success: no issues found in 1 source file\r\n':
            colorprint.colorprint(f"Mypy passed for {self.file} !", color = "green")
            return self.convert().dict()
        else:
            colorprint.colorprint(f"Mypy failed for {self.file} !", color = "red")
            os.system(mypy_command)
            exit(1)
            
    def convert(self) -> IProgramme:
        # we convert the python file to an intermediate representation
        # we open the input file
        with open(self.file, "r") as f:
            # we read the input file
            raw_content = f.readlines()
        raw_content[-1] = raw_content[-1]+"\n" # beacuse we get eof otherwise
        # we lex it
        tokens = self.lexer(raw_content)
        return self.parser(tokens)

    def lexer(self, raw_content:List[str]) -> List[LocalTokens | Value]:
        tokens:List[LocalTokens | Value] = []
        buffer:str = ""
        indent_level:int = 0 # in spaces
        for item in raw_content:
            # first we take into account if we indent/dedent
            indent_actual = len(item) - len(item.lstrip())
            if indent_actual > indent_level:
                tokens.append(LocalTokens.INDENT)
                indent_level = indent_actual
            elif indent_actual < indent_level:
                tokens.append(LocalTokens.DEDENT)
                indent_level = indent_actual
            # then we take into account the rest of the line
            for char in item:
                if char in [" ", "\t"]:
                    if buffer != "":
                        tokens.append(Value(buffer))
                        buffer = ""
                elif char == ":":
                    if buffer != "":
                        tokens.append(Value(buffer))
                        buffer = ""
                    tokens.append(LocalTokens.TYPE)
                elif char == "=":
                    if buffer != "":
                        tokens.append(Value(buffer))
                        buffer = ""
                    tokens.append(LocalTokens.ASSIGN)
                elif char == "\n":
                    if buffer != "":
                        tokens.append(Value(buffer))
                        buffer = ""
                    tokens.append(LocalTokens.NEWLINE)
                else:
                    buffer += char
                    
        tokens.append(LocalTokens.EOF)
        
        return tokens
    
    def parser(self, tokens:List[LocalTokens | Value]) -> IProgramme: # sourcery skip: low-code-quality
        prog = IProgramme([])
        index = 0
        while (token := tokens[index]) != LocalTokens.EOF:
            if isinstance(token, Value):
                index += 1
                continue
            elif token == LocalTokens.ASSIGN:
                # we get the name of the variable
                if index == 0:
                    raise SyntaxError("Unexpected token '=' at the beginning of the line")
                if index > 1: # if there is possibly a type
                    if tokens[index - 2] == LocalTokens.TYPE:
                        name = tokens[index - 3].value
                        var_type = tokens[index - 1].value
                    else:
                        name = tokens[index - 1].value
                        var_type = None
                else: # if there is no type
                    name = tokens[index - 1].value
                    var_type = None
                # now we get the value
                if not isinstance(tokens[index + 1], Value):
                    raise SyntaxError("Unexpected token 'NEWLINE' after '='")
                value = tokens[index + 1].value
                if not isinstance(value, str): raise Exception("BITE") #cant happend, here for mypy
                if not isinstance(name, str): raise Exception("BITE") #cant happend, here for mypy
                if not (isinstance(var_type, str) or var_type is None): raise Exception("BITE") #cant happend, here for mypy

                if var_type is None: # we need to infer the type
                    if value in ["True", "False"]:
                        prog.add_instruction(IAssign(name, IValue(value, ITYPES.BOOL)))
                    elif value.isnumeric():
                        prog.add_instruction(IAssign(name, IValue(value, ITYPES.INT)))
                    elif value[0] == value[-1] and value[0] in ["\"", "'"]:
                        prog.add_instruction(IAssign(name, IValue(value, ITYPES.STRING)))
                    else:
                        raise SyntaxError("Cannot infer the type !")
                else:
                    getITYPE = lambda x : {"int":ITYPES.INT, "bool":ITYPES.BOOL, "str":ITYPES.STRING}[x]
                    try:
                        prog.add_instruction(IAssign(name, IValue(value, getITYPE(var_type))))
                    except KeyError as e:
                        raise SyntaxError(f"Type doesnt exist : {var_type}") from e
                index += 1
                continue
            else:
                index += 1
                continue
        return prog
        
"""
# we only parse thing like `<name>[( ):( )<type>]( )=( )<value>` for now
# we use regex for this
"""