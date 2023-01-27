from typing import List, Dict, Union, Tuple, Any, Optional
from enum import Enum, IntEnum, auto

import src.py.lexerTokens as Tok

import mod.exceptions as Ex
import mod.inter.interlib as Ilib

class Types(Enum):
    # Element types
    LATER_DEFINED = auto()
    
class Expression:
    def __init__(self, type:Types, value:"List[Expression|Tok.Token]|str") -> None:
        self.type = type
        self.value = value
        
    def __repr__(self, indent:int=0) -> str:
        return f"Expression({self.type}, {self.value})"

class Line:
    def __init__(self, name:str, content:List[Expression|Tok.Token]) -> None:
        self.name = name
        self.content = content
    
    def __repr__(self) -> str:
        return f"Line(\"{self.name}\", {self.content})"

class Parser:
    def __init__(self, tokens:List[Tok.Token]):
        self.tokens:List[Tok.Token] = tokens
        self.programme:List[Line] = []

    def run(self) -> None:
        print(f"matching : {self.match(self.programme[0], self.tokens)}")
        print(Ilib.Programme([Ilib.Assign("a", Ilib.Value("1", Ilib.TYPES.INT))]).dict())
        print(self.programme)
        
    def add_line(self, line:Line) -> None:
        self.programme.append(line)
        
    def match(self, line:Line, tokens:List[Tok.Token]) -> bool:
        index_line:int = 0
        index_token:int = 0
        while index_line < len(line.content):
            if isinstance(line.content[index_line], Tok.Identifier):
                # we dont care for the value of the identifier, we just want to know if it is an identifier
                index_line += 1
                index_token += 1
            elif isinstance(line.content[index_line], Tok.Separator):
                if line.content[index_line].value == tokens[index_token].value:
                    index_line += 1
                    index_token += 1
                else:
                    raise Ex.ParserSyntaxError(f"Expected {line.content[index_line]}, got {tokens[index_token]}")
            else:
                raise Ex.ParserSyntaxError(f"Expected {line.content[index_line]}, got {tokens[index_token]}")
        return True