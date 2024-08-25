def vc_repeat_key(message, key):
    def shift_char(c, k):
        if c.isalpha():  
            base = ord('a') if c.islower() else ord('A')
            return chr((ord(c) - base + k) % 26 + base)
        return c

    key = (key * (len(message) // len(key) + 1))[:len(message)]
    key_shifts = [ord(k.lower()) - ord('a') for k in key]

    encoded_message = ''.join(shift_char(m, k) for m, k in zip(message, key_shifts))
    return encoded_message, key

M = input("Nhập họ tên sinh viên (không dấu): ").lower()
K = "antt"

encoded_message_repeat, key1 = vc_repeat_key(M, K)
print("Mã hóa Vigenère với lặp khóa: ",encoded_message_repeat)
print("Khóa được dùng là: ",key1)