
from sudoku import show_grid
import pandas as pd
import numpy as np


#Primeiro versão usando um grid fixo
#grid solução fixo
grid_solution = pd.DataFrame([
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

#montando um grid inicial com base na solução fixa
#substituindo algumas linhas e colunas por zero

percent_null= 0.3
sort_nulls = np.random.choice(81, int(percent_null*81), replace=False)
i =[int(d/9)  for d in sort_nulls]
j = [d%9 for d in sort_nulls]

grid_init = grid_solution.copy()
grid_init.values[i, j]=0

#iniciando o jogo
print('JOGO DE SUDOKU')
print(show_grid(grid_init))