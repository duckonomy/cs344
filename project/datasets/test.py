import pandas as pd

df = pd.read_csv('ratings.txt', sep='\t', lineterminator='\r')
df.head(33)
