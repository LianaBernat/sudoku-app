import pandas as pd

def sudoku_validator(grid):
    """
    Function to validate a Sudoku grid.
    The grid is a 9x9 DataFrame.

    A Sudoku is valid if and only if:
    1) A row contains all numbers from 1 to 9
    2) A column contains all numbers from 1 to 9
    3) Each of the nine 3x3 little squares contains numbers from 1 to 9
    """

    set_padrao={1,2,3,4,5,6,7,8,9}

    #testing rows(r) and columns(c)
    for index in range(9):
        r = set(grid.iloc[index,:])
        c= set(grid.iloc[:,index])
        if r!=set_padrao or c!= set_padrao:
            return False

    #testing the 3by3 blocks(block)
    for n in range(0,7,3):
        for m in range(0,7,3):
            block= set(grid.iloc[n:n+3, m:m+3].stack())
            if block!=set_padrao:
                return False

    return True
