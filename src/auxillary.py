import main

def id_to_string(id : int) -> str:
	COLOR : int = id % 10
	MODE : int = id // 10

	name = ""

	match MODE:
		case 0: name = ""
		case 1: name = "Horizontally Stripped"
		case 2: name = "Vertically Stripped"
		case 3: name = "Color Bomb"
		case _: pass

	match COLOR:
		case 0: return " "
		case 1: name += ""
		case 2: name += " Red Candy"
		case 3: name += " Orange Candy"
		case 4: name += " Yellow Candy"
		case 5: name += " Green Candy"
		case 6: name += " Blue Candy"
		case 7: name += " Purple Candy"
		case _: pass
	
	return name

def print_board_int():
    for r in range(main.ROWS - 1, -1, -1):
        print("| ", end="")
        for c in range(main.COLS):
            print(str(main.board[c][r]) + " | ", end="")
        print("")

def print_board_str():
    for r in range(main.ROWS - 1, -1, -1):
        print("| ", end="")
        for c in range(main.COLS):
            print(id_to_string(main.board[c][r]) + " | ", end="")
        print("")