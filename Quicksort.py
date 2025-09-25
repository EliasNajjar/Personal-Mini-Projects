def quicksort(arr, l, r):
    if l >= r:
        return
    i = l
    x = arr[r]
    for j in range(l, r):
        if arr[j] < x:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i += 1
    arr[r] = arr[i]
    arr[i] = x
    quicksort(arr, l, i - 1)
    quicksort(arr, i + 1, r)

nums = [15,5,2,6,4,12,10,14,1,3,8,7,11,9,13,0]
quicksort(nums,0,len(nums)-1)
print(nums)