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
                var_assign:str = ""
                var_assign += f"{instruction.name}:{get_type_as_str(instruction.value.type)} = "
                var_assign += "\"" if instruction.value.type == Ilib.TYPES.STRING else ''
                var_assign += instruction.value.value
                var_assign += "\"" if instruction.value.type == Ilib.TYPES.STRING else ""
                self.add_to_code(var_assign)
        return self.output
        
    def add_to_code(self, string: str):
        self.output += self.indentation*self.indent + string + "\n"
        
def get_type_as_str(type: Ilib.TYPES) -> str:
    return {
        Ilib.TYPES.INT: "int",
        Ilib.TYPES.FLOAT: "float",
        Ilib.TYPES.STRING: "str",
        Ilib.TYPES.BOOL: "bool",
        Ilib.TYPES.TYPE: "type",
    }.get(type, "type")