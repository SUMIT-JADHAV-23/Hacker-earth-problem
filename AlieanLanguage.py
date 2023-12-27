"""Problem
Little Jhool considers Jaadu to be a very close friend of his.
But, he ends up having some misunderstanding with him a lot of times,
because Jaadu's English isn't perfect, and Little Jhool sucks at the language Jaadu speaks.
So, he's in a fix - since he knows that Jaadu has got magical powers,
he asks him to help so as to clear all the issues they end up having with their friendship.
Now, Jaadu can only focus at one task, so to fix these language issues he comes up with a magical way out,
but someone needs to do the rest of it; this is where Little Jhool has asked for your help.
Little Jhool says a word, and then Jaadu says another word.
If any sub-string of the word said by Jaadu is a sub-string of the word said by Little Jhool,
the output should be "YES", else "NO". (Without the quotes.)
Input:
First line contains number of test case T.
Each test case contains two strings *Text ( Said by Jhool ) * and Pattern (Said by Jaadu ).
Both strings contains only lowercase alphabets ['a'-'z'].
Output:
For each test case print YES if any sub-string of Pattern is sub-string of Text else print NO."""


"""
def is_substring(pattern, text):
    for i in range(len(pattern)):
        for j in range(i + 1, len(pattern) + 1):
            substring = pattern[i:j]
            if substring in text:
                return "YES"
    return "NO"

# Input reading
T = int(input("Enter the number of test cases: "))

for _ in range(T):
    text = input().lower()
    pattern = input().lower()

    # Output result for each test case
    result = is_substring(pattern, text)
    print(result)
"""

#
# n = int(input("number of test cases: "))
# for i in range(n):
#     #lower ()function use for input always get in lower alphbet
#     name = input().lower()
#     check = input().lower()
# print(name)
# print(check)

# n = int(input())
# for i in range(n):
#     name = input().lower()
#     check = input().lower()
#     # using if else condition
#     if check in name:
#         print("YES")
#     else:
#         print("NO")
"""
# using dict and for loop we get the count of each substring
n1 = "hello"
n2 = "world"
m = {}
f = 0

# Count occurrences of characters in n1
for i in n1:
    if i not in m:
        #If it's not in the dictionary, it adds the character to the dictionary with a value of 1
        m[i] = 1
        print(m[i])
    else:
        #If the character is already in the dictionary, it increments its value by 1
        m[i] += 1
        f = 1  # Set f to 1 if there is at least one repeated character in n1

# print(m[i])= dictionary m becomes: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Check characters in n2 against the counts in m
for i in n2:
    if i in m:
        # If any character in the m is already in the dictionary (if i in dict), 
        # it sets f to 0 and breaks out of the loop
        f = 0
        break  # 'w' is not in m, so f remains 0

# Since f is 0, print 'YES'
print('YES')
print(m)
"""

for i in range(int(input())):
    text = input()
    pattern = input()

    dict = {}
    f = 0

    for i in text:
        if i not in dict:
            m[i] = 1
        else:
            m[i] += 1
            f = 1

    for i in pattern:
        if i in dict:
            f = 0
            break

    if f == 0:
        print('YES')
    else:
        print('NO').

"""
def is_substring(pattern, text):
    text_length = len(text)
    print(text_length)
    pattern_length = len(pattern)
    print(pattern_length)

    for i in range(text_length - pattern_length + 1):
        # print(pattern_length + 1)
        substring = text[i:i + pattern_length]
        print(substring)
        if substring == pattern:
            return "YES"

    return "NO"

# Example usage
pattern = "efghw"
text = "xyzabcw"

result = is_substring(pattern, text)
print(result)
"""




"""

t = int(input())
for i in range(t):
    st = input()
    ans = input()
    n = {}

    for i in st:
        if i not in n:
            n[i] = 1
        else:
            n[i] += 1

    res = 1

    for i in ans:
        if i in n:
            res = 0
            break

    print("YES") if res == 0 else print("NO")
"""