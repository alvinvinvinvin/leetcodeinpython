def majority_element(arr):
    ma = arr[0]
    count = 0
    for i in arr:
        if count == 0:
            ma = i
            count = 1
        elif ma == i:
            count += 1
        else:
            count -= 1
    return ma

arr = [1,1,1,3,1,1,2,2,2,1]
print(len(arr))
print(majority_element(arr))
