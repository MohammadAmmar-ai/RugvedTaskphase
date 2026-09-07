def smallindexfinder(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                return arr[j]

    return -1
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    value = int(input("Enter element " + str(i + 1) + ": "))
    arr.append(value)
print(smallindexfinder(arr))