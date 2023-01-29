from typing import List, Dict, Union, Tuple, Any, Optional
from enum import Enum, IntEnum, auto

import src.py_to_i.lexerTokens as Tok

import mod.exceptions as Ex
import mod.inter.interlib as Ilib

class Types(Enum):
    # Element types
    LATER_DEFINED = auto()
    
class Line:
    def __init__(self, name:str, content:List[Tok.Token]) -> None:
        self.name = name
        self.content = content
    
    def __repr__(self) -> str:
        return f"Line(\"{self.name}\", {self.content})"

class Parser:
    def __init__(self, tokens:List[Tok.Token]):
        self.tokens:List[Tok.Token] = tokens
        self.programme:List[Line] = []
        self.program:Ilib.Programme = Ilib.Programme()

    def run(self) -> Ilib.Programme:
        while len(self.tokens) > 0:
            # on récupère la ligne correspondante
            matching_list:List[Line] = []
            for line in self.programme:
                if self.match(line, self.tokens):
                    matching_list.append(line)
            if len(matching_list) == 0:
                raise Ex.ParserSyntaxError("No matching line found")
            if len(matching_list) > 1:
                raise Ex.ParserSyntaxError(f"Multiple matching lines found : {list(map(lambda x: x.name, matching_list))})")
            matching_line:Line = matching_list[0]
            
            # on vérifie que l'instruction existe et on la récupère
            if not matching_line.name in dir(Ilib):
                raise Ex.ParserSyntaxError(f"Unknown instruction {matching_line.name}")
            
            instruction:Ilib.Instruction = getattr(Ilib, matching_line.name)("", "")
            
            # on récupère les tokens qui correspondent à l'instruction
            tokens:List[Tok.Token] = self.get_tokens(matching_line, self.tokens)

            instruction = self.parse_instruction(instruction, tokens, matching_line)
            
            self.program.add_instruction(instruction)
            
        return self.program
            
    def parse_instruction(self, instruction:Ilib.Instruction, tokens:List[Tok.Token], matching_line:Line) -> Ilib.Instruction:
        for i, token in enumerate(matching_line.content):
            if token.name_value:
                if token.name_value in dir(instruction):
                    match token.name_value:
                        case "name": # on set juste le nom
                            setattr(instruction, token.name_value, tokens[i].value)
                        case "value": # on crée un objet value
                            value:Ilib.Value = Ilib.infer_value(tokens[i].value)
                            setattr(instruction, token.name_value, value)
                else:
                    raise Ex.ParserSyntaxError(f"Unknown attribute {token.name_value} for instruction {matching_line.name}")
        return instruction
            
    def get_tokens(self, line:Line, tokens:List[Tok.Token]) -> List[Tok.Token]:
        return_list:List[Tok.Token] = []
        index_line:int = 0
        index_token:int = 0

        while True:
            if isinstance(line.content[index_line], Tok.Identifier):
                if line.content[index_line].value:
                    if line.content[index_line].value == tokens[index_token].value:
                        return_list.append(tokens[index_token])
                    else:
                        raise Ex.ParserSyntaxError(f"Expected {line.content[index_line]}, got {tokens[index_token]}")
                else:
                    return_list.append(tokens[index_token])
    
            elif isinstance(line.content[index_line], Tok.Separator):
                if line.content[index_line].value:
                    if line.content[index_line].value == tokens[index_token].value:
                        return_list.append(tokens[index_token])
                    else:
                        raise Ex.ParserSyntaxError(f"Expected {line.content[index_line]}, got {tokens[index_token]}")
                else:
                    return_list.append(tokens[index_token])
            else:
                raise Ex.ParserSyntaxError(f"Expected {line.content[index_line]}, got {tokens[index_token]}")
            
            index_line += 1
            index_token += 1
            
            if index_line >= len(line.content):
                break
        
        # on supprime les tokens de la liste
        self.tokens = self.tokens[index_token:]
    
        return return_list
    
    def add_line(self, line:Line) -> None:
        self.programme.append(line)
        
    def match(self, line:Line, tokens:List[Tok.Token]) -> bool:
        index_line:int = 0
        index_token:int = 0
        while index_line < len(line.content):
            if isinstance(line.content[index_line], Tok.Identifier):
                if line.content[index_line].value:
                    if line.content[index_line].value == tokens[index_token].value:
                        index_line += 1
                        index_token += 1
                    else:
                        return False
                else:
                    index_line += 1
                    index_token += 1
            elif isinstance(line.content[index_line], Tok.Separator):
                if line.content[index_line].value:
                    if line.content[index_line].value == tokens[index_token].value:
                        index_line += 1
                        index_token += 1
                    else:
                        return False
                else:
                    index_line += 1
                    index_token += 1
            else:
                raise Ex.ParserSyntaxError(f"Expected {line.content[index_line]}, got {tokens[index_token]}")
        return True