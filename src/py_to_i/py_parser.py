from typing import List, Dict, Union, Tuple, Any, Optional

import mod.parser.parserlib as Plib

import src.py_to_i.lexerTokens as Tok

class Parser(Plib.Parser):
    def __init__(self, tokens:List[Tok.Token]):
        super().__init__(tokens)
        self.setup()

    def setup(self):
        self.add_line(Plib.Line("Assign", [
            Tok.Identifier("", name_value="name"), 
            Tok.Separator("="), 
            Tok.Identifier("", name_value="value"), 
            Tok.Separator("\n")
        ]))