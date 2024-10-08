'''Given a numbers X, write a program to perform the following.  
1. If the number is a single digit number, then display the square 
of the number.   
2. If the number is having more than 1 digit, then perform the following.  
If the 2nd digit is divisible by both 2 and 4 display “24”  
Else if the number is even number display “2”  
Else if the number is odd number display “1” '''

a=int(input("Enter a number:"))
if (a//10)<1:
    print(a**2)
else:
    b=str(a)
    c=b[1]
    d=int(c)
    if d%2==0:
        if d%4==0:
            print("24")
        else:
            print("2")
    else:
        print("1")