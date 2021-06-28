print("Ketik 'ekui.input_ekui()'")
def ekui(a,b,m,max):
    for x in range(max+1):
        if ((a*x)-b) % m == 0:
            print("x =",x)
def input_ekui():
    print("Masukkan dengan format :\nax = b (mod m)\n\n*note = jangan lupa operasiin si b nya dulu kalo misal ada konstanta lain\n")
    a,b,m,max = map(int,input("Urutan 'a b m max'\ninput : ").split())
    ekui(a,b,m,max)
