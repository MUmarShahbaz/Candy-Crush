from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar

class COLOR(Enum):
    N = ""
    RED = "Red"
    ORANGE = "Orange"
    YELLOW = "Yellow"
    GREEN = "Green"
    BLUE = "Blue"
    PURPLE = "Purple"

class MODE(Enum):
    N = ""
    VS = "Verticall Stripped"
    HS = "Horizontally Stripped"
    W = "Wrapped"
    CB = "Color Bomb"

@dataclass
class Candy:
    mode: MODE = MODE.N
    color: COLOR = COLOR.N

@dataclass
class Coords:
    c : int = 0
    r : int = 0

@dataclass
class Waiting_Candy:
    candy : Candy = Candy()
    coords : Coords = Coords()

@dataclass
class Game:
    ROWS: ClassVar[int] = 8
    COLS: ClassVar[int] = 8    
    board: list[list[Candy]] = field(default_factory=lambda: [[Candy() for _ in range(Game.COLS)]for _ in range(Game.ROWS)])
    score: int = 0
    time: int = 0