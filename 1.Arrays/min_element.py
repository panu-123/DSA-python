#Find minimum element in array
arr=[1,2,4,6,7,8,0]
min_val=arr[0]
for num in arr:
    if num<min_val:
        min_val=num
print(min_val)
    
