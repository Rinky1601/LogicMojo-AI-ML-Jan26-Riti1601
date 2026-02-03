org_num = int(input("Enter number:"))
print(org_num)
for i in range (2,org_num-1):
    if(org_num % i == 0):
        print("Not a prime number")
        break
else:
        print("Prime number")







        
    
  