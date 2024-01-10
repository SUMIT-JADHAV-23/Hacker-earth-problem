# def findsubarray(arr):
#     n = len(arr)
#     subarray = set()
#     l = []
#     for i in range(0, n):
#         for j in range(i+1, n+1):
#             subarray=arr[i:j]
#             l.append(subarray)
#     return l
#
#
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     res = findsubarray(arr)
#     print(res)


# def findsubarray(arr):
#     n = len(arr)
#     subarrays = set()
#     for i in range(0, n):
#         for j in range(i, n):
#             subarray = arr[i:j+1]
#             subarrays.add(tuple(subarray))
#     return subarrays
#
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     res = findsubarray(arr)
#     print(res)


"""def findsumarray(arr):
    n = len(arr)

    sums = 0

    l = []

    for i in range(0, n):

        sums = 0

        for j in range(i, n):
            sums = sums + arr[j]

            l.append(sums)

    return (max(l))
"""

# l=[[5], [5, -2], [5, -2, 7], [5, -2, 7, -3], [-2], [-2, 7], [-2, 7, -3], [7], [7, -3], [-3]]
# n=len(l)
# sums=set()
# l2=[]
# for i in range(0,n):
#     print(i)
#     sums=0
#  for j in range(i,n):
#      sums=sums+l[j]
#      print(sums)
#      l2.append(sums)
# print(l2)
#

# l = [[5], [5, -2], [5, -2, 7], [5, -2, 7, -3], [-2], [-2, 7], [-2, 7, -3], [7], [7, -3], [-3]]
# n = len(l)
# sum_1=[]
# max_sum = []
# for x in l:
#     if len(x)==1:
#         sum_1.append(x)
#     else:
#         n = len(l)
#         subarray_sums = []
#         max_sum = []
#         for i in range(0, n):
#             current_sum = 0
#             for j in range(i, n):
#                 current_sum = sum(l[i:j + 1])
#                 subarray_sums.append(current_sum)
#         max_sum.append(max(subarray_sums))
# print(sum_1)
# print(subarray_sums)






# l = [[5], [5, -2], [5, -2, 7], [5, -2, 7, -3], [-2], [-2, 7], [-2, 7, -3], [7], [7, -3], [-3]]
# sum_1 = []
# max_sums = []
#
# for x in l:
#     if len(x) == 1:
#         sum_1.append(x[0])
#     else:
#         n = len(x)
#         subarray_sums = []
#         for i in range(0, n):
#             current_sum = 0
#             for j in range(i, n):
#                 current_sum += x[j]
#                 subarray_sums.append(current_sum)
#         max_sums.append(max(subarray_sums))
#
# print( sum_1)
# print( max_sums)
# l1=sum_1+max_sums
# l2=set(l1)
# l3=sum(l2)
# print(l1)
# print(l2)
# print(l3)



"""
# l= [5,-2,7,-3]
# n = len(l)
# subarray_sums = []
# max_sum=[]
# for i in range(0,n):
#     current_sum = 0
#     for j in range(i, n):
#         current_sum = sum(l[i:j+1])
#         subarray_sums.append(current_sum)
# max_sum.append(max(subarray_sums))
# print(subarray_sums)
# print(max_sum)
"""

# sum_1=[5, -2, 7, -3]
# max_sum=[5, 10, 10, 7, 7, 7]
# l1=sum(set((sum_1)+(max_sum)))
# print(l1)







def findsubarray(arr):
    n = len(arr)
    subarray = set()
    l = []
    for i in range(0, n):
        for j in range(i+1, n+1):
            subarray=arr[i:j]
            l.append(subarray)
    sum_1 = []
    max_sums = []
    for x in l:
        if len(x) == 1:
            sum_1.append(x[0])
        else:
            n = len(x)
            subarray_sums = []
            for i in range(0, n):
                current_sum = 0
                for j in range(i, n):
                    current_sum += x[j]
                    subarray_sums.append(current_sum)
            max_sums.append(max(subarray_sums))
    l1=sum(set((sum_1)+(max_sums)))
    return l1


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    res = findsubarray(arr)
    print(res)





