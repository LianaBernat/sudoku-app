
'''
app/game.py
Sudoku Game
Main script to run the Sudoku game.
Run this script from the root folder using:
    python -m app.game
'''

from app.sudoku import (
    show_move_results,
    show_grid,
    sudoku_grid_generator,
    sudoku_initial_playable_grid)
import pandas as pd
import numpy as np


def main():
    '''Main function to run the Sudoku game.
    It initializes the game, generates a Sudoku grid,
    and handles user input for playing the game.
    '''
    grid_origin = pd.DataFrame([
    [7,8,4,  1,5,9,  3,2,6],
    [5,3,9,  6,7,2,  8,4,1],
    [6,1,2,  4,3,8,  7,5,9],

    [9,2,8,  7,1,5,  4,6,3],
    [3,5,7,  8,4,6,  1,9,2],
    [4,6,1,  9,2,3,  5,8,7],

    [8,7,6,  3,9,4,  2,1,5],
    [2,4,3,  5,6,1,  9,7,8],
    [1,9,5,  2,8,7,  6,3,4]
    ])

    grid_solution = sudoku_grid_generator(grid_origin)

    print()
    print('🤔 SUDOKU GAME')
    print('Welcome!')
    print('Choose a row, a column and a number from 1 to 9.')
    print("To exit, press 'q'")

    print()
    while True:
        d_level = input('Choose difficulty level (1, 2, or 3): ').strip().lower()

        if d_level.lower()=='q':
            exit()

        if str(d_level).isdigit() and int(d_level) in [1,2,3]:
            d_level = int(d_level)
            break
        print('❌ Invalid input. Please choose a difficulty level (1, 2, or 3).')

    grid_init =  sudoku_initial_playable_grid(grid_solution, difficulty_level=d_level)

    while (grid_init==0).sum().sum()>0:
        print(show_grid(grid_init))

        l=input('Choose row (1-9): ')
        if l.lower()=='q':
            exit()
        c=input('Choose column (1-9): ')
        if c.lower()=='q':
            exit()

        try:
            l= int(l)-1
            c=int(c)-1
            if grid_init.iloc[l,c]!=0:
                show_move_results("⚠️  Position is already fulfilled")

            else:
                n=int(input('Choose number (1-9): '))
                if grid_solution.iloc[l,c]==n:
                    grid_init.iloc[l,c]=n
                    show_move_results('✅ Good Move. Continue!')
                else:
                    show_move_results("❌ That's not correct. Try again!")

        except:
            show_move_results('❌ invalid row, column or number to fulfill. Use 1-9.')


    show_move_results( '🎉 Congratulations! You Won!')
    print(show_grid(grid_init))



if __name__=='__main__':
    main()
