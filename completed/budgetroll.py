# Budget Roll-up
# Used to roll-up individual budgets into one master budget

#import libraries
import pandas as pd
import glob

# import excel files
path = '*.xlsx'
files = glob.glob(path)

# loop thru
combined_files = pd.DataFrame()
for i in files:
    df = pd.read_excel(i, index_col=None,
                       skiprows=11, nrows=147, usecols='D:P')
    combined_files = pd.concat([combined_files, df])

combined_files.to_excel('output.xlsx', index=False)
