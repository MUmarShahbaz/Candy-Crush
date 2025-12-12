import structs as s
import misc as m
import console_print as c_print

# Queues
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
	print(f"Destroying Candy at ({coords.c},{coords.r}): {c_print.candy_to_str(game.board[coords.c][coords.r])}")
	game.board[coords.c][coords.r] = s.Candy()									# Replace with an empty candy (Queued Candies will be activated near end of the execution cycle)


def match_and_destroy(game: s.Game):
	# Special check to detect and queue wrapped candies
	new_wraped : list[s.Waiting_Candy] = []
	for c in range(game.COLS):
		for r in range(game.ROWS):
			if m.elbow_with_candy(game, s.Coords(c, r)):
				new_wraped.append(s.Waiting_Candy(s.Candy(s.MODE.W, game.board[c][r].color), s.Coords(c,r)))

	# Actual Match and Destroy function
	for c in range(game.COLS):
		for r in range(game.ROWS):
			candy : s.Candy = game.board[c][r]
			if m.no_candy(candy): continue	# Skip empty candies

			# Store special pattern checks
			horizontal = m.horizontal_streak_with_candy(game, s.Coords(c, r))
			vertical = m.vertical_streak_with_candy(game, s.Coords(c, r))

			# Destroy
			# Horizontal
			count : int = 1
			for h in range(c+1, game.COLS):
				if candy.color == game.board[h][r].color:
					count += 1
				else: break
			if count >= 3:
				for i in range(c, c+count):
					destroy_candy(game, s.Coords(i, r))

			# Vertical Dimension
			count = 1
			for v in range(r+1, game.ROWS):
				if candy.color == game.board[c][v].color:
					count += 1
				else: break
			if count >= 3:
				for i in range(r, r+count):
					destroy_candy(game, s.Coords(c, i))

			# Assign special
			if m.candy_is_special(candy):			continue
			if horizontal == 4:						game.board[c][r] = s.Candy(mode=s.MODE.HS, color=candy.color)
			if vertical   == 4:						game.board[c][r] = s.Candy(mode=s.MODE.VS, color=candy.color)
			if horizontal >= 5 or vertical >= 5:	game.board[c][r] = s.Candy(mode=s.MODE.CB, color=s.COLOR.N  )
			if m.candy_is_special(game.board[c][r]): print(f"New Special Candy at ({c},{r}): {c_print.candy_to_str(game.board[c][r])}")

	# Add all the new Wrapped Candies
	for new_wrapped_candy in new_wraped:
		game.board[new_wrapped_candy.coords.c][new_wrapped_candy.coords.r] = new_wrapped_candy.candy
		print(f"New wrapped at {new_wrapped_candy.coords.c},{new_wrapped_candy.coords.r}")

	# Run any triggered special candies
	apply_special_candies(game)

def apply_special_candies(game : s.Game):
	global activated_specials
	for queued_candy in activated_specials:
		print(f"Activating {c_print.candy_to_str(queued_candy.candy)} at ({queued_candy.coords.c}, {queued_candy.coords.r})")
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

	activated_specials = []