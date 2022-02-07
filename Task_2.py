
"""A Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
"""
def unique(numbers):
  if len(numbers) == len(set(numbers)):
    return True
  else:
    return False;
# print(unique([1,5,7,9,11,11]))
# print(unique([2,4,5,7,9]))



"""A Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
"""

from itertools import permutations
chars = list(['a', 'e', 'i', 'o', 'u'])
allStrings = permutations(chars)
# for string in allStrings:
    # print(("unique posibilities:"),''.join(string))

"""A Python program to remove and print every third number from a list of numbers until the list becomes empty.
"""

def removeThirdNumber(int_list):
    pos = 3 - 1
    index = 0
    len_list = (len(int_list))

    while len_list>0:
        index = (pos+index)%len_list
        print(int_list.pop(index))
        len_list -= 1

nums = [10,20,30,40,50,60,70,80,90]
# print(removeThirdNumber(nums))


"""4. Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers.
"""
def triplet(arr, arr_len):

    found = True
    for i in range(0, arr_len-2):

        for j in range(i+1, arr_len-1):

            for k in range(j+1, arr_len):

                if (arr[i]+arr[j]+arr[k]==0):
                    print(arr[i]+arr[j],arr[k])
                    found = True

    if (found == False):
        print("not exist")

arr = [7,8,9,-5,6,-4,-2]
arr_len = len(arr)
# print(triplet(arr,arr_len))


"""returns 3 digits"""
def TripleSum(arr, k):
    arr_size = len(arr)
    found = False
    arr.sort()

    for a in range(0, arr_size - 2):
        b = a + 1
        c = arr_size - 1
        while (b<c):
            if (arr[1] + arr[b] + arr[c] == k):
                print((arr[a], arr[b], arr[c]))
                b+=1
                c-=1
                found = True
            elif (arr[1] + arr[b] + arr[c] < k):
                b +=1
            else:
                c -= 1

    if (found == False):
        print("No matching Triplets found")
arr = [0, 1, 2, 3, 5, 7, 13, 17, 19, 19]
k = 20
# print(TripleSum(arr, k))
""""""
"""Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies"""


def freq(str):
    str_list = str.split()

    unique_words = set(str_list)

    for words in unique_words:
        print('Frequency of', words, 'is:', str_list.count(words))

if __name__=="__main__":
    str = 'apple mango apple orange orange apple guava mango mango'

    freq(str)



"""a trial of unique numbers"""
#
# numbers = []
# maxLengthList = 6
# while len(numbers) <= maxLengthList:
#     item = input("Enter your sequence if numbers:")
#     numbers.append(item)
#     # print(numbers)
#     # print(numbers)
#     if len(numbers) == len(set(numbers)):
#         print("No duplicate numbers")
#     else:
#         print("Duplicate numbers are present")
