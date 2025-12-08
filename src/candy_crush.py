import main as cc
import structs as s
import misc as m
import console_print as c_print


# init game
myCandyCrush : s.Game = s.Game()
s.new_board(myCandyCrush, 8, 8)
cc.refill(myCandyCrush)

# Test code
def set_test_board_1(game: s.Game):
    game.board = [
        [s.Candy(color=s.COLOR.BLUE,    mode=s.MODE.N), s.Candy(color=s.COLOR.ORANGE,  mode=s.MODE.N), s.Candy(color=s.COLOR.YELLOW,  mode=s.MODE.N), s.Candy(color=s.COLOR.RED,     mode=s.MODE.N), s.Candy(color=s.COLOR.GREEN,   mode=s.MODE.N), s.Candy(color=s.COLOR.PURPLE,  mode=s.MODE.N), s.Candy(color=s.COLOR.BLUE,    mode=s.MODE.N), s.Candy(color=s.COLOR.GREEN,   mode=s.MODE.N)],
        [s.Candy(color=s.COLOR.ORANGE,  mode=s.MODE.N), s.Candy(color=s.COLOR.RED,     mode=s.MODE.N), s.Candy(color=s.COLOR.RED,     mode=s.MODE.N), s.Candy(color=s.COLOR.ORANGE,  mode=s.MODE.N), s.Candy(color=s.COLOR.YELLOW,  mode=s.MODE.N), s.Candy(color=s.COLOR.GREEN,   mode=s.MODE.N), s.Candy(color=s.COLOR.ORANGE,  mode=s.MODE.N), s.Candy(color=s.COLOR.GREEN,   mode=s.MODE.N)],
        [s.Candy(color=s.COLOR.YELLOW,  mode=s.MODE.N), s.Candy(color=s.COLOR.RED,     mode=s.MODE.N), s.Candy(color=s.COLOR.BLUE,    mode=s.MODE.N), s.Candy(color=s.COLOR.YELLOW,  mode=s.MODE.N), s.Candy(color=s.COLOR.ORANGE,  mode=s.MODE.N), s.Candy(color=s.COLOR.GREEN,   mode=s.MODE.N), s.Candy(color=s.COLOR.YELLOW,  mode=s.MODE.N), s.Candy(color=s.COLOR.RED,     mode=s.MODE.N)],
        [s.Candy(color=s.COLOR.GREEN,   mode=s.MODE.N), s.Candy(color=s.COLOR.ORANGE,  mode=s.MODE.N), s.Candy(color=s.COLOR.YELLOW,  mode=s.MODE.N), s.Candy(color=s.COLOR.RED,     mode=s.MODE.N), s.Candy(color=s.COLOR.BLUE,    mode=s.MODE.N), s.Candy(color=s.COLOR.YELLOW,  mode=s.MODE.N), s.Candy(color=s.COLOR.GREEN,   mode=s.MODE.N), s.Candy(color=s.COLOR.ORANGE,  mode=s.MODE.N)],
        [s.Candy(color=s.COLOR.RED,     mode=s.MODE.N), s.Candy(color=s.COLOR.RED,     mode=s.MODE.N), s.Candy(color=s.COLOR.RED,     mode=s.MODE.N), s.Candy(color=s.COLOR.YELLOW,  mode=s.MODE.N), s.Candy(color=s.COLOR.RED,     mode=s.MODE.N), s.Candy(color=s.COLOR.ORANGE,  mode=s.MODE.N), s.Candy(color=s.COLOR.RED,     mode=s.MODE.N), s.Candy(color=s.COLOR.BLUE,    mode=s.MODE.N)],
        [s.Candy(color=s.COLOR.RED,     mode=s.MODE.N), s.Candy(color=s.COLOR.YELLOW,  mode=s.MODE.N), s.Candy(color=s.COLOR.ORANGE,  mode=s.MODE.N), s.Candy(color=s.COLOR.GREEN,   mode=s.MODE.N), s.Candy(color=s.COLOR.BLUE,    mode=s.MODE.N), s.Candy(color=s.COLOR.YELLOW,  mode=s.MODE.N), s.Candy(color=s.COLOR.RED,     mode=s.MODE.N), s.Candy(color=s.COLOR.YELLOW,  mode=s.MODE.N)],
        [s.Candy(color=s.COLOR.RED,     mode=s.MODE.N), s.Candy(color=s.COLOR.GREEN,   mode=s.MODE.N), s.Candy(color=s.COLOR.RED,     mode=s.MODE.N), s.Candy(color=s.COLOR.ORANGE,  mode=s.MODE.N), s.Candy(color=s.COLOR.YELLOW,  mode=s.MODE.N), s.Candy(color=s.COLOR.BLUE,    mode=s.MODE.N), s.Candy(color=s.COLOR.GREEN,   mode=s.MODE.N), s.Candy(color=s.COLOR.ORANGE,  mode=s.MODE.N)],
        [s.Candy(color=s.COLOR.YELLOW,  mode=s.MODE.N), s.Candy(color=s.COLOR.ORANGE,  mode=s.MODE.N), s.Candy(color=s.COLOR.BLUE,    mode=s.MODE.N), s.Candy(color=s.COLOR.GREEN,   mode=s.MODE.N), s.Candy(color=s.COLOR.RED,     mode=s.MODE.N), s.Candy(color=s.COLOR.YELLOW,  mode=s.MODE.N), s.Candy(color=s.COLOR.ORANGE,  mode=s.MODE.N), s.Candy(color=s.COLOR.BLUE,    mode=s.MODE.N)],
    ]

myCandyCrush = s.Game()
s.new_board(myCandyCrush, 8, 8)
set_test_board_1(myCandyCrush)

c_print.print_board_int(myCandyCrush)
print("")

print(m.swap(myCandyCrush, s.Coords(3, 1), s.Coords(3, 0)))

c_print.print_board_int(myCandyCrush)
print("")

cc.match_and_destroy(myCandyCrush)
c_print.print_board_int(myCandyCrush)
print("")

cc.refill(myCandyCrush)
c_print.print_board_int(myCandyCrush)
# Test code end

#while True:
#    c_print.print_board_int(myCandyCrush)
#    print("")
#    # User makes Turn
#    # Special check for Manual Color Bomb
#    while cc.refill(myCandyCrush):
#
#        # Check all candies for any special formations
#        for i in range(myCandyCrush.COLS):
#            for j in range(myCandyCrush.ROWS):
#                cc.queue_new_specials(myCandyCrush, s.Coords(c=i, r=j))
#        
#        # Match and Destroy
#        
#        # Add the queued special candies to the board
#        cc.apply_special_candies(myCandyCrush)
#        
#        # Activate triggered special candies
#        cc.apply_special_candies(myCandyCrush)
