from typing import List, Dict, Union, Tuple, Any, Optional
from enum import Enum, IntEnum, auto

import src.py.lexerTokens as Tok

import mod.parser.parserlib as Plib

class INST(IntEnum):
    ASSIGN_VAR = 0

class TYPES(IntEnum):
    INT = 0
    FLOAT = 1
    STRING = 2
    BOOL = 3

# here we define the intermediate representation of the programme (IR) for every language
class Instruction:
    def dict(self):
        list_attrs = [x for x in dir(self) if not (x in dir(Instruction) or callable(getattr(self, x)))]
        end_dict = {}
        for attr in list_attrs:
            end_dict[attr] = getattr(self, attr)
            if isinstance(end_dict[attr], Instruction):
                end_dict[attr] = end_dict[attr].dict()
            if isinstance(end_dict[attr], list):
                old_list = end_dict[attr]
                end_dict[attr] = []
                for item in old_list:
                    if isinstance(item, Instruction):
                        end_dict[attr].append(item.dict())
                    else:
                        end_dict[attr].append(item)
        return end_dict

class Value(Instruction):
    def __init__(self, value:str, type:TYPES):
        self.value = value
        self.type = type
    
class Assign(Instruction):
    def __init__(self, name:str, value:Value):
        self.name = name
        self.value = value
        self.inst_type = INST.ASSIGN_VAR

class Programme(Instruction):
    def __init__(self, instructions:List[Instruction]):
        self.instructions:List[Instruction] = instructions
    
    def add_instruction(self, instruction:Instruction):
        self.instructions.append(instruction)