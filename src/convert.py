import dis
import re

class Convertiseur:
    def __init__(self, code:str, debug:bool = False) -> None:
        self.code:str = code
        self.debug:bool = debug
        self.code_c:str = ""
        
    def run(self, debug:bool=False) -> None:
        header:str = open("config/header.c", "r").read()
        self.add_to_c(header)
        self.add_to_c("int main() {\n")
        
        bytecode = dis.Bytecode(self.code)
        for instruction in bytecode:
            self.code_c += self.convert(instruction)
            
        self.add_to_c("\n}")
        
    def add_to_c(self, code:str) -> None:
        self.code_c += code

    def convert(self, instruction:dis.Instruction) -> str:
        if self.debug:
            print(f"Converting {instruction}")
            
        match instruction.opname:
            case "LOAD_CONST":
                ...
            case "STORE_NAME":
                ...
            case "RETURN_VALUE":
                ...
            
        return ""