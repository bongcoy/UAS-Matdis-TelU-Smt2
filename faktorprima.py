# fungsi untuk mencari faktorisasi prima sebuah bilangan
'''credit to https://adityarizki.net/belajar-python-faktorisasi-prima-sebuah-bilangan/'''

print("Ketik 'faktorprima.fprima(x)'")
def faktorisasiprima(x):
    # keluaran variabel factorlist berupa array
    factorlist=[]
    loop=2
    while loop<=x:
        if x%loop==0:
            x/=loop
            # append berfungsi untuk menambahkan sebuah objek ke dalam list/daftar
            factorlist.append(loop)
        else:
            loop+=1
    return factorlist

def fprima(x):
    print(faktorisasiprima(x))
