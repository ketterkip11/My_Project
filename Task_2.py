
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
    for x in range(0, arr_len-2):

        for y in range(x+1, arr_len-1):

            for z in range(y+1, arr_len):

                if (arr[x]+arr[y]+arr[z]==0):
                    print(arr[x]+arr[y],arr[z])
                    found = True

    if (found == False):
        print("not exist")

arr = [7,8,9,-2,6,-3,-1, 8,-5]
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
    str = 'What is Python language? Python is a widely used high-level, general-purpose, ' \
          'interpreted, dynamic programming language. Its design philosophy emphasizes code readability, ' \
          'and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. ' \
          'Python supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles.' \
          'It features a dynamic type system and automatic memory management and has a large and comprehensive standard library. ' \
          'The best way we learn anything is by practice and exercise questions. We  have started this section for those (beginner to intermediate) who are familiar with Python'

    # freq(str)



"""a trial of unique numbers"""

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


# A simple Python 3 program
# to find three elements
# whose sum is equal to
# given sum

# Prints all triplets in
# arr[] with given sum
def findTriplets(arr, n, sum):
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (arr[i] + arr[j] +
                        arr[k] == sum):
                    print(arr[i], " ",
                          arr[j], " ",
                          arr[k], sep="")


# Driver code
arr = [7,8,9,-2,6,-3,-1, 8,-5]
n = len(arr)
# findTriplets(arr, n, 0)


def findThreeNumbers(A, arr_size, sum):
    A.sort()

    for i in range(0, arr_size-2):
        l = i + 1
        r = arr_size -1
        while(l<r):
            if (A[i], A[l], A[r] == sum):
                print("Triplet is:", A[i], ',', A[l],',',A[r]);
                return True
            elif (A[i] + A[l] + A[r] < sum):
                l += 1
            else: #A[i] + A[l] + A[r] > sum
                r -= 1

#     return False
# A = [1, 45, 4, 6,10, 8]
# sum = 22
# arr_size = len(A)
# findThreeNumbers(A, arr_size, sum)


# def countdown(n):
#     print(n)
#     if n < 0:
#         return
#     else:
#         countdown(n-1)
# countdown(5)

def countdown(n):
    print(n)
    if n >= 3:
        countdown(n - 1)

# countdown(5)

def countdown(n):
    print(n)
    while n >= 0:
        print(n)
        n -= 1
# countdown(5)

def combinations(l, n, mylist = []):

    if not n:
        print(mylist)
    for i in range(len(l)):
        mylist.append(l[i])
        combinations(l[i+1], n-1, mylist)
        mylist.pop()

# l = ['a','e','i','o','u']
# n = 4
# combinations(l, n)

def count_down(start):

    print(start)

    next = start - 1
    if next > 0:
        count_down(next)

# count_down(3)

def unique(lst):
    if n == 0:
        return [[]]
    l = []
    for i in range (0, len(lst)):
        m = lst[i]
        remLast = lst[i + 1:]

        for p in unique(remLast, n-1):
            l.append([m]+p)
    return l
if __name__=="__main__":

    arr = 'aeiou'
    # print(unique([x for x in arr]))

""""""
def printCombination(arr, n, r):
    data = [0]*r;

    combinationUntil(arr, data,0,n-1,0,r);

def combinationUntil(arr, data, start, end, index, r):
    if (index == r):
        for j in range(r):
            print(data[j], end= "");
        print();
        return ;

    i = start
    while(1 <= end and end - i + 1 >= r - index):
        data[index] = arr[i]
        combinationUntil(arr, data, i + 1, end, index + 1, r)

        i += 1

arr = [1,2,3,4,5]
r = 3
n = len(arr)
printCombination(arr, n, r)
""""""
def printCombinations(arr, n, r):
    data = [0]*r

    combinationUntill(arr, n,r, 0, data, 0)

def combinationUntill(arr, n, r, index, data, i):
    if (index == r):
        for j in range(r):
            print(data[j], end= "")
        print()
        return
    if (i >= n):
        return


    # i = start
    # while(1 <= end and end - i + 1 >= r - index):
    data[index] = arr[i]
    combinationUntill(arr, n, r, index + 1, data, i + 1)
    combinationUntill(arr, n, r, index, data, i + 1)
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    r = 3
    n = len(arr)
    printCombinations(arr, n, r)


