#count even and odd numbers
arr=[2,3,5,6,7,8,1]
even_count=0
odd_count=0
for num in arr:
    if num % 2==0:
        even_count+=1
    else:
        odd_count+=1
print(f"Even count is {even_count} and odd count is {odd_count}")