def num_letters(n_row, n_col):
    return(n_row*n_col)-(n_col-2)*(n_row-2)

assert num_letters(3, 4) == 10
assert num_letters(13, 4) == 30
assert num_letters(4, 4) == 12
assert num_letters(6, 4) == 16
assert num_letters(6, 7) == 22
print("Good assertions.")


