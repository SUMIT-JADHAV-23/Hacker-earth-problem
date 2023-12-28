"""
Little Jhool is still out of his mind - exploring all his happy childhood memories. And one of his favorite memory is when he found a magical ghost, who promised to fulfill one of Little Jhool's wish.

Now, Little Jhool was a kid back then, and so he failed to understand what all could he have asked for from the ghost. So, he ends up asking him something very simple. (He had the intuition that he'd grow up to be a great Mathematician, and a Ruby programmer, alas!) He asked the ghost the power to join a set of *the letters r, u, b and y * into a real ruby. And the ghost, though surprised, granted Little Jhool his wish...

Though he regrets asking for such a lame wish now, but he can still generate a lot of real jewels when he's given a string. You just need to tell him, given a string, how many rubies can he generate from it?

Input Format:
The first line contains a number t - denoting the number of test cases.
The next line contains a string.

Output Format:
Print the maximum number of ruby(ies) he can generate from the given string.
"""

"""# Python program to illustrate count()
txt = 'I love Python programming'

# Lowercase o
substring = 'o'
count = txt.count(substring)
print('No. of occurrences of - o: ', count)
# Uppercase O, case-sensitive function
print('No. of occurrences of - O: ', txt.count('O'))

txt = 'I am ill. Will you buy these medicines for me?'
count = txt.count('ill')
print('No. of occurrences of - ill: ', count)

# Python program to illustrate count()
string = 'Good morning, everyone, Welcome back to school'

# search starts from index = 8
c = string.count('o', 8)
print('The count for letter o:', c)

# search starts from index = 10 and ends at index = 25
c = string.count('e', 10, 25)
print('The count for letter e:', c)
"""

#=int(input())
# s=list(input().split())
# print(n)
# print(s)

for _ in range(int(input())):
    n=input()
    print(n)
"""

"""
#to get minimum count of (r,u,b,y)

n="rrrruubbbyy"
r=n.count("r")
u=n.count("u")
b=n.count("b")
y=n.count("y")
min_count=min(r,u,b,y)
print(min_count)

#
# for _ in range(int(input())):
#     n = input()
#
#     count_r = n.count('r')
#     count_u = n.count('u')
#     count_b = n.count('b')
#     count_y = n.count('y')
#
#     min_count = min(count_r, count_u, count_b, count_y)
#
#     if min_count > 0:
#         print(min_count)
#     else:
#         print('0')


#
# n = "adfrggrfafubsbysgy"
# count = {}
#
# for i in n:
#     if i == "r" or i == "u" or i == "b" or i == "y":
#         if i not in count:
#             count[i] = 1
#         else:
#             count[i] += 1
#
# print(min(count.values()))


for _ in range(int(input())):
    n=input()
    count={}

    for i in n :
        if i=="r" or i=="u" or i=="b" or i=="y":
            if i not in count:
                count[i]=1
            else:
                count[i] +=1
    print(min(count.values()) if len(count) >= 4 else '0')
