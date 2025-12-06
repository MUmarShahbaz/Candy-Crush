import structs as s
import misc as m

# Queues
new_specials = list[s.Waiting_Candy]
activated_specials = list[s.Waiting_Candy]


# Game Functions
def refill(game : s.Game):
	for c in range(game.COLS):									# For each column
		for r in range(game.ROWS-1, -1, -1):					# For each element in the current column
			if m.no_candy(game.board[c][r]):					# If this element is empty
				for i in range(r, game.ROWS - 1):				# Shift elements from right to left to fill in the empty space
					game.board[c][i] = game.board[c][i+1]
				game.board[c][game.ROWS - 1] = m.random_candy()	# Add a random candy at top of the column