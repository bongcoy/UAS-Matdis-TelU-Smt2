'''
Kekurangan program :
menunggu repiw dari testing

created by Muhammad Pascal Dewantara, Informatika'20 Telkom University
edited by Bagus Hariyadi 
p.s tinggal di testing ae bismillah kaga ada yang salah
'''
print("Ketik 'konversi_bilangan.tanya_input()'")
def konversi_kali(x,basis_x):
    '''
    konversi x to desi
    '''
    if basis_x <= 10:
        lis = [int(i) for i in str(x)]
        total = 0
        jmlh_digit = len(lis) - 1

        for i in lis:
            hasil = i * basis_x**jmlh_digit
            
            if jmlh_digit == len(lis) - 1:
                print(f"({i} x {basis_x}^{jmlh_digit})",end="")
            else:
                print(f" + ({i} x {basis_x}^{jmlh_digit})",end="")
            
            total += hasil
            jmlh_digit -= 1

    elif basis_x >10:
        lis_hexa = [ord(i) for i in x]
        for i in range(len(lis_hexa)):
            if lis_hexa[i]>=48 and lis_hexa[i]<=57:
                lis_hexa[i] = lis_hexa[i] - 48
            elif lis_hexa[i]>=65 and lis_hexa[i]<=90:
                lis_hexa[i] = lis_hexa[i] - 55
        
        total = 0
        jmlh_digit = len(lis_hexa) - 1

        for i in lis_hexa:
            hasil = i * basis_x**jmlh_digit
            
            if jmlh_digit == len(lis_hexa) - 1:
                print(f"({i} x {basis_x}^{jmlh_digit})",end="")
            else:
                print(f" + ({i} x {basis_x}^{jmlh_digit})",end="")
            
            total += hasil
            jmlh_digit -= 1

    print(f" = {total}")

def konversi_sisa(desimal,basis_y):
    '''
    konversi desi to y
    '''
    lis = []

    def aksi(desimal,basis_y):
        hasil = desimal // basis_y
        sisa = desimal % basis_y
        print(f"{desimal} : {basis_y} = {hasil} sisa {sisa}")

        lis.append(sisa)

        if hasil != 0:
            aksi(hasil,basis_y)
    aksi(desimal,basis_y)
    for i in range(len(lis)):
        if lis[i] >9:
            lis[i] = chr(lis[i]+55)
    print()

    for i in lis[::-1]:
        print(i,end="")
    print()
    
def tanya_input():
    mau = input('Mau kali atau sisa ? \n\nkalo dari x ke desimal, maka ketik "kali"\nkalo dari desimal ke y, maka ketik "sisa"\n\nMaunya ')
    if mau == "sisa":
        desi = int(input("Desimal = "))
        bas_y = int(input("Basis tujuan (tuliskan dlm bntk angka, tanpa spasi) = "))
        konversi_sisa(desi,bas_y)
    elif mau == "kali":
        basis_bil = int(input("Basis asal (tuliskan dlm bntk angka) = "))
        if basis_bil < 10:
            bil = int(input("Bilangan (tuliskan dlm bntk angka) = "))
            konversi_kali(bil,basis_bil)
        elif basis_bil > 10: #Parameter bilangan jadi ga wajib, karena kita input 1 per 1 untuk hexa
            bil = input("masukkin aja apa yang mau dikonversinya: ")
            bil = bil.upper()
            konversi_kali(bil,basis_bil)    
