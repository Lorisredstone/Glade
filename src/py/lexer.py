from typing import List, Dict, Union, Tuple, Any, Optional

class Lexer:
    def __init__(self, raw_content:List[str]):
        self.raw_content = raw_content
        
    def run(self):
        print(self.raw_content)