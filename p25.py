n = int(input("Enter integer:"))
print(n)
integers =input(f"Enter {n} integers:")
print(integers)
nums=list(map(int,integers.split()))
even_nums=[]
for number in nums:
    if(number % 2 == 0):
      even_nums.append(str(number))
print(" ".join(even_nums))