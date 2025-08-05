def plusMinus(arr):
    n = len(arr)
    pos = neg = zero = 0

    for num in arr:
        if num > 0:
            pos +=1
        elif num < 0:
            neg +=1
        else:
            zero +=1

    print("{:.6f}".format(pos / n))
    print("{:.6f}".format(neg / n))
    print("{:.6f}".format(zero / n))
n = int(input())
arr = list(map(int, input().split()))
plusMinus(arr)
