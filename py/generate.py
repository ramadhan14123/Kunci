from sympy import randprime

def generate_prime(digit):
    if digit == 1:
        return 2  # 2 adalah bilangan prima terkecil dan jika program menginputkan 1 digit maka akan selalu menampilkan angka 2
    batas_terkecil = 10**(digit - 1)
    batas_terbesar = 10**digit - 1
    return randprime(batas_terkecil, batas_terbesar)

def main():
    while True:
        Jumlah_digit = int(input("Masukkan jumlah digit untuk bilangan prima: "))
        angka_prima = generate_prime(Jumlah_digit)
        print(f"Bilangan prima {Jumlah_digit}-digit yang dihasilkan adalah: {angka_prima}")
        
        choice = input("Ulang Program? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()
