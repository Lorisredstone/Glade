from typing import List, Dict, Union, Tuple, Any, Optional

import src.py.lexerTokens as Tok

class Lexer:
    def __init__(self, raw_content:List[str]):
        self.raw_content:List[str] = raw_content
        self.preparsed:str = ""
        self.spaced:List[str] = []
        self.tokens:List[Tok.Token] = []
        
    def run(self) -> List[Tok.Token]:
        self.preparse()
        self.add_spaces()
        self.tokenize()
        return self.tokens
        
    def preparse(self) -> None:
        # we do nothing big for now, but later it will be useful for adding {} in if, else, classes...
        for line in self.raw_content:
            self.preparsed += line
    
    def add_spaces(self) -> None:
        internal_spaced:str = ""
        # for loop for now, beacause we dont have indentation yet
        buffer:str = ""
        for char in self.preparsed:
            if char in Tok.SEPARATORS + Tok.OPERATORS:
                internal_spaced += " " + buffer + " "
                internal_spaced += " " + char + " "
                buffer = ""
                continue
            buffer += char
        self.spaced = [x for x in internal_spaced.split(" ") if x]

    def tokenize(self) -> None:
        for token in self.spaced:
            if token in Tok.KEYWORDS:
                self.tokens.append(Tok.Keyword(token))
            elif token in Tok.SEPARATORS:
                self.tokens.append(Tok.Separator(token))
            elif token in Tok.OPERATORS:
                self.tokens.append(Tok.Operator(token))
            elif token in Tok.BUILTINS:
                self.tokens.append(Tok.Builtin(token))
            elif token in Tok.LITERALS:
                self.tokens.append(Tok.Literal(token))
            else:
                self.tokens.append(Tok.Identifier(token))