def Sum(arr):
    total = sum(arr)
    minimum = min(arr)
    maximum = max(arr)

    min_sum = total - maximum
    max_sum = total - minimum

    print(min_sum, max_sum)

arr = list(map(int, input().split()))
Sum(arr)