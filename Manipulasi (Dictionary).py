# Penambahan, penghapusan, dan perulangan pada dictionary 
data_dict = {'a': 1, 'b': 2, 'c': 3}

# Penambahan elemen ke dalam dictionary 
data_dict['d'] = 4

# Penghapusan elemen dari dictionary 
del data_dict['b']

# Perulangan pada dictionary (kunci) 
for key in data_dict: 
    print(key)

# Perulangan pada dictionary (nilai) 
for value in data_dict.values(): 
    print(value)
    