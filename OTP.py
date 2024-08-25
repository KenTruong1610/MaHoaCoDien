def otp_encrypt(plain_text, key):

    key = (key * (len(plain_text) // len(key) + 1))[:len(plain_text)]

    encrypted_text = []
    
    for i in range(len(plain_text)):
        char_value = ord(plain_text[i]) - ord('a')
        key_value = ord(key[i]) - ord('a')
        
        result_value = char_value + key_value
        
        if result_value >= 26:
            result_value = result_value - 26
        else: result_value = result_value
        
        encrypted_char = chr(result_value + ord('a'))
        encrypted_text.append(encrypted_char)
    
    return ''.join(encrypted_text)


M = input("Nhập họ và tên sinh viên (không dấu): ").lower()
K = "antt"  

encrypted_message = otp_encrypt(M, K)
print("Mã hóa OTP của", M, "với khóa", K, "là:", encrypted_message)
