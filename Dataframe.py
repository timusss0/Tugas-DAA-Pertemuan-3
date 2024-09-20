import pandas as pd

df = pd.DataFrame([
    ['1', 'Fares', 32, True],
    ['2', 'Elena', 23, False],
    ['3', 'Steven', 40, True]
])
df.columns = ['id', 'name', 'age', 'decision']
print(df)


#Row Selection
df.iloc[1:3,:]
df[df.age>30]


data = {'satu': [1,1,1,1,1],
        'dua' : [2,2,2,2,2],
        'tiga': [3,3,3,3,3]}
df = pd.DataFrame(data, index=['a','b','c','d','e'])
df.head()


#Latihan
df = pd.DataFrame([
    ['1', 'Informatika', 50, 30, 20],
    ['2', 'Sistem Informasi', 55, 30, 25],
    ['3', 'Teknik Sipil', 40, 30, 10]
])

df.columns = ['No', 'Prodi', 'Mahasiswa', 'Laki-Laki', 'Perempuan']
print(df)
