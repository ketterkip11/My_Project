# number = int(input("Enter the integer number:"))
#
# revs_number = 0
#
# while(number>0):
#     remainder = number%10
#     revs_number = (revs_number*10)+remainder
#     number = number//10
#
# print("The reverse is:{}".format(revs_number))



def rev_number(My_Number):
    reverse_num = 0
    while (My_Number) :
        Reminder = My_Number % 10
        reverse_num = reverse_num* 10 + Reminder
        My_Number //= 10
    return reverse_num

if __name__ == "__main__" :
    My_Number = int(input('Please provide number to be reversed::'))
    print('Reversed number is:', rev_number(My_Number))


