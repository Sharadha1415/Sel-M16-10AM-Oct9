'''PROGRAMMING QUESTIONS'''

'''1. Write a program to find the length of the iterable without using inbuilt function (len)'''
## Using inbuilt functions
str_1 = 'python is a programming language'
print(len(str_1))

list_ = ['amith', 'adithya', 'bharath', 'sanjay', 'krushitha']
print(len(list_))

dict_ = {'name':'bharath', 'age':28, 'gender':'male', 'place':'bengaluru'}
print(len(dict_))

# Using while loop
str_1 = 'python is a programming language'
index = 0
total = 0
while index < len(str_1):
    index += 1
    total += 1

print(total)


## Using for loop
str_1 = 'python is a programming language'
total = 0
for ele in str_1:
    total += 1

print(total)

# ## Using functions
# str_1 = 'python is a programming language'
# def find_length(n):
#     total = 0
#     for ele in n:
#         total += 1
#
#     return total
#
# print(find_length(str_1))
#----------------------------------------------------------------------------
'''2. Write a program to reverse a iterable without using any inbuilt functions'''
# Slicing
str_1 = 'python is a programming language'
print(str_1[::-1])

# Using for loop
str_1 = 'python is a programming language'
rev_str = ''
for ele in str_1:
    rev_str = ele + rev_str

print(rev_str)

# str_1 = 'python is a programming language'
# rev_str = ''
# for ele in str_1[::-1]:
#     rev_str += ele
#
# print(rev_str)

## reversing list
# list_ = ['flipkart', 'amazon', 'pencil', 'paper', 'books', 'oceans']
# rev_list = []
# for ele in list_:
#     rev_list = [ele] + rev_list
#
# print(rev_list)

## reversing tuple
# tuple_ = ('flipkart', 'amazon', 'pencil', 'paper', 'books', 'oceans')
# rev_tuple = ()
# for ele in tuple_:
#     rev_tuple = (ele,) + rev_tuple
#
# print(rev_tuple)

#----------------------------------------------------
'''3. Write a program to replace one string with another. 
e.g. "Hello World" replaces "World" with "Universe".**   '''

# Using str method
str_ = 'Hello World'
print(str_.replace("World", "Universe"))

# ## Using loops
# str_ = 'Hello World'
# words = str_.split()
# str_1 = ""
# # print(words)        #['Hello', 'World']
# for word in words:
#     if word == 'World':
#         str_1 += 'Universe'
#     else:
#         str_1 += word + ' '
#
# print(str_1)
#
## Using re
str_ = 'Hello World'
import re
print(re.sub('World', 'Universe', str_))

#------------------------------------------------------------------------
'''4. How to convert a string to a list and vice-versa'''
# str_ = 'version control'
# print(str_.split())     #['version', 'control']
# print(list(str_))  ## ['v', 'e', 'r', 's', 'i', 'o', 'n', ' ', 'c', 'o', 'n', 't', 'r', 'o', 'l']

# list_ = ['apple', 'google', 'ajio', 'myntra']
# print(str(list_))       #'['apple', 'google', 'ajio', 'myntra']'
# print(' '.join(list_))      #apple google ajio myntra

#------------------------------------------------------------------
'''5. Convert the string "Hello welcome to Python" to a comma separated string.'''
# str_ = "Hello welcome to Python"        #'Hello,welcome,to,Python'
# print(str_.replace(' ', ','))

## Alternate solution1
# str_ = "Hello welcome to Python"
# res = str_.split()  #['hello', 'welcome', 'to', 'python']
# print(','.join(res))        #'Hello,welcome,to,Python'

## Alternate solution
# str_ = "Hello welcome to Python"
# res = ''
# for ele in str_:
#     if ele==' ':
#         res += ','
#     else:
#         res += ele
#
# print(res)
#-------------------------------------------------------------------
'''6. Write a program to print alternate characters in a string.'''
# Slicing
str_ = "Hello welcome to Python"
print(str_[::2])        #Hlowloet yhn

## Loop
str_ = "Hello welcome to Python"
res = ''
for ele in range(0, len(str_), 2):
    res += str_[ele]            #res = res + str_[ele]

print(res)      #'Hlowloet yhn'

#-----------------------------------------------------------------
'''7. Write a Program to print ascii values of the characters present in a string.'''
str_ = 'Dharwad'
for ele in str_:
    print(f'The ASCII VALUE os {ele} is {ord(ele)}')
#
# ### ord() takes str as an argument. str should be of length 1
#
# # chr : chr() takes integer as an argument
# print(chr(120))     #x
# print(chr(114))     #r

#-----------------------------------------------------------------------
'''8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.'''
## Using inbuilt methods
str_ = 'HelLO WeLCOmE tO BeNGAluRu'
print(str_.swapcase())      #hELlo wElcoMe To bEngaLUrU

# ## Alternate solution
# str_ = 'HelLO WeLCOmE tO BeNGAluRu'
# swap = ''
# for ele in str_:
#     if ele.isalpha():
#         if ele.isupper():
#             swap += ele.lower()
#         else:
#             swap += ele.upper()
#     else:
#         swap += ele
# print(swap)     #hELlo wElcoMe To bEngaLUrU


# ## Alternate solution
# str_ = 'HelLO WeLCOmE tO BeNGAluRu'
# swap = ''
# for ele in str_:
#     if 'a'<= ele <='z' or 'A'<=ele<='Z':
#         if 'A'<=ele<='Z':
#             swap += chr(ord(ele)+32)
#         else:
#             swap += chr(ord(ele)-32)
#     else:
#         swap += ele
#
# print(swap)
# #---------------------------------------------------------------------
'''9. Write a program to swap two numbers without using the 3rd variable.'''
# ## using the 3rd variable
# num1 = 100
# num2 = 200
#
# temp = num1     #temp=100
# num1 = num2    #num1=200
# num2 = temp
# print(num1)
# print(num2)

## without using 3rd variable
num1 = 100
num2 = 200
num2, num1 = num1, num2
print(num1)
print(num2)

#-----------------------------------------------------------
'''10. Write a program to merge two different lists'''
# ## Concatenation
# l1 = [10, 20, 30]
# l2 = [100, 200, 300]        #[10, 20, 30, 100, 200, 300]
# print(l1 + l2)      #[10, 20, 30, 100, 200, 300]
#
# ## Using extend
# l1 = [10, 20, 30]
# l2 = [100, 200, 300]
# l1.extend(l2)
# print(l1)
#
# ## ALternate
# l1 = [10, 20, 30]
# l2 = [100, 200, 300]
# print([*l1, *l2])       #[10, 20, 30, 100, 200, 300]

# ## Alternate
# from itertools import chain
# l1 = [10, 20, 30]
# l2 = [100, 200, 300]
# res = chain(l1, l2)
# print(res)      #object
# print(list(res))        #[10, 20, 30, 100, 200, 300]

# ## To merge dictionaries
# d1 = {'one':1, 'two':2, 'three':3}
# d2 = {1:'one', 2:'two', 3:'three'}
# print({**d1, **d2})     #{'one': 1, 'two': 2, 'three': 3, 1: 'one', 2: 'two', 3: 'three'}
#
# ## Alternate
# print(d1 | d2)      #{'one': 1, 'two': 2, 'three': 3, 1: 'one', 2: 'two', 3: 'three'}
#
# from itertools import chain
# merged_dict = chain(d1.items(), d2.items())
# print(list(merged_dict))    #[('one', 1), ('two', 2), ('three', 3), (1, 'one'), (2, 'two'), (3, 'three')]
#-----------------------------------------------------------------------

'''11. Wap to read a random line in the file'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample2.txt'
# def random_line(num):
#     with open(path) as file_:
#         for line_no, line in enumerate(file_, start=1):
#             if line_no == num:
#                 print(line)
#
# random_line(12)

## Alternate solution
# from itertools import islice
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample2.txt'
# def random_line(line_num):
#     with open(path) as file_:
#         res = islice(file_, line_num-1, line_num)
#         print(res)          #itertools.islice object
#         for ele in res:
#             print(ele)
#
# random_line(11)

'''12. To read multiple lines'''
# from itertools import islice
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample2.txt'
# def random_line(start, end):
#     with open(path) as file_:
#         res = islice(file_, start-1, end)
#         print(res)          #itertools.islice object
#         for ele in res:
#             print(ele)
#
# random_line(2, 7)

#-------------------------------------------------------------
'''13. wap to print last n lines of a file'''
# from itertools import islice
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample2.txt'
# def random_line(num):
#     with open(path) as file_:
#         line_count = 0
#         for line in file_:
#             line_count += 1
#         print(line_count)
#
#         file_.seek(0)       #takes the cursor to 0th position
#
#         res = islice(file_, line_count-num, line_count)
#         # print(res)      # islice object
#         for line in res:
#             print(line)
# random_line(4)

# ## Alternate solution
# from collections import deque
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample2.txt'
# def random_line(num):
#     with open(path) as file_:
#         res = deque(file_, num)
#         print(res)
#
# random_line(4)

#--------------------------------
# # from collections import deque
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample2.txt'
# with open(path) as file_:
#     res = deque(file_, 5)   ## Reads last 5 lines from the file
#     print(res)

#-----------------------------------------------------
'''
tell() : Gives the position of the cursor
        Syntax : file_name.tell()
        tell() doesnot take any parameter
        
seek() : Takes cursor to the specified position
        Syntax : file_name.seek(position)
        seek() takes only one mandatory parameter.'''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample2.txt'
# with open(path) as file_:
#     print(file_.readline())
#     print(file_.readline())
#     print(file_.readline())
#
#     print(file_.tell())     #71
#     file_.seek(35)
#
#     print(file_.readline())

#--------------------------------------------------------
'''14. write a func to check if the string is palindrome or not'''
str_1 = 'madam'
str_2 = 'sir'

def palindrome(string):
    if string == string[::-1]:
        print(f'{string} is a palindrome')
    else:
        print(f'{string} is not a palindrome')

palindrome(str_1)
palindrome(str_2)

## Alternate solution
# str_1 = 'madam'
# def palindrome(string):
#     rev = ''
#     for ele in string:
#         rev = ele + rev
#     if string == rev:
#         print('palindrome')
#     else:
#         print('not a palindrome')
# palindrome(str_1)

#------------------------------------------------------------
'''15. wap to search for a particular character in a given string and return the 
corresponding index'''
# str_1 = 'tomorrow is holiday'
# def search_str(n):
#     for index, item in enumerate(str_1):
#         if item == n:
#             print(index)
# search_str('o')
#
#
# ## Alternate
# str_1 = 'tomorrow is holiday'
# def str_index(n):
#     for ele in str_1:
#         if str_1.find(n) > -1:
#             return str_1.find(n)
# print(str_index('s'))

#--------------------------------------------------------------
'''03 July 2023'''
'''16. wap to get the below output
str_ =  'python is a programming language and programs are fun'
op --> {'p': ['python', 'programming', 'programs'], 'i':['is'], 'a':['a', 'and', are'], 'l':['language'], 'f':['fun']}
'''
# str_ =  'python is a programming language and programs are fun'
# str_split = str_.split()
# print(str_split)    #['python', 'is', 'a', 'programming', 'language', 'and', 'programs', 'are', 'fun']
#
# dict_ = {}
# for ele in str_split:
#     if ele[0] not in dict_:
#         dict_[ele[0]] = [ele]
#     else:
#         dict_[ele[0]] += [ele]
#
# print(dict_)


# ## ALternate solution
# from collections import defaultdict
# str_ =  'python is a programming language and programs are fun'
# def_dict = defaultdict(list)
#
# for ele in str_.split():
#     def_dict[ele[0]] += [ele]
#
# print(def_dict)     #defaultdict(<class 'list'>, {'p': ['python', 'programming', 'programs'], 'i': ['is'], 'a': ['a', 'and', 'are'], 'l': ['language'], 'f': ['fun']})
#----------------------------------------------------
## Similarly, ending elements
# {'n': ['python', 'fun'], 's': ['is', 'programs'], 'a': ['a'], 'g': ['programming'], 'e': ['language', 'are'], 'd': ['and']}
# str_ =  'python is a programming language and programs are fun'
# d = {}
# res = str_.split()
# for ele in res:
#     if ele[-1] not in d:
#         d[ele[-1]] = [ele]
#     else:
#         d[ele[-1]] += [ele]
# print(d)

# ## Using default dict
# from collections import defaultdict
# str_ =  'python is a programming language and programs are fun'
# def_dict = defaultdict(list)
# res = str_.split()
# for ele in res:
#     def_dict[ele[-1]] += [ele]
#
# print(def_dict)

#------------------------------------------------------------------------------------------
'''wap to create a dict of element and its count pair'''
str_ = 'she sells seashells on the seashore'    #{s:8, h:4, e:7, ..}
d = {}
for ele in str_:
    if ele not in d:
        d[ele] = 1
    else:
        d[ele] += 1
print(d)

# # Using default dict
# str_ = 'she sells seashells on the seashore'    #{s:8, h:4, e:7, ..}
# from collections import defaultdict
# def_dict = defaultdict(int)
# for ele in str_:
#     def_dict[ele] += 1
#
# print(def_dict)

## Using count
# str_ = 'she sells seashells on the seashore'
# d = {}
# for ele in str_:
#     d[ele] = str_.count(ele)
# print(d)        #{'s': 8, 'h': 4, 'e': 7, ' ': 5, 'l': 4, 'a': 2, 'o': 2, 'n': 1, 't': 1, 'r': 1}

#_------------------------------------------------------------------------------
'''17. wap to replace all the characters with * if the character occurs more than once in a string'''
# str_ = 'hello welcome to Bengaluru'     ## h*****w**c*m**t**B*nga**r*
# res = ''
# for ele in str_:
#     if str_.count(ele) > 1:
#         res += '*'
#     else:
#         res += ele
# print(res)      # h*****w**c*m**t**B*nga**r*
#
# ## Using comprehension
# str_ = 'hello welcome to Bengaluru'
# res_ = ['*' if str_.count(ele)>1 else ele for ele in str_]
# # print(res_)
# print(''.join(res_))    #h*****w**c*m**t**B*nga**r*

#------------------------------------------------------------------
'''18. write a deco which will convert neg numbers into positive'''
# def outer(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)       #subtraction(9, 11)
#         print(abs(res))
#     return wrapper
#
# @outer      #subtraction = outer(subtraction)
# def subtraction(a, b):
#     return a - b
#
# subtraction(9, 11)
#
# ## func --> subtraction
# ## subtraction --> wrapper address
# ## (*args, **kwargs) --> (9, 11)

#-------------------------------------------------------------
'''19. wap to get the count of number of instances of a class that is being created'''
# class Sample:
#     count = 0
#
#     def __init__(self):
#         Sample.count += 1
#
# s1 = Sample()
# s2 = Sample()
# s3 = Sample()
#
# print(f'The number of instances created are {Sample.count}')

#--------------------------------------------------------------
'''20. write a func which takes a list of strings and numbers. If the item is string, print it as it is,
if it is int or float reverse it and print it'''
# list_ = ['apple', 10, 9.8, 'google', 123, 'hello', 987, 8.4]
# res = []
# for ele in list_:
#     if isinstance(ele, str):
#         res.append(ele)
#     else:
#         res.append(str(ele)[::-1])
# print(res)

#--------------------------------------------------------
# l = ['apple', 'myntra']     #{apple:elppa, myntra:myntra}
# d = {}
# for ele in l:
#     if len(ele)%2==0:
#         d[ele] = ele
#     else:
#         d[ele] = ele[::-1]
#
# print(d)

#--------------------------------------------------------------
'''04 July'''
'''21. write a class names Sample and it should have iteration capability'''
# class Sample:
#
#     def __init__(self, iterable):
#         self.iterable = iterable
#
#     def __iter__(self):
#         return iter(self.iterable)
#
# s = Sample(['hai', 'bye', 'hello', 'welcome', 20, 21])
# for ele in s:
#     print(ele)

#------------------------
# a = 'hello world'
# print(dir(a))       #__iter__, __len__
#
# ## Converting iterable to the iterator
# b = iter(a)
# print(dir(b))       #__iter__, __next__

#---------------------------------------------------------------
'''22. write a custom class which can access the values of dictionary using d['a'] 
and d.a   '''
# class Sample:
#     def __init__(self, dict_):
#         self.dict_ = dict_
#
#     def __getitem__(self, item):
#         return self.dict_[item]
#
#     def __getattr__(self, item):
#         return self.dict_[item]
# s = Sample({'a':10, 'b':20})
# print(s['a'])
# print(s.a)

#---------------------------------------------------------------
'''23. wap to get the below output'''
s = 'hi how are you'        ## uoy era woh ih
rev_str = ''
for ele in s:
    rev_str = ele + rev_str
print(rev_str)
#
#
# s = 'hi how are you'        ## 'ih woh era uoy'
# res = s.split()
# rev = ''
# for ele in res:
#     rev += ele[::-1] +' '
# print(rev)

# ## Alternate solution
# s = 'hi how are you'        ## 'ih woh era uoy'
# res = s.split()     #['hi', 'how', 'are', 'you']
# rev_str = ''
# for ele in res:
#     rev = ''
#     for item in ele:
#         rev = item + rev
#     rev_str += rev +' '
#
# print(rev_str)
#------------------------------------------------------------
'''24. wap to reverse the elements in the  list'''
# l = ['apple', 'google', 'ajio', 'myntra']   #['elppa', 'elgoog', 'oija', 'artnym']
# new = []
# for ele in l:
#     rev = ''
#     for item in ele:
#         rev = item + rev
#     new.append(rev)
#
# print(new)

#------------------------------------------------------
'''25. write a lambda func to add two numbers'''
# res = lambda a, b : a + b
# print(res(1, 2))
#------------------------------------------------------
'''26. what is the output of the following 
l1 = [1, 2, 3]              l2 = [4, 5, 6]
l1 + l2'''
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(l1 + l2)      #[1, 2, 3, 4, 5, 6]
# print([l1 + l2])
# print(l1, l2)       #[1, 2, 3] [4, 5, 6]
# print([l1, l2])     #[[1, 2, 3], [4, 5, 6]]
# print([*l1, *l2])       #[1, 2, 3, 4, 5, 6]
#------------------------------------------------------
'''27. wap to remove the duplicates from the list without using inbuilt methods'''
# items = [1, 2, 3, 1, 4, 2, 5, 4, 5, 6, 7, 6, 8 ,7, 9, 10]
# ## Solution 1
# unique_list = set(items)
# print(list(unique_list))        #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# ## Alternate
# items = [1, 2, 3, 1, 4, 2, 5, 4, 5, 6, 7, 6, 8 ,7, 9, 10]
# unique_list = []
# for ele in items:
#     if ele not in unique_list:
#         unique_list.append(ele)
# print(unique_list)  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#-----------------------------------------------------
'''28. wap to find the longest word in the sentence '''
# sentence = 'python is a programming language'
# res = sentence.split()
# longest_word = ''
# for item in res:
#     if len(longest_word) < len(item):
#         longest_word = item
#
# print(longest_word)
#
# ## Alternate solution
# sentence = 'python is a programming language'
# res = sentence.split()
# print(res)      #['python', 'is', 'a', 'programming', 'language']
# print(max(res, key=len))    #programming

#------------------------------------------
# ## Program to find shortest word
# sentence = 'python is a programming language'
# res = sentence.split()
# print(min(res, key=len))        #a
#
# ## Alternate solution
# sentence = 'python is a programming language'
# res = sentence.split()
# shortest_word = res[0]
# for word in res:
#     if len(shortest_word) > len(word):
#         shortest_word = word
#
# print(shortest_word)

#------------------------------------------
# l = [1, 2, 3 ,4, 5, 6]
# print(max(l))
# print(min(l))

##
# l = ['apple', 'google', 'ajio', 'myntra', 'microsoft']
# print(max(l))       #myntra.. It'll consider based on ASCII number
# print(max(l, key=len))      #microsoft. Since key=len, the longest word will be considered
#
# print(min(l))
# print(min(l, key=len))      #ajio

#-------------------------------------------------------------
'''29. wap to reverse the value of a dict if the value is of type string'''
# d = {'a':'hello', 'b':9.2, 'c':True, 'd':'hai', 'e':'199'}      ## {a:olleh, b:9.2, c:True, d:iah, e:991}
# d1 = {}
# for key, value in d.items():
#     if isinstance(value, str):
#         d1[key] = value[::-1]
#     else:
#         d1[key] = value
#
# print(d1)       #{'a': 'olleh', 'b': 9.2, 'c': True, 'd': 'iah', 'e': '991'}
#
# ## Using comprehensions
# d2 = {key:value[::-1] if isinstance(value, str) else value for key, value in d.items()}
# print(d2)       #{'a': 'olleh', 'b': 9.2, 'c': True, 'd': 'iah', 'e': '991'}

#-------------------------------------------------------------
'''30. wap to get '1234' from tuple t = (1, 2, 3, 4)'''
# t = ('1', '2', '3', '4')        #'1234'
# print(''.join(t))       #'1234'
#
# ## Alternate solution
# t = ('1', '2', '3', '4')
# res = ''
# for ele in t:
#     res += ele
# print(res)

#----------------------------------------------------------
'''31. How to get the elements that are in list b, but not in list a'''
# a = [1, 2, 3, 4, 5, 6, 7]
# b = [1, 3, 5, 7, 9, 11, 13, 15]
#
# set_a = set(a)
# set_b = set(b)
# res = set_b.difference(set_a)
# print(list(res))
#
# # Alternate solution
# a = [1, 2, 3, 4, 5, 6, 7]
# b = [1, 3, 5, 7, 9, 11, 13, 15]
# unique_list = []
# for ele in b:
#     if ele not in a:
#         unique_list.append(ele)
# print(unique_list)      #[9, 11, 13, 15]

#-----------------------------------------------------------
'''32. A func takes variable number of positional args as input. How to check if the args 
passed are more than 5'''
# def func(*args):
#
#     if len(args) > 5:
#         print('Args are more than 5')
#     else:
#         print('Args are less than 5')
#
# func(10, 'hai', 11, 12, 19, 'hello', True, False, 'abc')
# func(1, 1)


# ## Alternate solution
# def func(*args):
#     total = 0
#     for ele in args:
#         total += 1
#
#     if total > 5:
#         print('Args are more than 5')
#     else:
#         print('Args are less than 5')
#
# func(1, 2, 3, 4, 5 ,6, 7, 8)

#--------------------------------------------------------------
'''33. Count the number of occurances of 'CRITICAL', 'INFO', 'ERROR' lines in sample2.txt file '''
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample2.txt'
# with open(path) as file:
#     d = {}
#     for line in file:
#         res = line.split(':')
#         if res[0] not in d:
#             d[res[0]] = 1
#         else:
#             d[res[0]] += 1
#
#     print(d)

#------------------------------------------
'''34. wap to reverse the iterable without using reversed func'''
# l = [1, 2, 3, 4, 5]
# rev = []
# for ele in l:
#     rev = [ele] + rev
# print(rev)
#
# ## Alternate method
# l = [1, 2, 3, 4, 5]
# rev = []
# for ele in l[::-1]:
#     rev  += [ele]
#
# print(rev)

#-----------------------------------------------------------------------------------
'''35. Print the numbers in the below list'''
# l = ['abcd', '123', 'xyz', '456']
# for ele in l:
#     if ele.isnumeric():
#         print(ele)
#---------------------------------------------------------
'''36. write a func to print the below output
func('TRACXN', 0) ---> should print RCN
func('TRACXN', 1) ---> should print TAX'''
# def func(a, n):
#     if n ==0:
#         print(a[1::2])
#     elif n==1:
#         print(a[::2])
#
# func('TRACXN', 0)
# func('TRACXN', 1)

#----------------------------------------------------------
'''37. wap to find the sum of all numbers in the below string'''
# str_ = 'Sony12India567Pvt29ltd'  #[1, 2, 5, 6, 7, 2, 9]
# sum_ = 0
# for ele in str_:
#     if ele.isnumeric():
#         sum_ += int(ele)
#
# print(sum_)

## ALternate solution
# import re
# str_ = 'Sony12India567Pvt29ltd'
# res = re.findall('\d', str_)
# print(res)      #['1', '2', '5', '6', '7', '2', '9']
# sum_ = 0
# for ele in res:
#     sum_ += int(ele)
#
# print(sum_)

#--------------------------------------------------------
'''38. wap to find the sum of all numbers in the below string'''
# str_1 = 'Sony12India567Pvt29ltd'  ##[12, 567, 29]
# import re
# str_ = 'Sony12India567Pvt29ltd'
# res = re.findall('\d+', str_)
# print(res)      #['12', '567', '29']
# sum_ = 0
# for ele in res:
#     sum_ += int(ele)
#
# print(sum_)
# ------------------------------------------------------------------
'''39. wap to print the number of occurances of characters in a string without using
inbuilt methods'''
# s = 'python is a programming language'
# d = {}
# for ele in s:
#     if ele not in d:
#         d[ele] = 1
#     else:
#         d[ele] += 1
#
# print(d)
#-----------------------------------------------------------------
'''40. wap to print only the repeated characters in a string'''
# str_2 = 'hello world'
# for ele in str_2:
#     if str_2.count(ele) > 1:
#         print(ele)

#------------------------------------------------------------
'''41. wap to get alternate characters of a string in list format'''
# str_2 = 'hello universe'
# list_ = []
# for ele in range(0, len(str_2), 2):
#     list_.append(str_2[ele])
#
# print(list_)

## Alternate
# str_2 = 'hello universe'
# list_ = []
# for ele in str_2[::2]:      #hlouies
#     list_.append(ele)
#
# print(list_)

#-----------------------------------------------------------------------
'''42. wap to get the squares of list of numbers'''     #l = [21, 2, 35, 67, 89, 65]
# l = [21, 2, 35, 67, 89, 65]
# squares_list = []
# for num in l:
#     squares_list.append(num ** 2)
#
# print(squares_list)

#-----------------------------------------------------------
'''43. write a func that accepts two strings and returs True if the two strings are anagrams
of each other'''
# def anagrams(str1, str2):
#
#     a = sorted(str1)
#     b = sorted(str2)
#
#     if str1 == str2:
#         return 'Same strings not allowed'
#     elif a==b :
#         return True
#     else:
#         return False
#
# print(anagrams('silent', 'listen'))
# print(anagrams('silent', 'listenss'))
# print(anagrams('silent', 'silent'))

#---------------------------------------------------------------------------
'''44. wap to iterate through a list and build a new list, only if the items in the list has
even number of characters'''
# l = ['apple', 'google', 'microsoft', 'ajio', 'uber', 'myntra', 'yahoo']
# even_list = []
# for ele in l:
#     if len(ele) % 2 == 0:
#         even_list.append(ele)
#
# print(even_list)

#_---------------------------------------------
'''45. wap to iterate through a list and build a new dict, the even len elements should
be the key and its length should be the value'''
# l = ['apple', 'google', 'microsoft', 'ajio', 'uber', 'myntra', 'yahoo']
# even_dict = {}
# for ele in l:
#     if len(ele) % 2 == 0:
#         even_dict[ele] = len(ele)
#
# print(even_dict)
#--------------------------------------------------------
'''46. wap which squares the numbers in the list using map object'''
# ## map(func, iterable)
# l = [2, 4, 6, 8, 10]
# res = map(lambda n : n ** 2, l)
# print(res)      #map object
# print(list(res))
#
# ## Alternate
# l = [2, 4, 6, 8, 10]
# def square(n):
#     return n ** 2
#
# result = map(square, l)
# print(list(result))

#----------------------------------------------------------
'''47. wap to count the number of lines in the file'''
## Using for loop
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample2.txt'
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     print(count)

## Alternate solution
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample2.txt'
# with open(path) as file:
#     lines = file.readlines()
#     print(len(lines))
#------------------------------------------------------
'''48. wap to print the line and line number'''
## Using enumerate
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample2.txt'
# with open(path) as file:
#     for line_no, line in enumerate(file, start=1):
#         print(line_no, line)

## Alternate solution
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample2.txt'
# with open(path) as file:
#     line_num = 1
#     for line in file:
#         print(line_num, line)
#         line_num += 1

#--------------------------------------------------
'''49. wap to print the sum of entire list and the sum of internal list'''
# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ## [6, 15, 24]      #45
# total = []
# for ele in l:
#     total += [sum(ele)]
#
# print(total)        #[6, 15, 24]
# print(sum(total))   #45

#-------------------------------------------------
'''50. wap to reverse the list as below'''
# words = ['hi', 'hello', 'python']
# ## op --> ['nohtyp', 'olleh', 'ih']
# reverse_list = []
# for ele in words:
#     reverse_list.append(ele[::-1])
# print(list(reversed(reverse_list))) #['nohtyp', 'olleh', 'ih']

#-----------------------------------------------
'''51. wap to merge the tuples'''
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# print(t1 + t2)      #(1, 2, 3, 4, 5, 6)
# print((*t1, *t2))   #(1, 2, 3, 4, 5, 6)

#--------------------------------------------------------
'''52. wap to replace the value present in nested disctionary'''
# d = {'a':100, 'b':{'m':'man', 'n':'nose', 'c':'cat'}}
# ## replace nose with net
#
# for ele in d.values():
#     if isinstance(ele, dict):
#         ele['n'] = 'net'
# print(d)    #{'a': 100, 'b': {'m': 'man', 'n': 'net', 'c': 'cat'}}

#------------------------------------------------
'''53. write a list comprehension to get the list of even numbers from 1-50'''
even_num = [ele for ele in range(1, 51) if ele%2==0]
print(even_num)
#----------------------------------------------------------------
'''54. wap to count the number of white spaces in the file'''
## Solution 1
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample2.txt'
# with open(path) as file:
#     for line in file:
#         white_space_count = 0
#         for ele in line:
#             if ele==' ':
#                 white_space_count += 1
#         print(white_space_count)

## Using RegEx
# import re
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample2.txt'
# with open(path) as file:
#     for line in file:
#         res = re.findall('\s', line)
#         print(len(res))
#--------------------------------------------------------
'''55. difference between normal dict and default dict
Defaultdict
-----------
1. When each key is encountered for the first time, it will not be there in the mapping.
2. So an entry is automatically created with default value (an empty list in case of defaultdict of list and zero in case of defaultdict int).
3. When keys are encountered again, the look-up proceeds normally as like a normal dictionary.
4. So, in defaultdict, creation of key, initialisation will happen simultaneously. 

Normal Dictionary
------------------
1. In case of normal dictionary, if the key does not exist, "KeyError" is raised. 
2. In order to work on the value, first the key needs to be created and initialised.
'''
#------------------------------------------------------
'''56. Property decorator 
Property decorators are specific type of decorators that are applied to class properties
or attributes to provide custom behaviour when accessing setting or deleting the value of the 
property
'''
#----------------------------------------------------
'''57. Mutable and immutable datatypes'''
#-------------------------------------------------------
'''58. Explain get() method in dict'''
# d = {'a':10, 'b':20, 'c':30, 'd':40}
# # print(d['a'])       #10
# # print(d['z'])       #KeyError
#
# print(d.get('a'))       #10
# print(d.get('z'))       #None

## whenever the key is present, the square bracket method will give the corresponding
## value of the key. When key is not present, it will give error
## In case of get method, if key is not present, it will not give error, instead it will give None



#-------------------------------------------------------
'''59. '''
#--------------------------------------------------
'''60. Find the longest non-repeated substring in the below string'''
# s = 'python is a programming language and programming is easy'
# res = s.split()
# # ['python', 'is', 'a', 'programming', 'language', 'and', 'programming', 'is', 'easy']
#
# max_len = res[0]
# for ele in res:
#     if len(ele) > len(max_len):
#         if res.count(ele)==1:
#             max_len = ele
#
# print(max_len)
#--------------------------------------------
'''61. wap to find the duplicate elements in the list without using inbuilt methods'''
# l = ['apple', 'google', 'apple', 'gmail', 'yahoo', 'yahoo']
# duplicate = []
# unique = []
# for ele in l:
#     if ele in unique:
#         duplicate.append(ele)
#     else:
#         unique.append(ele)
# print(unique)
# print(duplicate)
#----------------------------------------------
'''62. wap to count the number of occurances of each item in the list without using
inbuilt methods'''
# l = ['apple', 'google', 'apple', 'gmail', 'yahoo', 'yahoo']
# d = {}
# for ele in l:
#     if ele in d:
#         d[ele] += 1
#     else:
#         d[ele] = 1
#
# print(d)

## USing inbuilt
# l = ['apple', 'google', 'apple', 'gmail', 'yahoo', 'yahoo']
# d = {}
# for ele in l:
#     d[ele] = l.count(ele)
#
# print(d)

## Using counter
# l = ['apple', 'google', 'apple', 'gmail', 'yahoo', 'yahoo']
# from collections import Counter
# res = Counter(l)
# print(res)      #Counter({'apple': 2, 'yahoo': 2, 'google': 1, 'gmail': 1})

#---------------------------------------------
'''63. write a func to check if the number is prime'''
# num = int(input('Enter the num: '))
#
# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             print('Not a prime')
#             break
#     else:
#         print('Prime')
#
# is_prime(num)



#-------------------------------------------------------
'''64. create a tuple using the range'''
# print(tuple(range(1, 10)))

#--------------------------------------------------------
'''65. wap to find the largest number in the list without using inbuilt methods'''
# l = [100, 98, 90, 101, 23, 32, 104, 91]
# max_num = l[0]
# for ele in l:
#     if ele > max_num:
#         max_num = ele
#
# print(max_num)
#--------------------------------------------------------
'''66 Write a method that returns the last digit of an integer. For example,
 the call of get_last_digit(3572) should return 2.**
'''
# def get_last_digit(num):
#     res = str(num)
#     return int(res[-1])
#
# print(get_last_digit(3572))
#--------------------------------------------------------------
'''67 Write a program to find most common words in a given list.**
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
'eyes', 'look', 'into','my', 'eyes', "you're", 'under'
]'''

# words = [
# 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
# 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
# 'eyes', 'look', 'into','my', 'eyes', "you're", 'under'
# ]

# d = {}
# for ele in words:
#     if ele not in d:
#         d[ele] = 1
#     else:
#         d[ele] += 1
#
# print(d)
#
# res = sorted(d.items(), key=lambda item:item[-1])
# print(res[-1])

## USing counter
# from collections import Counter
# res = Counter(words)
# print(res)
# common = res.most_common()
# print(common[0])

#-------------------------------------------------------------------
'''68. Make a func names tail that takes the sequence(list, str, tuple) and a number
and returns the last n elements from the given sequence as a list'''
# def tail(iterable, n):
#     if isinstance(iterable, (str, list, tuple)):
#         if n < 0:
#             return 'not valid'
#         else:
#             return iterable[-n:]
#
# print(tail('python', -3))
# print(tail('python', 3))

#--------------------------------------------------------------
'''70 Write a program to get all the duplicate items and the number of times the 
item is repeated in the list
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
'''
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
# unique_elements = set(names)
# # print(unique_elements)      #{'yahoo', 'google', 'apple', 'facebook', 'gmail'}
# for ele in unique_elements:
#     if names.count(ele) > 1:
#         print(ele, names.count(ele))

#-------------------------------------------------------
'''71 Write a program to count the number of occurrences of each word in a file'''
# from collections import defaultdict
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(path) as file:
#     def_dict = defaultdict(int)
#     for line in file:
#         if line.strip():
#             res = line.split()
#             for ele in res:
#                 def_dict[ele] += 1
#
#     print(def_dict)

#------------------------------------------------------------------
# def positive(func):
#     def wrapper(num1, num2):
#         if num1 > num2:
#             return func(num1, num2)
#         else:
#             raise Exception
#     return wrapper
#
# @positive
# def sub(a, b):
#     return a - b
#
# print(sub(14, 19))

#-----------------------------------------------------------------
'''72 Write a program to count the number of occurrences of vowels in a file '''
# from collections import defaultdict
# path = r'C:\Users\Ramya\PycharmProjects\qsp_9AM\file_handling_files\sample1.txt'
# with open(path) as file:
#     def_dict = defaultdict(int)
#     for line in file:
#         if line.strip():
#             for ele in line:
#                 if ele in 'aeiouAEIOU':
#                     def_dict[ele] += 1
#
#     print(def_dict)

#------------------------------------------------------
'''73 Write a program to print all numeric values in a list '''
# l = ['apple', 9, 8.2, 100, 'hai', 'welcome', 20]
# for ele in l:
#     if isinstance(ele, (int, float)):
#         print(ele)

#---------------------------------------------------------
'''74 Triangle Patterns
*         
* *       
* * *     
* * * *   
* * * * * 
'''
# for ele in range(1, 6):
#     print('* ' * ele)

'''
        * 
      * * 
    * * * 
  * * * * 
* * * * *
'''
# for ele in range(1, 6):
#     print(f"{'* ' * ele:>10}")

'''
    *     
   * *    
  * * *   
 * * * *  
* * * * *
'''
# for ele in range(1, 6):
#     print(f"{'* ' * ele:^10}")

#--------------------------
'''
* * * * * * 
* * * * * 
* * * * 
* * * 
* *   
*
'''
# for ele in range(6, 0, -1):
#     print('* ' * ele)

'''
* * * * * * 
  * * * * * 
    * * * * 
      * * * 
        * * 
          * 
'''
# for ele in range(6, 0, -1):
#     print(f"{'* ' * ele:>12}")

'''
 * * * * * *
  * * * * * 
   * * * *  
    * * *   
     * *    
      * 

'''
# for ele in range(6, 0, -1):
#     print(f"{'* ' * ele:^12}")

#---------------------------------------------
'''
1    
12   
123  
1234 
12345
'''
# res = ''
# for ele in range(1, 6):
#     res += str(ele) +' '
#     print(res)

#----------------------------
'''
5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1
'''
# res = ''
# for ele in range(5, 0, -1):
#     res += str(ele) +' '
#     print(res)

#---------------------------
'''
        5 
      5 4 
    5 4 3 
  5 4 3 2 
5 4 3 2 1 
'''
# res = ''
# for ele in range(5, 0, -1):
#     res += str(ele) +' '
#     print(f'{res:>10}')

#--------------------------
'''
a 
a b 
a b c 
a b c d 
a b c d e 
'''
# res = ''
# for ele in range(ord('a'), ord('f')):
#     res += chr(ele) +' '
#     print(res)

#--------------------------------
'''
        a 
      a b 
    a b c 
  a b c d 
a b c d e 
'''
# res = ''
# for ele in range(ord('a'), ord('f')):
#     res += chr(ele) +' '
#     print(f'{res:>10}')
#----------------------------------------------
# res = ''
# for ele in 'python':
#     res += ele +' '
#     print(f'{res:>12}')







