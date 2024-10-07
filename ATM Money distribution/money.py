'''Given an ATM money containing K units of money. N people want to withdraw money from the 
machine one by one in order, write a python program to check if each person can withdraw required 
amount of money or not.
Input Format:  
Input contains comma separated integers where first input is the amount of money in machine rest are 
the amount of money required by each person.  
Output Format:  
Print a single line containing a string with length N. For each valid i, the i-th character of this string 
should be '1' if the i-th person will successfully withdraw their money or '0' otherwise.  '''

def withdrawals(li):
    samp_list=[]
    a=li[0]
    for i in li[1:]:  
        if a >= i:  
            a = a - i  
            samp_list.append(1)  
        else:
            samp_list.append(0)  
            break
    return samp_list

list1=[]
atm_money=int(input("Enter the money in atm:"))
list1.append(atm_money)
withdraw=int(input("Enter the amount of withdrawals:"))
for i in range(withdraw):
    b=int(input("Enter the money for withdrawal:"))
    list1.append(b)
print("1-withdraw successful 0-withdraw failure")
print(withdrawals(list1))