def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result

array=[1,2,3]
result = grow(array)
print (result)
