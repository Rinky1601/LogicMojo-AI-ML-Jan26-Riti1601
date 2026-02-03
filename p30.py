n = int(input("Enter integer:"))
print(n)
integers =input(f"Enter {n} integers:")
nums=list(map(int,integers.split()))
print(" ".join(map(str,nums)))
rev_nums=nums[-1::-1]
if nums == rev_nums:
    print("Palindrome")
else:
    print("Not Palindrome")
  
