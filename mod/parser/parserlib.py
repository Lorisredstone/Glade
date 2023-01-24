from typing import List, Dict, Union, Tuple, Any, Optional

import src.py.lexerTokens as Tok

class ParserLine:
    def __init__(self, line:str):
        self.line:str = line
    
    def __repr__(self):
        return f"ParserLine(\"{self.line}\")"
    

class Parser:
    def __init__(self, tokens:List[Tok.Token], file:str):
        self.tokens:List[Tok.Token] = tokens
        self.file = file
        self.lines:List[ParserLine] = []
    
    def run(self) -> None:
        self.parse_file()
        print(self.lines)
        
    def parse_file(self) -> None:
        with open(self.file, "r") as f:
            content = f.readlines()
        for line in content:
            self.lines.append(ParserLine(line if line[-1] != "\n" else line[:-1]))