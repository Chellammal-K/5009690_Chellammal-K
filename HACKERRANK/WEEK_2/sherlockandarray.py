def balancedSums(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for num in arr:
        if left_sum == total_sum - left_sum - num:
            return "YES"
        left_sum += num
        
    return "NO"



T = int(input())  
for _ in range(T):
    n = int(input())  
    arr = list(map(int, input().split()))
    print(balancedSums(arr))
