def este_prim(numar):
    if numar < 2:
        return False
    if numar == 2:
        return True
    if numar % 2 == 0:
        return False
    for i in range(3, int(numar**0.5) + 1, 2):
        if numar % i == 0:
            return False
    return True

def gaseste_perechi_goldbach(n):
    perechi = []
    for p in range(2, n // 2 + 1):
        q = n - p
        if este_prim(p) and este_prim(q):
            perechi.append((p, q))
    return perechi

def main():
    while True:
        try:
            valoare_introdusa = input("Introduceți un număr natural par mai mare decât 2 (n > 2): ")
            n = int(valoare_introdusa)
            
            if n <= 2:
                print("Eroare: Numărul trebuie să fie mai mare decât 2.")
            elif n % 2 != 0:
                print("Eroare: Numărul trebuie să fie par.")
            else:
                break
        except ValueError:
            print("Eroare: Vă rugăm să introduceți un număr valid.")

    perechi = gaseste_perechi_goldbach(n)
    
    if perechi:
        rezultate_formatate = " și ".join([f"{p} + {q}" for p, q in perechi])
        print(f"Pentru n = {n}, perechile sunt: {rezultate_formatate}")
    else:
        print(f"Nu s-au găsit perechi pentru numărul {n}.")

if __name__ == "__main__":
    main()