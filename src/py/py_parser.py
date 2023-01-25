from typing import List, Dict, Union, Tuple, Any, Optional

import mod.parser.parserlib as Plib

import src.py.lexerTokens as Tok

class Parser(Plib.Parser):
    def __init__(self, tokens:List[Tok.Token]):
        super().__init__(tokens)
        self.setup()
        print(self.programme)

    def setup(self):
        self.add_line(Plib.Line("Programme", ["Hello", Plib.Expression(Plib.Types.REPEAT, ["World"])]))