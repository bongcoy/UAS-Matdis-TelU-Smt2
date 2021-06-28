print("Ketik 'kpk.kpk()'")
def kpk():
    print("masukkin bilangan yang mau diitung si kpk nya dipisah pake spasi okee\n")

    arr = [int(i) for i in input().split()]
    arr.sort()
    for i in range(1,arr[0]+1):
        stat = 0
        for j in range(len(arr)):
            if arr[j] % i == 0:
                stat+=1
        if stat == len(arr):
            fpb = i
    for i in range(len(arr)):
        arr[i] = arr[i]//fpb
    for i in range(2,arr[len(arr)-1]):
        stat = 0
        for j in range(len(arr)):
            if arr[j] % i == 0:
                stat +=1
        if stat >=2:
            for j in range(len(arr)):
                if arr[j] % i == 0:
                    arr[j] = arr[j] // i
            fpb = fpb*i
    for i in arr:
        fpb = fpb * i
    print(f"kpk: {fpb}")
