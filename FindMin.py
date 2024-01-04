"""You are given an array A consisting of N non-negative integers.
Find out the minimum number K  such that there exists a non-empty subset of A for
which the bitwise OR of all its elements is equal to K.
"""

# Input the number of test cases
t = int(input("Enter the number of test cases: "))

for i in range(t):
    # Input the number of elements in the array
    n = int(input("Enter the number of elements in the array: "))

    # Input the array elements
    arr = list(map(int, input("Enter space-separated array elements: ").split()))

    # Find and print the minimum value in the array
    min_value = min(arr)
    print("Minimum value in the array:", min_value)


t = 2  # Number of test cases

# Test Case 1
n1 = 5  # Number of elements in the array for Test Case 1
arr1 = [3, 1, 4, 2, 8]  # Array elements for Test Case 1
print("Minimum value in the array for Test Case 1:", min(arr1))

# Test Case 2
n2 = 3  # Number of elements in the array for Test Case 2
arr2 = [7, 5, 2]  # Array elements for Test Case 2
print("Minimum value in the array for Test Case 2:", min(arr2))


"""
t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(min(arr))
"""

