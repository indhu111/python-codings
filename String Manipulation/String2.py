'''Given a word W, write a program to perform the following.  
1. If the length of the word is greater than or equal to 3 then check the following  
If the nth place is an Alphabet and a vowel display “vowel”  
If the nth place is an Alphabet and not a vowel display “consonant”  
If the nth place is a digit display “digit”  
If any other char display “other”  
2. if the length of the word is less than 3, display “invalid” '''

a=str(input("Enter a string:"))
aa=int(input("Enter a digit:"))
b=len(a)
if (b<3):
    print("Invalid")
else:
    print(f"The character at {aa} is:")
    for i, char in enumerate(a):
        c=i+1
        if c==aa:
            if char.isalpha()==True:
                if char.lower() in ('a','e','i','o','u'):
                    print("vowel")
                else:
                    print("consonant")
            elif char.isdigit()==True:
                print("digit")
            else:
                print("other")
        else:
            print("Index out of range")
            break
