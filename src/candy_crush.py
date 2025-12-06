import main
import auxillary

# main.refill()

main.board = [
    [ 5, 7, 7, 6, 2, 2, 3, 2 ],
    [ 6, 7, 1, 3, 7, 3, 1, 3 ],
    [ 2, 3, 3, 3, 4, 5, 2, 7 ],
    [ 2, 5, 6, 3, 5, 5, 2, 3 ],
    [ 7, 6, 5, 4, 2, 3, 4, 2 ],
    [ 4, 4, 5, 5, 6, 3, 3, 3 ]
]

auxillary.print_board_int()
print("----------------------------")

while main.detect_and_destroy():
    auxillary.print_board_int()
    print("")
    main.refill()
    auxillary.print_board_int()
    print("----------------------------")