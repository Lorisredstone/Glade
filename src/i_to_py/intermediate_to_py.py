from typing import List, Dict, Union, Tuple, Any, Optional

import mod.inter.interlib as Ilib

class Intermediatetopy:
    def __init__(self, inter: Ilib.Programme):
        self.inter = inter
        self.output = ""
        self.indent = 0
        self.indentation = "    "
        
    def intermediate_to_py(self) -> str:
        for instruction in self.inter.instructions:
            if isinstance(instruction, Ilib.Assign):
                self.add_to_code(f"{instruction.name} = {instruction.value.value}")
        
        return self.output
        
    def add_to_code(self, string: str):
        self.output += self.indentation*self.indent + string + "\n"