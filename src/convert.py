from typing import List
import random
import dis

class Convertiseur:
    def __init__(self, code:str, debug:bool = False) -> None:
        self.code:str = code
        self.debug:bool = debug
        self.code_c:str = ""
        self.indent_level:int = 0
        self.hash_list:List[int]= list(range(1000, 9999))
        random.shuffle(self.hash_list)
        self.hash_pointer:int = 0
        self.modules_list = {'BINARY_ADD' : "config/modules/BINARY_ADD.c",}
        
    def get_next_hash(self) -> int:
        hash_data = self.hash_list[self.hash_pointer]
        self.hash_pointer += 1
        return hash_data
        
    def run(self, debug:bool=False) -> None:
        header:str = open("config/header.c", "r").read()
        self.add_to_c(header)
        
        bytecode = dis.Bytecode(self.code)
        
        # first we add the nessessary modules
        for instruction in bytecode:
            if instruction.opname in self.modules_list:
                self.add_to_c(f"\n{open(self.modules_list[instruction.opname], 'r').read()}")
                self.add_to_c("\n")
        if any(instruction.argval == "print" and instruction.opname == "LOAD_NAME" for instruction in bytecode):
            self.add_to_c(f"\n{open('config/modules/PRINT.c', 'r').read()}")
            self.add_to_c("\n")
        
        self.add_to_c("\nint main() {\n")
        self.indent_level = 4
        self.add_to_c("Stack_t *stack = create_stack(10);\n")
        
        for instruction in bytecode:
            self.convert(instruction)
            
        self.add_to_c("\n}")
        
    def add_to_c(self, code:str) -> None:
        self.code_c += ' ' * self.indent_level+code

    def convert(self, instruction:dis.Instruction) -> None:
        if self.debug:
            print(f"Converting {instruction}")
            # print(list(dis.Bytecode(instruction.argval)))
            self.add_to_c(f"// {instruction}\n")
            
        current_hash = self.get_next_hash()
        
        match instruction.opname:
            case "LOAD_CONST":
                self.add_to_c(f"Element_t *element{current_hash} = malloc(sizeof(Element_t));\n")
                if isinstance(instruction.argval, str):
                    self.add_to_c(f'element{current_hash}->data_type = STRING_T;\n')
                    self.add_to_c(f'element{current_hash}->value_str = "{instruction.argval}";\n')
                elif isinstance(instruction.argval, bool):
                    self.add_to_c(f'element{current_hash}->data_type = BOOL_T;\n')
                    self.add_to_c(f'element{current_hash}->value_int = {instruction.argval};\n')
                elif isinstance(instruction.argval, int):
                    self.add_to_c(f'element{current_hash}->data_type = INT_T;\n')
                    self.add_to_c(f'element{current_hash}->value_int = {instruction.argval};\n')
                elif isinstance(instruction.argval, float):
                    self.add_to_c(f'element{current_hash}->data_type = FLOAT_T;\n')
                    self.add_to_c(f'element{current_hash}->value_float = {instruction.argval};\n')
                elif instruction.argval is None:
                    self.add_to_c(f'element{current_hash}->data_type = NONE_T;\n')
                    self.add_to_c(f'element{current_hash}->is_none = 1;\n')
                else:
                    print(f"Unknown type in LOAD_CONST : {type(instruction.argval)}")
                    exit(1)
                self.add_to_c(f"push(stack, element{current_hash});\n")
                self.add_to_c("\n")
            case "STORE_NAME":
                self.add_to_c(f"Element_t *element{current_hash};\n")
                self.add_to_c(f"element{current_hash} = pop(stack);\n")
                self.add_to_c(f"add_variable(\"main_{instruction.argval}\", element{current_hash});\n")
                self.add_to_c("\n")
            case "RETURN_VALUE":
                self.add_to_c(f"Element_t *element{current_hash};\n")
                self.add_to_c(f"element{current_hash} = pop(stack);\n")
                self.add_to_c(f"return element{current_hash}->is_none ? 0 : 1;")
            case "LOAD_NAME":
                self.add_to_c(f"Element_t *element{current_hash};\n")
                self.add_to_c(f"element{current_hash} = get_variable(\"main_{instruction.argval}\");\n")
                self.add_to_c(f"push(stack, element{current_hash});\n")
                self.add_to_c("\n")
            case "BINARY_ADD":
                self.add_to_c(f"binary_add(stack);\n")
                self.add_to_c("\n")
            case "POP_TOP":
                self.add_to_c(f"pop(stack);\n")
                self.add_to_c("\n")
            case _:
                print(f"Unknown instruction : {instruction.opname}")