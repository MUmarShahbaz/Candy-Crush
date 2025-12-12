from dataclasses import dataclass, field
from enum import Enum

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
	VS = "Vertically Stripped"
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
	candy : Candy = field(default_factory=lambda: Candy())
	coords : Coords = field(default_factory=lambda: Coords())

@dataclass
class Game:
	ROWS: int = 8
	COLS: int = 8
	board: list[list[Candy]] = field(default_factory=lambda: [[Candy() for _ in range(Game.COLS)]for _ in range(Game.ROWS)])
	score: int = 0
	time: int = 0

def new_board(game: Game, cols : int, rows : int):
	game.COLS = cols
	game.ROWS = rows
	game.board = [[Candy() for _ in range(rows)] for _ in range(cols)]