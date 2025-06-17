
import math 
num = int(input("Enter a number: "))
p = int(math.sqrt(num))

if num<=1:
    print(num, "is not a prime number")
else :
    is_prime = True
    for n in range(2, p+1):
        if num%n == 0 :
            is_prime = False
            break
        
    if is_prime :
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")