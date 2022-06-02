from typing import List

board = [['o', '-', 'o'],
         ['-', 'o', 'x'],
         ['x', 'x', 'o']]
        
board1 = [['-', '-', '-'],
          ['-', 'o', 'o'],
          ['x', 'x', 'x']]

def checkLine(symb: str, board: List[List])-> bool:
    for line in range(3):
        lin = True
        col = True
        for column in range(3):
            if board[line][column] != symb:
                 lin = False
            if board[column][line] != symb: 
                col = False
        if lin or col: 
            return True
    return False

def checkDiagonal(symb: str, board: List[List])-> bool:
    diagonal = True
    rev_diagonal = True
    for i in range(3):
        if board[i][i] != symb:
            diagonal = False
        if board[i][3-i-1] != symb:
            rev_diagonal = False
    if diagonal or rev_diagonal:
        return True
    else: 
        return False

def tic_tac_toe_checker(board: List[List]) -> str:
    """
    >>> line = [['o', 'x', 'o'],['x', 'o', 'o'],['o', 'o', 'x']]
    >>> print(tic_tac_toe_checker(line))
    o wins!
    >>> line = [['-', '-', 'o'],['-', 'x', 'o'],['x', 'o', 'x']]
    >>> print(tic_tac_toe_checker(line))
    unfinished!
    >>> line = [['o', 'x', 'o'],['o', 'x', 'o'],['x', 'o', 'x']]
    >>> print(tic_tac_toe_checker(line))
    draw!
    :param board:
    :return:
    """
    if checkLine('o', board) or checkDiagonal('o', board):
        return 'o wins'
    elif checkLine('x', board) or checkDiagonal('x', board):
        return 'x wins'
    else:
        return 'unfinished'


print(tic_tac_toe_checker(board)) # o wins
print(tic_tac_toe_checker(board1)) # x wins