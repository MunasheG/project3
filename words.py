import numpy as np

def num_letters(n_row, n_col):
    return(n_row*n_col)-(n_col-2)*(n_row-2)

#assert num_letters(13, 4) == 30
#assert num_letters(4, 4) == 12
#assert num_letters(6, 4) == 16
#assert num_letters(6, 7) == 22
#print("Good assertions.")

#loop4.csv

data4 = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')

words4 = []

rows, columns = data4.shape

for r in range(rows):
    for c in range(columns):
        if r == 0 or r == rows - 1 or c == 0 or c == columns - 1:
            words4.append(str(data4[r, c]))

assert len(words4) == num_letters(rows, columns)

print(words4)

#loop3.csv

data3 = np.loadtxt("loop3.csv", delimiter=",", dtype=str, encoding = 'utf8')

words3 = []

rows, columns = data3.shape

for r in range(rows):
    for c in range(columns):
        if r == 0 or r == rows - 1 or c == 0 or c == columns - 1:
            words3.append(str(data3[r, c]))

assert len(words3) == num_letters(rows, columns)

print(words3)

#loop2.csv

data2 = np.loadtxt("loop2.csv", delimiter=",", dtype=str, encoding = 'utf8')

words2 = []

rows, columns = data2.shape

for r in range(rows):
    for c in range(columns):
        if r == 0 or r == rows - 1 or c == 0 or c == columns - 1:
            words2.append(str(data2[r, c]))

assert len(words2) == num_letters(rows, columns)

print(words2)

#loop1.csv

data1 = np.loadtxt("loop3.csv", delimiter=",", dtype=str, encoding = 'utf8')

words1 = []

rows, columns = data1.shape

for r in range(rows):
    for c in range(columns):
        if r == 0 or r == rows - 1 or c == 0 or c == columns - 1:
            words1.append(str(data1[r, c]))

assert len(words1) == num_letters(rows, columns)

print(words1)


