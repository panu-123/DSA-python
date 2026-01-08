#Reverse array without using reverse() Time: O(n) Space: O(1)
arr=[10,11,12,13,14]
left=0
right=len(arr)-1
while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)


#output= [14, 13, 12, 11, 10]