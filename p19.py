str = input("Enter string:")
print(str)
vowels="aeiouAEIOU"
count=0
for s in str:
   if s in vowels:
     count=count+1
print(count)   
  