import structs

def candy_to_str(candy : structs.Candy):
	return candy.mode.value + " " + candy.color.value

def candy_to_99_str(candy : structs.Candy):
	return str(list(structs.MODE).index(candy.mode)) + str(list(structs.COLOR).index(candy.color))

def print_board_int(game: structs.Game):
	for r in range(game.ROWS - 1, -1, -1):
		print("| ", end="")
		for c in range(game.COLS):
			print(candy_to_99_str(game.board[c][r]), end=" | ")
		print("")

def print_board_str(game: structs.Game):
	for r in range(game.ROWS - 1, -1, -1):
		print("| ", end="")
		for c in range(game.COLS):
			print(candy_to_str(game.board[c][r]), end=" | ")
		print("")