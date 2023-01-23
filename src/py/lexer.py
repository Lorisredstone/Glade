from typing import List, Dict, Union, Tuple, Any, Optional

from src.py.lexerTokens import Tokens

class Lexer:
    def __init__(self, raw_content:List[str]):
        self.raw_content:List[str] = raw_content
        self.preparsed:List[str] = []
        self.spaced:str = ""
        
    def run(self) -> None:
        self.preparse()
        self.add_spaces()
        print(self.preparsed)
        print(self.spaced.split(" "))
        
    def preparse(self) -> None:
        # we do nothing big for now, but later it will be useful for adding {} in if, else, classes...
        for line in self.raw_content:
            self.preparsed.append(line)
    
    def add_spaces(self) -> None:
        # for loop for now, beacause we dont have indentation yet
        for expression in self.preparsed:
            buffer:str = ""
            