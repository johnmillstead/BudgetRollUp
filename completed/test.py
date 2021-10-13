# Budget Roll-up
# Used to roll-up individual budgets into one master budget

#import libraries
import pandas as pd
import glob

# import csv files
path = '*.csv'
files = glob.glob(path)

# loop thru
all_data = pd.DataFrame()
for f in files:
    df = pd.read_csv(f)
    all_data = pd.concat([all_data,df])

all_data.to_csv('all.csv', index=False)

