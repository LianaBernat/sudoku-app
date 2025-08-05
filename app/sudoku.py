'''app/sudoku.py
Auxiliary functions for the Sudoku game.
These functions are used to display the Sudoku grid and show move results.'''


import numpy as np
import pandas as pd
import os

def show_grid(grid_df):
    '''
    function to display the Sudoku grid in a readable format.
    It formats the grid into a string representation with rows and columns.
    '''
    grid='\n'
    for index, row in grid_df.iterrows():
        a= row.iloc[0:3].to_string(index=False, header=False).replace('\n', ' ')
        b= row.iloc[3:6].to_string(index=False, header=False).replace('\n', ' ')
        c= row.iloc[6:].to_string(index=False, header=False).replace('\n', ' ')
        grid+= a + ' | ' + b + ' | '+ c + '\n'
        if index==2 or index==5:
            grid+= '-'*21+'\n'

    return grid.replace('0','.')


def show_move_results(message):
    '''
    function to display messages after a move.
    It clears the console and prints the message.
    '''
    os.system('clear')
    print()
    print(message)



def sudoku_grid_generator(grid_origin, n_rotations=1, n_blocks_3by9=1,
                          n_blocks_9by3=1, n_swap_rows_3by9=1,
                          n_swap_cols_9by3=1, n_swap_numbers=5):
    '''
    Function to generate a random Sudoku grid based on the original grid.
    It applies a series of transformations to create a new valid Sudoku grid.
    Parameters:
    - grid_origin: The original Sudoku grid to base the transformations on.
    - n_rotations: Number of random rotations to apply to the grid.
    - n_blocks_3by9: Number of times to shuffle 3x9 blocks.
    - n_blocks_9by3: Number of times to shuffle 9x3 blocks.
    - n_swap_rows_3by9: Number of times to swap rows within 3x9 blocks.
    - n_swap_cols_9by3: Number of times to swap columns within 9x3 blocks.
    - n_swap_numbers: Number of times to swap two numbers in the grid.
    '''

    grid_random=grid_origin.copy()

    for _ in range(n_rotations):
        grid_random=rotation_random(grid_random)

    for _ in range(n_blocks_3by9):
        grid_random=blocks_3by9_9by3_random(grid_random, split='3by9')

    for _ in range(n_blocks_9by3):
        grid_random=blocks_3by9_9by3_random(grid_random, split='9by3')

    for _ in range(n_swap_rows_3by9):
        grid_random=swap_rows_columns_random(grid_random, split='3by9')

    for _ in range(n_swap_cols_9by3):
        grid_random=swap_rows_columns_random(grid_random, split='9by3')

    for _ in range(n_swap_numbers):
        grid_random=swap_numbers_random(grid_random)

    grid_random = grid_random.reset_index(drop=True)
    grid_random.columns = range(9)
    return grid_random


def rotation_random(grid_origin):

    '''
    function to randomly rotate the original Sudoku grid.
    It randomly chooses a rotation angle (90, 180, or 270 degrees)
    '''

    rotation=np.random.choice([90,180,270],1)

    if rotation==90:
        grid_random=grid_origin.T.iloc[::-1]
    elif rotation==180:
        grid_random=grid_origin.iloc[::-1,::-1]
    else:
        grid_random=grid_origin.T.iloc[:,::-1]

    return grid_random


def blocks_3by9_9by3_random(grid_origin, split='3by9'):
    '''
    function to randomly shuffle blocks of the Sudoku grid.
    It splits the grid into 3x9 or 9x3 blocks and shuffles them.
    The split parameter determines the orientation of the blocks.
    '''
    ord=np.random.choice([1,2,3],3,replace=False)

    if split=='3by9':
        m1= grid_origin.iloc[0:3,:]
        m2 =grid_origin.iloc[3:6,:]
        m3 =grid_origin.iloc[6:9,:]

        m_dict={'m1':m1,'m2':m2,'m3':m3}
        m_random= pd.concat([m_dict['m'+str(ord[0])],
                             m_dict['m'+str(ord[1])],
                             m_dict['m'+str(ord[2])]], axis=0)
    else:
        m1= grid_origin.iloc[:,0:3]
        m2 =grid_origin.iloc[:,3:6]
        m3 =grid_origin.iloc[:,6:9]

        m_dict={'m1':m1,'m2':m2,'m3':m3}
        m_random= pd.concat([m_dict['m'+str(ord[0])],
                             m_dict['m'+str(ord[1])],
                             m_dict['m'+str(ord[2])]], axis=1)

    return m_random


def swap_rows_columns_random(grid_origin, split= '3by9'):

    '''function to randomly swap rows (or columns) within the 3x9 (or 9x3)
    blocks of the Sudoku grid.
    It swaps rows within the specified split orientation (3by9 or 9by3).
    '''
    if  split=='3by9':
        ord=np.random.choice([0,1,2],3,replace=False)
        m1= grid_origin.iloc[0:3,:].iloc[ord,:]

        ord=np.random.choice([0,1,2],3,replace=False)
        m2 =grid_origin.iloc[3:6,].iloc[ord,:]

        ord=np.random.choice([0,1,2],3,replace=False)
        m3 =grid_origin.iloc[6:9,:].iloc[ord,:]

        grid_random= pd.concat([m1,m2,m3], axis=0)

    else:
        ord=np.random.choice([0,1,2],3,replace=False)
        m1= grid_origin.iloc[:,0:3].iloc[:,ord]

        ord=np.random.choice([0,1,2],3,replace=False)
        m2 =grid_origin.iloc[:,3:6].iloc[:,ord]

        ord=np.random.choice([0,1,2],3,replace=False)
        m3 =grid_origin.iloc[:,6:9].iloc[:,ord]

        grid_random= pd.concat([m1,m2,m3], axis=1)

    return grid_random


def swap_numbers_random(grid_origin):
    '''
    function to randomly swap two numbers in the Sudoku grid.
    It randomly selects two distinct numbers from 1 to 9 and swaps them
    throughout the grid.
    '''
    n1, n2 = np.random.choice(range(1,10), 2, replace=False)
    grid_random=grid_origin.replace(n1,0).replace(n2,n1).replace(0,n2)

    return grid_random


def sudoku_initial_playable_grid(grid_solution, difficulty_level=2):

    '''
    function to create an initial playable Sudoku grid based on the solution.
    It generates a grid with a specified percentage of empty cells based on
    the difficulty level.

    parameters:
    - grid_solution: The solution grid to base the initial grid on.
    - difficulty_level: Difficulty level of the Sudoku game (1, 2, or 3).
        - 1: Easy (10% empty cells)
        - 2: Medium (20% empty cells)
        - 3: Hard (40% empty cells)
    '''
    try:
        difficulty_level = int(difficulty_level)
        dict_difficulty = {1: 0.1, 2: 0.2, 3: 0.4}
        percent_null= dict_difficulty[difficulty_level]

        sort_nulls = np.random.choice(81, int(percent_null*81), replace=False)
        i =[int(d/9)  for d in sort_nulls]
        j = [d%9 for d in sort_nulls]

        grid_init = grid_solution.copy()
        grid_init.values[i, j]=0

    except:
        show_move_results('❌ Invalid difficulty level. Please choose 1, 2, or 3.')

    return grid_init
