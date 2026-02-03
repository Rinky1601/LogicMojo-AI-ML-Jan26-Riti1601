str = (input("Enter string:").lower())
print(str)
rev_str=(str[-1::-1])
if(str == rev_str):
    print("Palindrome")
else:
    print("Not Palindrome")