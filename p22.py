n = int(input("Enter integer:"))
print(n)
integers =input(f"Enter {n} integers:")
print(integers)
nums=list(map(int,integers.split()))
count=0
for numbers in nums:
    count+=numbers 
print(count)



