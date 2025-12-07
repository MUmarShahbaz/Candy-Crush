import main as cc
import structs as s
import console_print as c_print


# init game
myCandyCrush : s.Game = s.Game()
s.new_board(myCandyCrush, 8, 8)
cc.refill(myCandyCrush)

while True:
    c_print.print_board_int(myCandyCrush)
    print("")
    # User makes Turn
    # Special check for Manual Color Bomb
    while cc.refill(myCandyCrush):

        # Check all candies for any special formations
        for i in range(myCandyCrush.COLS):
            for j in range(myCandyCrush.ROWS):
                cc.queue_new_specials(myCandyCrush, s.Coords(c=i, r=j))
        
        # Match and Destroy
        
        # Add the queued special candies to the board
        cc.apply_special_candies(myCandyCrush)
        
        # Activate triggered special candies
        cc.apply_special_candies(myCandyCrush)
