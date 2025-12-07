###
#import temp
#import console_print
#
# main.refill()
#
#temp.board = [
#    [ 5, 7, 7, 6, 2, 2, 3, 2 ],
#    [ 6, 7, 1, 3, 7, 3, 1, 3 ],
#    [ 2, 3, 3, 3, 4, 5, 2, 7 ],
#    [ 2, 5, 6, 3, 5, 5, 2, 3 ],
#    [ 7, 6, 5, 4, 2, 3, 4, 2 ],
#    [ 4, 4, 5, 5, 6, 3, 3, 3 ]
#]
#
#console_print.print_board_int()
#print("----------------------------")
#
#while temp.match_and_destroy():
#    console_print.print_board_int()
#    print("")
#    temp.refill()
#    console_print.print_board_int()
#    print("----------------------------")
#

import main as cc
import structs as s
import console_print as c_print

myCandyCrush : s.Game = s.Game()
s.new_board(myCandyCrush, 5, 8)
cc.refill(myCandyCrush)
c_print.print_board_int(myCandyCrush)