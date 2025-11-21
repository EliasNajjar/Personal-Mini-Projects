def solveSudoku(board) -> None:
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.': # find first open spot
                for k in range(1,10): # test numbers 1 to 9
                    board[i][j] = str(k) # set value in board
                    seen = []
                    for l in range(9):
                        if board[i][l] != '.' and l != j: # find numbers in same row
                            seen.append(board[i][l])
                        if board[l][j] != '.' and l != i: # find numbers in same column
                            seen.append(board[l][j])
                    for l in range(i // 3 * 3, i // 3 * 3 + 3): # lower to higher multiple of 3
                        for o in range(j // 3 * 3, j // 3 * 3 + 3):
                            if board[l][o] != '.' and (l != i or o != j): # find numbers in same box
                                seen.append(board[l][o])
                    if board[i][j] not in seen: # valid if number is not the same as another in the row, column, or box
                        solveSudoku(board) # solve recursively with the new number
                        complete = True
                        for l in range(8,-1,-1):
                            for o in range(8,-1,-1):
                                if board[l][o] == '.': # board has a '.' so it is incomplete
                                    complete = False
                                    break
                            if not complete:
                                break
                        if complete: # if the number is valid and the board is complete, end before next number
                            return
                board[i][j] = '.' # if no number 1-9 works, a previous number is wrong; set back to '.' and go back
                return

b = [ # use dots for open spaces, keep numbers as strings
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
solveSudoku(b)
for i in b:
    print(i)