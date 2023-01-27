from typing import List, Dict, Union, Tuple, Any, Optional

import mod.parser.parserlib as Plib

import src.py.lexerTokens as Tok

class Parser(Plib.Parser):
    def __init__(self, tokens:List[Tok.Token]):
        super().__init__(tokens)
        self.setup()

    def setup(self):
        self.add_line(Plib.Line("Programme", [Plib.Expression(Plib.Types.LATER_DEFINED, "Assign")]))
        self.add_line(Plib.Line("Assign", [Tok.Identifier(""), Tok.Separator("="), Tok.Identifier(""), Tok.Separator("\n")]))