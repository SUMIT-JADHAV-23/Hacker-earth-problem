'''
n=int(input())

s=input()
t=input()

# print(s,t)
'''
'''
# x, y = input("Enter two values: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)
'''
'''
# n=int(input())
# pairs=[]
#
# for _ in range(n):
#     input_pair = input()
#     s, t = input_pair.split()
#
#     pair.append((s, t))
#
# print("Pairs:")
# for pair in pairs:
#     print(pair)
'''
'''
# s, t = int(input().split())
# print(s)
# print(t)
'''
'''
# Get the number of pairs
# n = int(input("number of pairs: "))
# 
# # Initialize an empty list to store pairs
# pairs = []
# 
# # Loop to take input for each pair
# for _ in range(n):
#     # Input two strings separated by a space
#     input_pair = input("Enter two strings separated by a space: ")
# 
#     # Split the input into two strings
#     s, t = input_pair.split()
# 
#     # Add the pair to the list
#     pairs.append((s,t ))
# 
# 
# # Print the pairs
# print("Pairs:")
# 
# for pair in pairs:
#     print(pair)
'''
'''
s = "str"
t = "brt"

def Anagram(s, t):
    if s == t:
        return True
    else:
        return False

result = Anagram(s, t)
print(result)
'''
# n=int(input())
# for _ in range(n):
#
#      s = sorted(input())
#
#      t = sorted(input())
#
#      print(s)
#      print(t)
#
# def Anagram(s,t):
#         if s==t:
#             return True
#         else:
#             False
#
# r=Anagram(s,t)
# print(r)


'''

def Anagram(s, t):
    for i in (s, t):
        if i == t:
            return True
    return False

s = "abc"
t = "bca"

r = Anagram(s, t)
print(r)
'''


'''
# # use of get() function
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# 
# # Using get() to retrieve values
# value_a = my_dict.get('a')
# value_d = my_dict.get('d', 'Key not found')
# for key in my_dict:
#     x=my_dict.get(key)
#     print(x)
# 
# print(value_a)  # Output: 1
# print(value_d)  # Output: Key not found


def anagrams(s, t):
    # Create dictionaries to store character frequencies
    freq_s = {}
    freq_t = {}

    # Count character frequencies in string s
    for char in s:
        freq_s[char] = freq_s.get(char, 0) + 1
        print(freq_s)

    # Count character frequencies in string t
    for char in t:
        freq_t[char] = freq_t.get(char, 0) + 1
        print(freq_t)

'''
# n=int(input())
# for _ in range(n):
#
#     s = sorted(input())
#
#     t = sorted(input())
#
#     print(s)
#     print(t)
#
# def anagrams(s, t):
#     # Create dictionaries to store character frequencies
#     freq_s = {}
#     freq_t = {}
#
#     # Count character frequencies in string s
#     for char in s:
#         freq_s[char] = freq_s.get(char, 0) + 1
#         print(freq_s)
#
#     # Count character frequencies in string t
#     for char in t:
#         freq_t[char] = freq_t.get(char, 0) + 1
#         print(freq_t)
#
#
# anagrams(s,t)
'''

#find the difeerence between two dict then get only diff keys
dict1 = {'key1': 'Geeks', 'key2': 'For', 'key3': 'geeks'}
dict2 = {'key1': 'Geeks', 'key2': 'Portal'}

diff1 = set(dict2) - set(dict1)
diff2 = set(dict1) - set(dict2)

print(diff1)
print(diff2)

#find the difeerence between two dict then get only similar keys
dict3 = {'a': 1, 'j': 1, 'c': 1}
dict4= {'c': 1, 'b': 1, 'a': 1}

for i in dict3.keys():
    # print(differences)
    if i in dict4:
        print(i)


#find the difference between two dict and add it
# Define two dictionaries
s = {'a': 1, 'j': 1, 'c': 1}
t = {'c': 1, 'b': 1, 'a': 1}

# set function use for compare the keys of the dictionaries
# union it use add the in it
keys = set(s.keys()).union(set(t.keys()))
print(set(s.keys()))
print(set(t.keys()))
print(keys)


#find the difference between the dict del them

# Define two dictionaries
p = {'a': 1, 'j': 1, 'c': 1}
r = {'c': 1, 'b': 1, 'a': 1}

# Find the differences between the two dictionaries
keys = set(dict1.keys()).union(set(dict2.keys()))

for i in p.keys():
    # print(differences)
    if i in r:
        print(i)
#



# Define two dictionaries
x = {'a': 1, 'j': 1, 'c': 1}
y = {'c': 1, 'b': 1, 'a': 1}

# Find the differences between the two dictionaries
keys = set(x.keys()).union(set(y.keys()))
differences = {}
for key in keys:
    if x.get(key) != y.get(key):
        differences[key] = [x.get(key), y.get(key)]

# Print the differences
print("Differences between the two dictionaries:")
'''


'''
# x = {'a': 1, 'j': 1, 'c': 1}
# y = {'c': 1, 'b': 1, 'a': 1}
#
# # Find the differences between the two dictionaries
# keys = set(x.keys()).union(set(y.keys()))
# differences = {}
# for key in keys:
#     #The get() function in Python is a method that is used to access the value of a specified key from a dictionary
#     if x.get(key) != y.get(key):
#         print(x.get(key))
#         print(y.get(key))
#         differences[key] = [x.get(key), y.get(key)]
# print(differences)
# # Print the differences
# print("Differences between the  dictionaries:")
# # for key, values in differences.items():
# #     print(f"Key: {key}, Values: {values}")
#
# for key in differences.items():
#     print(key)
'''

'''
n=int(input())
for _ in range(n):

    s = sorted(input())

    t = sorted(input())

    # print(s)
    # print(t)

def anagrams(s, t):
    # Create dictionaries to store character frequencies
    dict1 = {}
    dict2 = {}

    # Count character frequencies in string s
    for char in s:
        dict1[char] = dict1.get(char, 0) + 1
        # print(dict1)

    # Count character frequencies in string t
    for char in t:
        dict2[char] = dict2.get(char, 0) + 1
        # print(dict2)
    diff = 0
      # Iterate over all unique characters in both dictionaries
    for char in set(dict1.keys()).union(set(dict2.keys())):
       # Calculate the absolute difference in frequencies and add to the running total
       #(+=)) → Add the right side to the left (=+) → Don't use this. Set the left to the right side.
        diff += abs(dict1.get(char, 0) - dict2.get(char, 0))
        # print(dict1.get(char, 0))
        # print(dict2.get(char, 0))
    #
    print(diff)

anagrams(s,t)
'''


def min_operations_to_anagram(s, t):
    # Create dictionaries to store character frequencies
    freq_s = {}
    freq_t = {}

    # Count character frequencies in string s
    for char in s:
        freq_s[char] = freq_s.get(char, 0) + 1

    # Count character frequencies in string t
    for char in t:
        freq_t[char] = freq_t.get(char, 0) + 1

    # Calculate the absolute difference in frequencies
    diff = 0
    for char in set(freq_s.keys()).union(set(freq_t.keys())):
        diff += abs(freq_s.get(char, 0) - freq_t.get(char, 0))

    return diff

# Input reading and processing
T = int(input("Enter the number of test cases: "))
for _ in range(T):
    S = input().strip()
    T = input().strip()
    # Calculate and print the minimum number of operations
    result = min_operations_to_anagram(S, T)
    print(result)
#
#
# def min_operations_to_anagram(s, t):
#     freq_s = {}
#     freq_t = {}
#
#     for char in s:
#         freq_s[char] = freq_s.get(char, 0) + 1
#
#     for char in t:
#         freq_t[char] = freq_t.get(char, 0) + 1
#
#     diff = 0
#     for char in set(freq_s.keys()).union(set(freq_t.keys())):
#         diff += abs(freq_s.get(char, 0) - freq_t.get(char, 0))
#
#     return diff
#
#
# T = int(input())
#
# for _ in range(T):
#     S = input().strip()
#     T = input().strip()
#
#     result = min_operations_to_anagram(S, T)
#     print(result)