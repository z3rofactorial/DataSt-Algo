arr=[1,22,3,44,5,6,11,2,11]
for index in range(len(arr)):
    min_index=index
    for j in range(index+1,len(arr)):
        if arr[min_index]>arr[j]:
            min_index=j
    arr[index],arr[min_index]=arr[min_index],arr[index]

print(arr)