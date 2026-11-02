import os

def citire_numere(nume_fisier):
    if not os.path.exists(nume_fisier):
        print(f"Eroare: Fișierul '{nume_fisier}' nu există.")
        return None, None
    
    with open(nume_fisier, 'r') as f:
        linii = f.read().splitlines()
    
    if len(linii) < 2:
        print("Eroare: Fișierul trebuie să conțină cel puțin două numere.")
        return None, None
    
    numar1 = linii[0].strip()
    numar2 = linii[1].strip()
    
    if not numar1.isdigit() or not numar2.isdigit():
        print("Eroare: Liniile trebuie să conțină doar cifre valide.")
        return None, None
        
    return list(numar1), list(numar2)

def adunare(n1, n2):
    rezultat = []
    transport = 0
    i = len(n1) - 1
    j = len(n2) - 1
    
    while i >= 0 or j >= 0 or transport > 0:
        cifra1 = int(n1[i]) if i >= 0 else 0
        cifra2 = int(n2[j]) if j >= 0 else 0
        
        suma = cifra1 + cifra2 + transport
        rezultat.append(str(suma % 10))
        transport = suma // 10
        
        i -= 1
        j -= 1
        
    rezultat.reverse()
    rez_str = "".join(rezultat).lstrip('0')
    return rez_str if rez_str else "0"

def inmultire(n1, n2):
    if n1 == ['0'] or n2 == ['0']:
        return "0"
    if n1 == ['1']: return "".join(n2)
    if n2 == ['1']: return "".join(n1)
    
    len1, len2 = len(n1), len(n2)
    rezultat = [0] * (len1 + len2)
    
    for i in range(len1 - 1, -1, -1):
        cifra1 = int(n1[i])
        transport = 0
        for j in range(len2 - 1, -1, -1):
            cifra2 = int(n2[j])
            produs = cifra1 * cifra2 + rezultat[i + j + 1] + transport
            rezultat[i + j + 1] = produs % 10
            transport = produs // 10
        rezultat[i] += transport
        
    rez_str = "".join(map(str, rezultat)).lstrip('0')
    return rez_str if rez_str else "0"

def main():
    n1, n2 = citire_numere("numere.txt")
    if n1 is None or n2 is None:
        return
    
    suma = adunare(n1, n2)
    produs = inmultire(n1, n2)
    
    print(f"Suma este {suma}, iar produsul este {produs}.")

if __name__ == "__main__":
    main()