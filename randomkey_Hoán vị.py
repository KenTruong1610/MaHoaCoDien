import string
import random

def random_key():
    alphabet = string.ascii_uppercase  
    key = ''.join(random.sample(alphabet, len(alphabet)))
    return key

def cipher(message):
    key = random_key()  
    alphabet_upper = string.ascii_uppercase  
    alphabet_lower = string.ascii_lowercase  
    
    map_upper = dict(zip(alphabet_upper, key))  
    map_lower = dict(zip(alphabet_lower, key.lower()))  
    encrypted_message = ''.join(
        map_upper.get(char, map_lower.get(char, char))
        for char in message
    )
    return encrypted_message, key

M = input("Nhập họ tên sinh viên (sử dụng ký tự không dấu): ")

encrypted_message, key = cipher(M)
print("Bản tin đã mã hóa: ",encrypted_message)
print("Khóa được sử dụng: ",key)
