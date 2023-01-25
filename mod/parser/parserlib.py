from typing import List, Dict, Union, Tuple, Any, Optional

import src.py.lexerTokens as Tok

import mod.exceptions as Ex

class Element:
    def __init__(self, content:"List[str|Element]"):
        self.content = content
    def __repr__(self) -> str:
        return f"Element({self.content})"

class ParserLine:
    def __init__(self, line:str):
        print(line)
        self.line:str = line
        self.name = self.line.split("::=")[0][:-1]
        self.content = self.line.split("::=")[1][1:]
        self.parsed:List[str|Element] = self.parse(self.content)
    
    def __repr__(self):
        return f"ParserLine(\"{self.name}\", {self.parsed})"
    
    def __contains__(self, b) -> bool:
        return b == self.name
    
    def parse(self, content:str) -> List[str|Element]:
        """
        should parse (test)(2)3
        as [Element(['test']), Element(['2']), '3']
        """
        parsed:List[str|Element] = []
        buffer:str = ""
        i:int = 0
        while i < len(content):
            buffer = ""
            if content[i] == "(":
                i += 1
                while content[i] != ")": # TODO : handle nested parentheses
                    buffer += content[i]
                    i += 1
                i += 1
                parsed.append(Element(self.parse(buffer)))
            else:
                while i < len(content) and content[i] != "(":
                    buffer += content[i]
                    i += 1
                parsed.append(buffer)
        return parsed
        

class Parser:
    def __init__(self, tokens:List[Tok.Token], file:str):
        self.tokens:List[Tok.Token] = tokens
        print(self.tokens)
        self.file = file
        self.lines:List[ParserLine] = []

    def run(self) -> None:
        self.parse_file()
        if not self.name_in_lines("Programme", self.lines):
            raise Ex.NoProgrammeSpecified()
        for line in self.lines:
            print(line)

    def parse_file(self) -> None:
        with open(self.file, "r") as f:
            content = f.readlines()
        for line in content:
            self.lines.append(ParserLine(line if line[-1] != "\n" else line[:-1]))

    def name_in_lines(self, name:str, lines:List[ParserLine]) -> bool:
        return any(name in line.line for line in lines)