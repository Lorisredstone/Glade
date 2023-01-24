from typing import List, Dict, Union, Tuple, Any, Optional
from enum import Enum, IntEnum, auto
import token

KEYWORDS:List[str] = []
OPERATORS:List[str] = ["+"]
BUILTINS:List[str] = []
LITERALS:List[str] = ["True", "False"]
SEPARATORS:List[str] = [":", "\n", "="]

# to have a beatiful print
SPECIAL:dict[str, str] = {
    "\n" : "\\n"
}

# to have a common class for all tokens
class Token:
    type:str = ""
    value:str = ""
    def __repr__(self) -> str:
        total = "<"
        total += self.__dict__.get('type', '')
        total += "("
        value = self.__dict__.get('value', '')
        total += value if value not in SPECIAL else SPECIAL[value]
        total += ")>"
        return total
    
class Keyword(Token):
    def __init__(self, value:str):
        self.value:str = value
        self.type:str = "Keyword"

class Operator(Token):
    def __init__(self, value:str):
        self.value:str = value
        self.type:str = "Operator"

class Builtin(Token):
    def __init__(self, value:str):
        self.value:str = value
        self.type:str = "Builtin"

class Literal(Token):
    def __init__(self, value:str):
        self.value:str = value
        self.type:str = "Literal"

class Separator(Token):
    def __init__(self, value:str):
        self.value:str = value
        self.type:str = "Separator"

class Identifier(Token):
    def __init__(self, value:str):
        self.value:str = value
        self.type:str = "Identifier"