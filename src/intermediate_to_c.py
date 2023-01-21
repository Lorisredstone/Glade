from typing import List, Dict, Union, Tuple, Any, Optional
from enum import Enum, IntEnum
import subprocess
import os
import re

from src.intermediate import *

import mod.colorprint as colorprint

class Intermediatetoc:
    def __init__(self, file:str, intermediate:Dict[Any, Any]):
        self.file = file
        self.intermediate = intermediate
        self.output:List[str] = []
        
    def convert(self):
        self.add_module("start")
        for instruction in self.intermediate["instructions"]:
            if instruction["inst_type"] == IINST.ASSIGN_VAR:
                print(instruction)
            else:
                raise Exception(f"Unknown type {instruction['inst_type']}")
        self.add_module("end")
        self.write()
    
    def write(self):
        with open(self.file, "w") as f:
            f.write("\n".join(self.output))
            
    def add(self, string:str):
        self.output.append(string)
        
    def add_module(self, module_name:str):
        with open(f"cmod/c/{module_name}.c", "r") as f:
            self.output.append(f.read())