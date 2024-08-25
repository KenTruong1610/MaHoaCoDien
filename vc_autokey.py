def vc_autokey(message, key):
    def shift_char(c, k):
        if c.isalpha():  
            base = ord('a') if c.islower() else ord('A')
            return chr((ord(c) - base + k) % 26 + base)
        return c

    extended_key = (key + message)[:len(message)]
    key_shifts = [ord(k.lower()) - ord('a') for k in extended_key]

    encoded_message = ''.join(shift_char(m, k) for m, k in zip(message, key_shifts))
    return encoded_message, extended_key

M = input("Nhập họ tên sinh viên (không dấu): ").lower()
K = "antt"

encoded_message_autokey, extended_key_autokey = vc_autokey(M, K)
print("Mã hóa Vigenère với khóa tự động: ",encoded_message_autokey)
print("Khóa đã sử dụng (khóa tự động): ",extended_key_autokey)
