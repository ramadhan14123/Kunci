import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def invers_modular(e, M):
    d, x1, x2, y1 = 0, 0, 1, 1
    sisa_sementara = M
    
    while e > 0:
        hasil_bagi = sisa_sementara // e  
        sisa_baru = sisa_sementara - hasil_bagi * e 
        sisa_sementara, e = e, sisa_baru  
        
        x = x2 - hasil_bagi * x1
        y = d - hasil_bagi * y1
        
        x2, x1 = x1, x
        d, y1 = y1, y
    
    if sisa_sementara == 1:
        return d + M


def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Kedua angka harus prima.')
    elif p == q:
        raise ValueError('p dan q tidak boleh sama')
    
    n = p * q
    M = (p-1) * (q-1)
    
    e = random.randrange(1, M)
    g = gcd(e, M)
    while g != 1:
        e = random.randrange(1, M)
        g = gcd(e, M)
    
    d = invers_modular(e, M)
    
    return ((e, n), (d, n))

def main():
    p = int(input("Masukkan bilangan prima p: "))
    q = int(input("Masukkan bilangan prima q: "))
    print("Menghasilkan pasangan kunci...")
    public, private = generate_keypair(p, q)
    print("Kunci publik Anda adalah (e, n): ", public)
    print("Kunci privat Anda adalah (d, n): ", private)

if __name__ == '__main__':
    main()
