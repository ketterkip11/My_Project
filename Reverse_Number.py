
"""a function to reverse a number"""

def rev_number(My_Number):
    reverse_num = 0
    while (My_Number) :
        Reminder = My_Number % 10
        reverse_num = reverse_num* 10 + Reminder
        My_Number //= 10
    return reverse_num

if __name__ == "__main__" :
    My_Number = int(input('Please provide number to be reversed: '))
    print('Reversed number is:', rev_number(My_Number))


