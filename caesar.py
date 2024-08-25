def caesar_cipher(message, k):
    def shift_char(c, k):
        if c.isalpha():  
            base = ord('a') if c.islower() else ord('A')
            return chr((ord(c) - base + k) % 26 + base)
        return c

    return ''.join(shift_char(c, k) for c in message)

M = input("Nhập họ tên sinh viên (không dấu): ")
birth_date = int(input("Nhập ngày sinh (1-31): "))

if 0 < birth_date <= 31: 
	K = birth_date if birth_date <= 26 else birth_date - 26
else:
	print("Không có ngày sinh trên 31")
	K = 0

encoded_message = caesar_cipher(M, K)

print("Bản tin sau khi mã hóa Caesar là:", encoded_message)
