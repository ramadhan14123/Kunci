def enkripsi(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def dekripsi(private_key, ciphertext):
    d, n = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)

# Kunci publik dan privat
public_key = map(int, input("Masukkan kunci publik (e, n) dengan dipisahkan oleh spasi: ").split())
private_key = map(int, input("Masukkan kunci privat (e, n) dengan dipisahkan oleh spasi: ").split())

# Pesan yang ingin dienkripsi
message = input("Masukkan Teks: ")
print("Pesan asli:", message)

# Enkripsi pesan
pesan_enkripsi = enkripsi(public_key, message)
print("Pesan terenkripsi:", pesan_enkripsi)

# Dekripsi pesan
pesan_denkripsi = dekripsi(private_key, pesan_enkripsi)
print("Pesan yang didekripsi:", pesan_denkripsi)
