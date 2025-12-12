import main as cc
import structs as s
import misc as m
import console_print as c_print


def swap_prompt():
	print("")
	coords_1 = s.Coords(int(input("\tC1:")), int(input("\tR1:")))
	coords_2 = s.Coords(int(input("\tC2:")), int(input("\tR2:")))
	while not m.swap(myCandyCrush, coords_1, coords_2):
		print("\nInvalid swap, try again\n")
		coords_1 = s.Coords(int(input("\tC1:")), int(input("\tR1:")))
		coords_2 = s.Coords(int(input("\tC2:")), int(input("\tR2:")))

# init game
myCandyCrush : s.Game = s.Game()
s.new_board(myCandyCrush, 8, 8)
cc.refill(myCandyCrush)

# Optimal scenario for Testing a Horizontally Stripped Candy
myCandyCrush.board[0][0] = s.Candy(color=s.COLOR.BLUE)
myCandyCrush.board[1][0] = s.Candy(color=s.COLOR.BLUE)
myCandyCrush.board[2][0] = s.Candy(color=s.COLOR.BLUE)
myCandyCrush.board[3][0] = s.Candy(color=s.COLOR.RED)
myCandyCrush.board[3][1] = s.Candy(color=s.COLOR.BLUE)
myCandyCrush.board[1][2] = s.Candy(color=s.COLOR.BLUE)
myCandyCrush.board[0][2] = s.Candy(color=s.COLOR.BLUE)


while True:
	print("")
	c_print.print_board_int(myCandyCrush)
	print("")
	swap_prompt()
	# Special check for Manual Color Bomb To be placed here
	cc.match_and_destroy(myCandyCrush)
	while cc.refill(myCandyCrush):
		cc.match_and_destroy(myCandyCrush)