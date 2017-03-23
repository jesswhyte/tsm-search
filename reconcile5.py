import pandas as pd

master = pd.read_csv('./ls.csv', sep=',', index_col=0, header=None)
tfrbl = pd.read_csv('./tfrbl-csv.csv', sep=',', index_col=0, header=None)

res = pd.concat([master, tfrbl], axis=1, join='inner')
res.to_csv('./output.csv', mode='w', sep=',')
