"""
the problem statement is that we have given a arry A and a num k these two diff element
we need find out that num k is sum of all arry A menas A== k then print YES or NO
line 1- conatin two integer denoting size of array and num k
line 2- contian n int num space separeted denoting array in given size
example - (5,9) ,(1 2 3 4 5) output=YES
"""

#use of two pointer method
# def isPairSum(A, N, X):
#
# 	for i in range(N):
# 		for j in range(N):
#
# 			# as equal i and j means same element
# 			if(i == j):
# 				continue
#
# 			# pair exists
# 			if (A[i] + A[j] == X):
# 				return True
#
# 			# as the array is sorted
# 			if (A[i] + A[j] > X):
# 				break
#
# 	# No pair found with given sum
# 	return 0
#
#
# # Driver code
# arr = [2, 3, 5, 8, 9, 10, 11]
# val = 17
#
# print(isPairSum(arr, len(arr), val))
#



#
# #takes input as string and splits into a list of substrings on whitespace
# #map fun() to each element of the list obtained from input().split().
# # It converts each string element in the list to an integer
# #This unpacks the tuple into the variables n and k
# n, k = map(int, input().split())
# print("size of array",n)
# print("num k",k)
# print(n,k)
# #takes input as string and splits into a list of substrings on whitespace
# #converts the mapped values into a list
# # Example
# # If the user enters "2 4 7 3 9" as input, the value of array_a would be:
# # array_a = [2, 4, 7, 3, 9]
# array_a = list(map(int, input().split()))
# print(array_a)
#
#
# #we had a arr now sort in order in ascedeing order
# #sort fuct work on list not tuple
# arr=[12,45,52,2,35,24]
# arr.sort()
# print(arr)
#
# # Sorting array_a in descending order in-place
# arrr=[12,45,52,2,35,24]
# arrr.sort(reverse=True)
# print(arrr)
# #sorted "ed" use when assinging with new vaeriable
# array_a=[12,45,52,2,35,24]
# array_a = sorted(array_a, reverse=True)
# print(array_a)
# #
#
'''
# The initialization of two pointers, left and right,
# is a common technique in algorithms called the Two Pointers Technique
arr=[2, 4, 7, 8, 11, 15]
left, right = 0, 5  # Initialization
while left < right:
    current_sum = arr[left] + arr[right]  # Sum of elements at indices 0 and 5 (2 + 15)
    # Since current_sum (17) is less than 18, move left pointer to the right
    left += 1
    # Now, left = 1, right = 5
    current_sum = arr[left] + arr[right]  # Sum of elements at indices 1 and 5 (4 + 15)
    # Since current_sum (19) is greater than 18, move right pointer to the left
    right -= 1
    # Now, left = 1, right = 4
    current_sum = arr[left] + arr[right]  # Sum of elements at indices 1 and 4 (4 + 11)
    # Since current_sum (15) is less than 18, move left pointer to the right
    left += 1
    # Now, left = 2, right = 4
    current_sum = arr[left] + arr[right]  # Sum of elements at indices 2 and 4 (7 + 11)
    # Since current_sum (18) is equal to 18, return "YES"
    print("Pair found:", arr[left], arr[right])  # Output the pair found
    break  # Exit the loop since the pair is found
'''
'''
arr=[2, 4, 7, 8, 11, 15]
left, right = 0, 5  # Initialization

while left < right:
    current_sum = arr[left] + arr[right]  # Sum of elements at indices 0 and 5 (2 + 15)
    # Since current_sum (17) is less than 18, move left pointer to the right
    left += 1
    # Now, left = 1, right = 5
    current_sum = arr[left] + arr[right]  # Sum of elements at indices 1 and 5 (4 + 15)
    # Check if current_sum is equal to the target sum (18)
    if current_sum == 18:
        print("Pair found:", arr[left], arr[right])
        break
    # Since current_sum (19) is greater than 18, move right pointer to the left
    right -= 1
    # Now, left = 1, right = 4
    current_sum = arr[left] + arr[right]  # Sum of elements at indices 1 and 4 (4 + 11)
    # Since current_sum (15) is less than 18, move left pointer to the right
    left += 1
    # Now, left = 2, right = 4
    current_sum = arr[left] + arr[right]  # Sum of elements at indices 2 and 4 (7 + 11)
    # Check if current_sum is equal to the target sum (18)
    if current_sum == 18:
        print("Pair found:", arr[left], arr[right])
        break
'''
# def has_pair_with_sum(arr, k):
#     left, right = 0, len(arr) - 1
#
#     while left < right:
#         current_sum = arr[left] + arr[right]
#         # print(arr[left])
#         # print(arr[right])
#         # print(current_sum)
#         if current_sum == k:
#             return "YES"
#         elif current_sum != k:
#             left += 1
#         else:
#             right -= 1
#
#     return "NO"
# # Example usage
# arr = [2, 4, 3,4]
# k = 5
# result = has_pair_with_sum(arr, k)
# print(result)

#
# # Function to check if there exists a pair with the given sum using Two Pointers Technique
# def pair_with_sum(arr, k):
#     # Sort the array in ascending order
#     arr.sort()
#
#     # Initialize two pointers, left at the beginning, and right at the end of the sorted array
#     #This sets left to the index 0 (beginning of the array)
#     # and right to the index len(arr) - 1, indicate the index of the last element in the array.
#     left, right = 0, len(arr) - 1
#
#     # Continue the loop until the pointers meet(until this condition fails)
#     while left < right:
#         # Calculate the sum of the elements pointed to by left and right pointers
#         current_sum = arr[left] + arr[right]
#
#         # Check if the current sum is equal to the target sum, k
#         if current_sum == k:
#             return "YES"
#         # If the current sum is less than the target sum, move the left pointer to the right
#         elif current_sum < k:
#             left += 1
#         # If the current sum is greater than the target sum, move the right pointer to the left
#         else:
#             right -= 1
#
#     # If the pointers meet and no pair is found, return "NO"
#     return "NO"
#
# # Input reading
# n, k = map(int, input().split())
# array_a = list(map(int, input().split()))
#
# # Output result
# result = pair_with_sum(array_a, k)
# print(result)
'''
def has_pair_with_sum(arr, k):
    arr.sort()
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == k:
            return "YES"
        elif current_sum < k:
            left += 1
        else:
            right -= 1

    return "NO"

# Input reading
n, k = map(int, input().split())
array_a = list(map(int, input().split()))

# Output result
result = has_pair_with_sum(array_a, k)
print(result)
'''


# use of nested if
def has_pair_with_sum(arr, k):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == k:
                return "YES"
    return "NO"

# Input reading
n, k = map(int, input().split())
array_a = list(map(int, input().split()))

# Output result
result = has_pair_with_sum(array_a, k)
print(result)
#
