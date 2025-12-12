import structs as s
import random


# Misc Functions
def no_candy(candy : s.Candy):
	return candy.color == s.COLOR.N and candy.mode == s.MODE.N

def candy_is_special(candy : s.Candy):
	return not no_candy(candy) and candy.mode != s.MODE.N

def random_candy() -> s.Candy:
	return s.Candy(mode=s.MODE.N, color=random.choice([s.COLOR.RED, s.COLOR.ORANGE, s.COLOR.YELLOW, s.COLOR.GREEN, s.COLOR.BLUE, s.COLOR.PURPLE]))

def horizontal_streak_with_candy(game: s.Game, coords : s.Coords) -> int:
	candy : s.Candy = game.board[coords.c][coords.r]
	count : int = 0
	for i in range(0, coords.c+1):							# Loop for selecting an anchor point (start of the consecutive candies)
		if count != 0: break
		if candy.color == game.board[i][coords.r].color:
			count = 1
			for j in range(i+1, game.COLS):							# Loop over the next 4 items to see if they are the same (upto 5 consecutive check)
				if candy.color == game.board[j][coords.r].color:
					count += 1
				else:
					if j < coords.c: count = 0
					break
	return count

def vertical_streak_with_candy(game: s.Game, coords : s.Coords) -> int:
	candy : s.Candy = game.board[coords.c][coords.r]
	count : int = 0
	for i in range(0, coords.r+1):									# Loop for selecting an anchor point (start of the consecutive candies)
		if count != 0: break
		if candy.color == game.board[coords.c][i].color:
			count = 1
			for j in range(i+1, game.ROWS):							# Loop over the next 4 items to see if they are the same (upto 5 consecutive check)
				if candy.color == game.board[coords.c][j].color:
					count += 1
				else:
					if j < coords.r: count = 0
					break
	return count

def elbow_with_candy(game : s.Game, coords : s.Coords) -> bool:
	candy : s.Candy = game.board[coords.c][coords.r]

	# Elbow Match
	horizontal_3_to_left  : bool = False
	horizontal_3_to_right : bool = False
	vertical_3_to_top     : bool = False
	vertical_3_to_bottom  : bool = False

	# Check to the left only if there are 3 cols to the left
	if coords.c >= 2:
		horizontal_3_to_left = (candy.color == game.board[coords.c-1][coords.r].color and candy.color == game.board[coords.c-2][coords.r].color)

	# Check to the right only if there are 3 cols to the right
	if coords.c <= game.COLS - 3:
		horizontal_3_to_right = (candy.color == game.board[coords.c+1][coords.r].color and candy.color == game.board[coords.c+2][coords.r].color)

	# Check to the top only if there are 3 cols to the top
	if coords.r <= game.ROWS - 3:
		vertical_3_to_top = (candy.color == game.board[coords.c][coords.r+1].color and candy.color == game.board[coords.c][coords.r+2].color)

	# Check to the bottom only if there are 3 cols to the bottom
	if coords.r >= 2:
		vertical_3_to_bottom = (candy.color == game.board[coords.c][coords.r-1].color and candy.color == game.board[coords.c][coords.r-2].color)

	# If there is an elbow shape, wrap the candy
	if (horizontal_3_to_left or horizontal_3_to_right) and (vertical_3_to_top or vertical_3_to_bottom): return True
	else: return False

def swap(game : s.Game, coords_1 : s.Coords, coords_2 : s.Coords) -> bool:
	if coords_1.c != coords_2.c and coords_1.r != coords_2.r: return False
	if abs(coords_1.c - coords_2.c) > 1 or abs(coords_1.r - coords_2.r) > 1: return False
	candy_1 = game.board[coords_1.c][coords_1.r]
	candy_2 = game.board[coords_2.c][coords_2.r]
	game.board[coords_1.c][coords_1.r] = candy_2
	game.board[coords_2.c][coords_2.r] = candy_1
	coords_1_allowed = horizontal_streak_with_candy(game, coords_1) >= 3 or vertical_streak_with_candy(game, coords_1) >= 3
	coords_2_allowed = horizontal_streak_with_candy(game, coords_2) >= 3 or vertical_streak_with_candy(game, coords_2) >= 3
	if coords_1_allowed or coords_2_allowed: return True
	else:
		game.board[coords_1.c][coords_1.r] = candy_1
		game.board[coords_2.c][coords_2.r] = candy_2
		return False