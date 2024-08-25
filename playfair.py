def playfair(key):
    alphabet = "abcdefghiklmnopqrstuvwxyz"  
    matrix = []
    used_letters = set()

    for char in key:
        if char not in used_letters and char != 'j':
            matrix.append(char)
            used_letters.add(char)

    for char in alphabet:
        if char not in used_letters:
            matrix.append(char)
            used_letters.add(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def p_en(message, key):
    matrix = playfair(key)
    print("Bảng mã Playfair (ma trận 5x5):")
    for row in matrix:
        print(' '.join(row))
    print()  
    #Thêm chữ X nếu bản tin cần
    message = message.replace('j', 'i')
    pm = ""
    i = 0
    while i < len(message):
        char1 = message[i]
        if i + 1 < len(message):
            char2 = message[i + 1]
            if char1 == char2:
                pm += char1 + 'x'
                i += 1
            else:
                pm += char1 + char2
                i += 2
        else:
            pm += char1 + 'x'
            i += 1

    # Mã hóa thông điệp
    encrypted_message = ""
    for i in range(0, len(pm), 2):
        row1, col1 = find(matrix, pm[i])
        row2, col2 = find(matrix, pm[i + 1])

        if row1 == row2:
            encrypted_message += matrix[row1][(col1 + 1) % 5]
            encrypted_message += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_message += matrix[(row1 + 1) % 5][col1]
            encrypted_message += matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_message += matrix[row1][col2]
            encrypted_message += matrix[row2][col1]

    return encrypted_message

M = input("Nhập họ và tên sinh viên (không dấu): ").lower()
K = "antt"

encrypted_message = p_en(M, K)
print("Mã hóa Playfair của",M,"với khóa",K,"là:",encrypted_message)
