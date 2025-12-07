import structs as s
import misc as m

# Queues
new_specials : list[s.Waiting_Candy] = []
activated_specials : list[s.Waiting_Candy] = []


# Game Functions

def refill(game : s.Game) -> bool:
	flag : bool = False
	for c in range(game.COLS):									# For each column
		for r in range(game.ROWS-1, -1, -1):					# For each element in the current column
			if m.no_candy(game.board[c][r]):					# If this element is empty
				for i in range(r, game.ROWS - 1):				# Shift elements from right to left to fill in the empty space
					game.board[c][i] = game.board[c][i+1]
				game.board[c][game.ROWS - 1] = m.random_candy()	# Add a random candy at top of the column
				flag = True
	return flag


def destroy_candy(game : s.Game, coords : s.Coords):
    candy = game.board[coords.c][coords.r]										# Access the candy at the given coords
    if m.candy_is_special(candy):												# If the candy is a special candy, queue it
        activated_specials.append(s.Waiting_Candy(coords=coords, candy=candy))
    game.board[coords.c][coords.r] = s.Candy()									# Replace with an empty candy (Queued Candies will be activated near end of the execution cycle)
    

def queue_new_specials(game: s.Game, coords : s.Coords):
	candy : s.Candy = game.board[coords.c][coords.r]

    # Only assign if candy exists and is not already a special
	if not m.candy_is_special(candy) and not m.no_candy(candy):

		# Horizontal Match
		for i in range(max(coords.c - 4, 0), coords.c+1):							# Loop for selecting an anchor point (start of the consecutive candies)
			if candy.color == game.board[i][coords.r].color:
				count : int = 1
				for j in range(i+1, min(game.COLS, i+5)):							# Loop over the next 4 items to see if they are the same (upto 5 consecutive check)
					if candy.color == game.board[j][coords.r].color:
						count += 1
					else: break

				# If 4 consecutive, Queue a Horizontally Stripped Candy
				if count == 4: new_specials.append(s.Waiting_Candy(coords=coords, candy=s.Candy(mode=s.MODE.HS, color=candy.color)))

				# If 5 consecutive, Queue a Color Bomb Candy
				if count == 5: new_specials.append(s.Waiting_Candy(coords=coords, candy=s.Candy(mode=s.MODE.CB, color=s.COLOR.N)))

		# Vertical Match
		for i in range(max(coords.r - 4, 0), coords.r+1):							# Loop for selecting an anchor point (start of the consecutive candies)
			if candy.color == game.board[coords.c][i].color:
				count : int = 1
				for j in range(i+1, min(game.ROWS, i+5)):							# Loop over the next 4 items to see if they are the same (upto 5 consecutive check)
					if candy.color == game.board[coords.c][j].color:
						count += 1
					else: break

				# If 4 consecutive, Queue a Vertically Stripped Candy
				if count == 4: new_specials.append(s.Waiting_Candy(coords=coords, candy=s.Candy(mode=s.MODE.VS, color=candy.color)))

				# If 5 consecutive, Queue a Color Bomb Candy
				if count == 5: new_specials.append(s.Waiting_Candy(coords=coords, candy=s.Candy(mode=s.MODE.CB, color=s.COLOR.N)))

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
		if (horizontal_3_to_left or horizontal_3_to_right) and (vertical_3_to_top or vertical_3_to_bottom):
			new_specials.append(s.Waiting_Candy(coords=coords, candy=s.Candy(mode=s.MODE.W, color=candy.color)))

def assign_specials(game : s.Game):
    for queued_candy in new_specials:
        game.board[queued_candy.coords.c][queued_candy.coords.r] = queued_candy.candy

def apply_special_candies(game : s.Game):
	for queued_candy in activated_specials:

		# Horizontally Stripped Candy
		if queued_candy.candy.mode == s.MODE.HS:
			# Destroy entire row
			for i in range(game.COLS):
				destroy_candy(game, s.Coords(c=i, r=queued_candy.coords.r))

		# Vertically Stripped Candy
		if queued_candy.candy.mode == s.MODE.VS:
			# Destroy entire column
			for i in range(game.ROWS):
				destroy_candy(game, s.Coords(c=queued_candy.coords.c, r=i))

		# Wrapped Candy:
		if queued_candy.candy.mode == s.MODE.W:
			# Destroy a 3*3 chunk around this candy
			for i in range(max(0, queued_candy.coords.c-1), min(game.COLS, queued_candy.coords.c+2)):
				for j in range(max(0, queued_candy.coords.r-1), min(game.ROWS, queued_candy.coords.r+2)):
					destroy_candy(game, s.Coords(c=i, r=j))

		# Color Bomb:
		if queued_candy.candy.mode == s.MODE.CB:
			pass