# PandasLoadDataBenchmarks

There is a 4x difference by only changing the datatype.
```python
pd.read_csv('data.csv', dtype=dict(x='string'))
```
and
```python
pd.read_csv('data.csv', dtype=dict(x='int32'))
```

There is a 500x difference by reading the data in via a binary format.
```python
with open('df1.df', 'rb') as f:
    pickle.load(f)
```
    




```bash
$ lscpu | grep "Model name"
Model name:                         AMD Ryzen 9 7950X 16-Core Processor
$ python main.py
Time to read string: 0.1951918601989746
Time to read int32: 0.04430508613586426
Time to read binary format file: 0.0003447532653808594
```

