import pandas as pd
import pickle
from time import time


ROWS = 1000000

with open("data.csv", 'w') as f:
    f.write('x\n')
    f.write('\n'.join(str(i) for i in range(ROWS)))


start = time()
df = pd.read_csv('data.csv', dtype=dict(x='string'))
print(f'Time to read string: {time()-start}')

start = time()
df = pd.read_csv('data.csv', dtype=dict(x='int32'))
print(f'Time to read int32: {time()-start}')

with open('df1.df', 'wb') as f:
    pickle.dump(df, f)

start = time()
with open('df1.df', 'rb') as f:
    pickle.load(f)
print(f'Time to read binary format file: {time()-start}')

