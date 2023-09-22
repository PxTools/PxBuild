import pandas as pd

data = {
    'KJONN': ['A', 'B', 'A','B'],
    'ALDER': ['X', 'X', 'Y','Y'],
    'value_VEKT': [1, 2, 3, 4],
    'value_PRIS': [5, 6, 7, 8],
    'symbol_VEKT': ['ax1', None, 's13', None],
    'symbol_PRIS': ['ax2', 'bx2', 's23',None],
    'attrubute1': ['axQ', 'bxW', 'ayE','byR'],
}


data = {
    'KJONN': ['M', 'K', 'M','K'],
    'ALDER': ['40', '40', '80','80'],
    'value_VEKT': [1, 3, 5, 7],
    'value_PRIS': [2, 4, 6, 8],
    'symbol_VEKT': ['ax1', None, 's13', None],
    'symbol_PRIS': ['ax2', 'bx2', 's23',None]
}

    #/// MINDEX:
    #/// We need to convert a point(one value for each variable) in 
    #/// the cube to a number(the index of the array).
    #///
    #/// k,j, i... 1-based counters
    #/// Nx number of values for x
    #/// Factor_k=Nj*Ni
    #/// Factor_j= Ni
    #/// Factor_i = 1
    #/// index = Factor_k*(k-1) + Factor_j*(j-1) + Factor_i(i-1) </remarks>
    #/// </summary>

df = pd.DataFrame(data)
print("Slik det ligger i parquet/cvs/statdata")
print(df)

# Use pd.wide_to_long to reshape the DataFrame
result_df = pd.wide_to_long(df, stubnames=['value', 'symbol'], i=['KJONN', 'ALDER'], j='CONT', sep='_', suffix='(!?VEKT|PRIS)')

# Reset the index and rename columns
result_df.reset_index(inplace=True)

# Print or save the result
print("Statistikk variablen som kolonne:")
print(result_df)



