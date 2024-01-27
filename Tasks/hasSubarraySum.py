def hasSubarraySum(arr, k):
    prefix_sum = 0
    seen = {0} 

    for num in arr:
        prefix_sum += num
        if prefix_sum - k in seen:
            return True
        seen.add(prefix_sum)

    return False

arr = [11, 12, 34, 4, 2, 8, 9, 5]
k = 6
result = hasSubarraySum(arr, k)
print(result)  
