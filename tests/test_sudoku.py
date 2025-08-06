'''
Sudoku Validator Test
This module contains tests for the Sudoku validator function.
It checks if the Sudoku grid is valid according to the rules of Sudoku.
'''

import pandas as pd
import unittest
from app.sudoku import sudoku_grid_generator
from tests.sudoku_validator import sudoku_validator

class SudokuValidatorTest(unittest.TestCase):
    def test_grid_origin(self):
        '''
        Test the original Sudoku grid.
        It checks if the original grid is valid according to Sudoku rules.
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

        solver = sudoku_validator(grid_origin)
        self.assertTrue(solver)

    def test_grid_generated(self):
        '''
        Test the function used to generated a random Sudoku grid.
        It checks if one generated grid is valid according to Sudoku rules.
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

        grid_generated = sudoku_grid_generator(grid_origin)
        solver = sudoku_validator(grid_generated)
        self.assertTrue(solver)


    def test_invalid_grid(self):
        '''
        Test an invalid Sudoku grid.
        It checks if the validator correctly identifies an invalid grid.
        '''
        grid_invalid = pd.DataFrame([
            [7,8,5,  1,5,9,  3,2,6],
            [5,3,9,  6,7,2,  8,4,1],
            [6,1,2,  4,3,8,  7,5,9],

            [9,2,8,  7,1,5,  4,6,3],
            [3,5,7,  7,4,6,  1,9,2],
            [4,6,1,  9,2,3,  5,8,7],

            [8,7,6,  3,9,4,  2,1,5],
            [2,4,3,  5,6,1,  9,7,8],
            [1,9,5,  2,8,7,  6,3,4]
        ])

        solver = sudoku_validator(grid_invalid)
        self.assertEqual(solver,False)
