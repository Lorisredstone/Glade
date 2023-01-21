from typing import List, Dict, Union, Tuple, Any, Optional
from enum import Enum, IntEnum

class IINST(IntEnum):
    ASSIGN_VAR = 0

class ITYPES(IntEnum):
    INT = 0
    FLOAT = 1
    STRING = 2
    BOOL = 3

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

class IValue(Instruction):
    def __init__(self, value:str, type:ITYPES):
        self.value = value
        self.type = type
    
class IAssign(Instruction):
    def __init__(self, name:str, value:IValue):
        self.name = name
        self.value = value
        self.inst_type = IINST.ASSIGN_VAR

class IProgramme(Instruction):
    def __init__(self, instructions:List[Instruction]):
        self.instructions:List[Instruction] = instructions
    
    def add_instruction(self, instruction:Instruction):
        self.instructions.append(instruction)