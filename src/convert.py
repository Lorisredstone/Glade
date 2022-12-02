from typing import List
import random
import dis
class Convertiseur:
    def __init__(self, code:str, debug:bool = False) -> None:
        self.code:str = code
        self.debug:bool = debug
        self.code_c:str = ""
        self.indent_level:int = 4
        self.hash_list:List[int]= list(range(1000, 9999))
        random.shuffle(self.hash_list)
        self.hash_pointer:int = 0
        
    def get_next_hash(self) -> int:
        hash_data = self.hash_list[self.hash_pointer]
        self.hash_pointer += 1
        return hash_data
        
    def run(self, debug:bool=False) -> None:
        header:str = open("config/header.c", "r").read()
        self.add_to_c(header)
        
        bytecode = dis.Bytecode(self.code)
        print(bytecode)
        for instruction in bytecode:
            self.convert(instruction)
            
        self.add_to_c("\n}")
        
    def add_to_c(self, code:str) -> None:
        self.code_c += ' ' * self.indent_level+code

    def convert(self, instruction:dis.Instruction) -> None:
        if self.debug:
            print(f"Converting {instruction}")
            
        current_hash = self.get_next_hash()
        
        match instruction.opname:
            case "LOAD_CONST":
                self.add_to_c(f"Element_t element{current_hash};\n")
                if isinstance(instruction.argval, str):
                    self.add_to_c(f'printf("{instruction.argval}");\n')
                    self.add_to_c(f'element{current_hash}.data_type = STRING_T;\n')
                    self.add_to_c(f'element{current_hash}.value_str = "{instruction.argval}";\n')
                elif isinstance(instruction.argval, bool):
                    self.add_to_c(f'printf("%d", {instruction.argval});\n')
                    self.add_to_c(f'element{current_hash}.data_type = BOOL_T;\n')
                    self.add_to_c(f'element{current_hash}.value_int = {instruction.argval};\n')
                elif isinstance(instruction.argval, int):
                    self.add_to_c(f'printf("%d", {instruction.argval});\n')
                    self.add_to_c(f'element{current_hash}.data_type = INT_T;\n')
                    self.add_to_c(f'element{current_hash}.value_int = {instruction.argval};\n')
                elif isinstance(instruction.argval, float):
                    self.add_to_c(f'printf("%f", {instruction.argval});\n')
                    self.add_to_c(f'element{current_hash}.data_type = FLOAT_T;\n')
                    self.add_to_c(f'element{current_hash}.value_float = {instruction.argval};\n')
                elif instruction.argval is None:
                    self.add_to_c(f'printf("None");\n')
                    self.add_to_c(f'element{current_hash}.data_type = NONE_T;\n')
                    self.add_to_c(f'element{current_hash}.is_none = 1;\n')
                self.add_to_c(f"push(stack, element{current_hash});\n")
                self.add_to_c("\n")
            case "STORE_NAME":
                ...
            case "RETURN_VALUE":
                ...