#Função que monta o tabuleiro
import numpy as np
import pandas as pd

def show_grid(grid_df):
    grid='\n'
    for index, row in grid_df.iterrows():
        a= row.iloc[0:3].to_string(index=False, header=False).replace('\n', ' ')
        b= row.iloc[3:6].to_string(index=False, header=False).replace('\n', ' ')
        c= row.iloc[6:].to_string(index=False, header=False).replace('\n', ' ')
        grid+= a + ' | ' + b + ' | '+ c + '\n'
        if index==2 or index==5:
            grid+= '-'*21+'\n'
    
    return grid.replace('0','.')
