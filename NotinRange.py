"""
You are given 10**6 boxes that are numbered from 1 to 10**6.
The value of each box is equal to its number.
There are N ranges and every range consists of two integers L and R
denoting that the value of box in the range[L,R] will turn out to be zero.
Find the sum of values of all boxes from 1 to 10**6
Note: The ranges may overlap.
Input format
Firstline: Integer N
Next N lines: Two space-separated integers L and R
Output format
Print a single integer denoting the answer.
"""
#def NotinRange(left,right):
#     x=[]
#     for x in range (left,right):
#         print(x)
#
#
#
#     for x not in range(1,10**6):
#         print(i, end="")
#     print()
#
#
# t=int(input())
#
# for _ in range(t):
#     L,R=list(map(int,input().split()))
#     # print(L)
#     # print(R)
#
#     result=NotinRange(L,R)
#     print(result)
#
#

# x = list(range(1, 10 ** 6 +1))

"""#overlap range adjust in set ()
x=61
l1=set()
for i in range(1,50):
    l1.add(i)
    # print(i,end=" ")
for j in range(30,60):
    l1.add(j)

print(l1,end=" ")
if x not in l1:
    print("True")
else:
    print("false")


"""
#
# l = []
#
# for _ in range(int(input())):
#     a, b = map(int, input().split())
#
#     l.append([a, b])
#
# print(l)
#
# for i in range(l(a,b)):
#     print(i)


"""# Initialize an empty list
l = []
s=set()
# Get input for the number of iterations
for _ in range(int(input())):
    a, b = map(int, input().split())
    l.append([a, b])

# Print the list of pairs
print(l)

# Iterate over the list and print each pair
for pair in l:
    s.add(range(pair[0], pair[1]))

print(s)
"""
# Initialize an empty list
l = []
s = set()

# Get input for the number of iterations
for _ in range(int(input())):
    a, b = map(int, input().split())
    l.append([a, b])

# Print the list of pairs
print(l)

# Iterate over the list and add integers to the set
for pair in l:
    s.update(range(pair[0], pair[1] + 1))

print(list(s))


x = list(range(1, 10 ** 2+1))
print(x)

not_in_range = []
for i in x:
  if i not in s:
    not_in_range.append(i)

print(sum(not_in_range))




#
# def NotinRange (R, L, n):
#     # Write your code here
# n = int(input())
# L, R = [], []
# for i in range(n):
#     x, y = map(int, input().split())
#     L.append(x)
#     R.append(y)
# out_ = NotinRange(R, L, n)
# print(out_)



# if x not in s:
#     print(x)


# accepted
# n = int(input())
# ranges = {int(i[0]): int(i[1]) for i in [list(input().split()) for x in range(n)]}
# print(ranges)
#
#
#
# total = 0
# end = 0
# start = 0
# maxnos = 10 ** 6
# for start in sorted(ranges):
#     if end < start:
#         total += (end + start) * (start - end - 1) / 2
#     end = max(end, ranges[start])
# total += (maxnos + end + 1) * (maxnos - end) / 2
# print(int(total))