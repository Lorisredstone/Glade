from typing import List, Dict, Union, Tuple, Any, Optional
from enum import Enum, IntEnum, auto
import token

class Tokens(IntEnum):
    TEXT = auto()
    NUMBER = auto()
    BOOL = auto()
    KEYWORD = auto()
    EQUAL = auto()
    COLON = auto()