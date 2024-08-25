import numpy as np

def create_permutation_order(keyword):
    return sorted(range(len(keyword)), key=lambda k: keyword[k])

def encrypt_message(fullname, keyword):
    message = fullname.replace(" ", "")
    
    num_columns = len(keyword)
    num_rows = (len(message) + num_columns - 1) // num_columns 
    
    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]
    
    for i in range(len(message)):
        grid[i // num_columns][i % num_columns] = message[i]
    
    for i in range(len(message), num_rows * num_columns):
        grid[i // num_columns][i % num_columns] = 'x'
    
    permutation_order = create_permutation_order(keyword)
    
    encrypted_message = ''
    for col in permutation_order:
        for row in range(num_rows):
            if grid[row][col] != '':
                encrypted_message += grid[row][col]
    
    return encrypted_message, grid, permutation_order

K = input("Nhập họ và tên: ")
keyword = input("Nhập khóa (keyword): ")

encrypted_message, matrix, order = encrypt_message(K, keyword)

print("\nMa trận ban đầu:")
for row in matrix:
    print(' '.join(row))

print("\nThứ tự hoán vị các cột:", order)

print("\nBản mã:", encrypted_message)
