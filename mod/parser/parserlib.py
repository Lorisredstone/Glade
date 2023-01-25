from typing import List, Dict, Union, Tuple, Any, Optional
from enum import Enum, IntEnum, auto

import src.py.lexerTokens as Tok

import mod.exceptions as Ex

class Types(Enum):
    REPEAT = auto()

class Expression:
    def __init__(self, type:Types, value:"List[Expression|str]") -> None:
        self.type = type
        self.value = value
        
    def __repr__(self, indent:int=0) -> str:
        return f"Expression({self.type}, {self.value})"

class Line:
    def __init__(self, name:str, content:List[Expression|str]) -> None:
        self.name = name
        self.content = content
    
    def __repr__(self) -> str:
        return f"Line(\"{self.name}\", {self.content})"

class Parser:
    def __init__(self, tokens:List[Tok.Token]):
        self.tokens:List[Tok.Token] = tokens
        self.programme:List[Line] = []

    def run(self) -> None:
        ...
        
    def add_line(self, line:Line) -> None:
        self.programme.append(line)