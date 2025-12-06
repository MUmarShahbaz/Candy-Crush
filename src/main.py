import random

ROWS : int = 8
COLS : int = 6
board = [[0 for _ in range(ROWS)] for _ in range(COLS)]
queued_special : list[list[int]] = []

def is_special(id : int) -> bool:
	MODE : int = id // 10
	match MODE:
		case 1: return True
		case 2: return True
		case 3: return True
		case _: return False

def refill() -> None:
	global board
	for c in range(COLS):								# For each updated column
		for r in range(ROWS-1, -1, -1):					# For each element in the current column
			if board[c][r] == 0:						# If this element is empty
				for i in range(r, ROWS - 1):			# From this element to second-last
					board[c][i] = board[c][i+1]			# This element is equal to the next
				board[c][ROWS - 1] = random.randint(1, 7)

def detect_and_destroy() -> bool:
	global board
	destruction_queue : list[list[int]] = []

	# Horizontal Checks
	for r in range(ROWS - 1, -1, -1):
		count = 0
		for c in range(COLS):
			if count > 0:
				count -= 1
				continue
			for i in range(c+1, COLS):
				if board[c][r] == board[i][r]:
#					print(f"At ({c},{r}) and ({i},{r}) : {board[c][r]}")
					count += 1
				else: break
			if count >= 2:
#				print("Consecutive found")
				for i in range(c, c+1+count):
					destruction_queue.append([i, r])
    
    # Vertical Checks
	for c in range(COLS):
		count = 0
		for r in range(ROWS - 1, -1, -1):
			if count > 0:
				count -= 1
				continue
			for i in range(r-1, -1, -1):
				if board[c][r] == board[c][i]:
#					print(f"At ({c},{r}) and ({c},{i}) : {board[c][r]}")
					count += 1
				else: break
			if count >= 2:
#				print("Consecutive found")
				for i in range(r, r-1-count, -1):
					destruction_queue.append([c, i])
	
	# Clear Destruction Queue
	for i in destruction_queue:
		destroy(i[0], i[1])
	return len(destruction_queue) > 0

def destroy(c : int, r : int) -> None:
	global board
	if is_special(board[c][r]):
		queued_special.append([c, r, board[c][r]])
	board[c][r] = 0