print("Ketik 'fpb.fpb()'")
def fpb():
    print("masukkin bilangan yang mau diitung si fpb nya dipisah dengan spasi\n")
    arr = [int(i) for i in input().split()]
    arr.sort()
    for i in range(1,arr[0]+1):
        stat = 0
        for j in range(len(arr)):
            if arr[j] % i == 0:
                stat+=1
        if stat == len(arr):
            fpb = i
    print(f"FPB atau GCD nya adalah: {fpb}")
