
from sudoku import show_grid
from sudoku import show_move_results
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
percent_null= 0.4
sort_nulls = np.random.choice(81, int(percent_null*81), replace=False)
i =[int(d/9)  for d in sort_nulls]
j = [d%9 for d in sort_nulls]

grid_init = grid_solution.copy()
grid_init.values[i, j]=0

#iniciando o jogo
if __name__=='__main__':
    print()
    print('🤔 SUDOKU GAME')
    print('Welcome!')
    print('Choose a row, a column and a number from 1 to 9.')
    print("To exit, press 'q' instead of a row or column number.")


    while (grid_init==0).sum().sum()>0:
        print(show_grid(grid_init))

        l=input('Choose row (1-9): ')
        if l=='q':
            exit()
        c=input('Choose column (1-9): ')
        if c=='q':
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
