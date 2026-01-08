#Find max element in array
arr=[1,2,4,6,7,8,0]
max_val=arr[0]
for num in arr:
    if num>max_val:
        max_val=num
print(max_val)
    