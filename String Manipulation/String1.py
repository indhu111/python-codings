'''Given a string s, write a program to remove the characters from the string 
which has the same index value that is the multiple of a given number.
Constraints:   
S is not null and contains minimum 2 characters.  
Input Format:   
First line of the input contains s,j
Output Format:   
Generated string  '''

def sequence(s,j):
    list1=[]
    list1.append(s[0])
    for i,char in enumerate(s):
        if i%j==0:
            pass
        else:
            list1.append(char)
    return list1
        

ab=str(input("Enter a string value:"))
c=int(input("Enter the value of  places to be removed:"))
print(sequence(ab,c))
