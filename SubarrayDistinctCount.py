# Function to calculate distinct sub-array
# def countDistictSubarray(arr, n):
# 	unst1 = set(arr)
# 	totalDist = len(unst1)
# 	count = 0
#
# 	for i in range(n):
# 		unst = set()
# 		for j in range(i, n):
# 			unst.add(arr[j])
# 			if len(unst) == totalDist:
# 				count += 1
#
# 	return count
#
# # Driver code
# arr = [2, 1, 3, 2, 3]
# n = len(arr)
#
# print(countDistictSubarray(arr, n))

# sub-arrays having total distinct elements
# same as that original array.
"""
#first line contain arr size secound line contain number of interger
n = int(input())
arr = list(map(int, input().split()))

"""


# Print special set for each subarray
def count_distinct_subarrays(n, arr):
    distinct_subarrays = set()

    for i in range(n):
        #we get set for when both the i and j having same value then make it 1 speacil set
        special_set = set()
        for j in range(i, n):
            #add the arr(j) to set and make subarray
            special_set.add(arr[j])
            #now after getting final subarray they make count of subarrays
            distinct_subarrays.add(tuple(sorted(special_set)))
            # Print special set for each subarray
            print(f"Special Set of numbers in subarray [{i+1} {j+1}]: {sorted(special_set)}")

    return len(distinct_subarrays)

# Input
n = 3
arr = 1, 1,2

# Output
result = count_distinct_subarrays(n, arr)
print(f"\nNumber of distinct subarrays: {result}")

#print distinct subarrays
def count_distinct_subarrays(n, arr):
    distinct_subarrays = set()

    for i in range(n):
        subarray=set()
        for j in range(i, n):
            subarray.add(arr[j])
            distinct_subarrays.add(tuple(sorted(subarray)))
            # Print distinct subarray
            print(f"Distinct Subarray: {distinct_subarrays}")

    return len(distinct_subarrays)

# Input
n = 3
arr =1,1,2

# Output
result = count_distinct_subarrays(n, arr)
print(f"\nNumber of distinct subarrays: {result}")



"""
#def function that call distinct subarray
def CountDistinctarray(n, arr):
    #make empty set for collect distinct array and remove duplicate
    distinct_array=set()

    for i in range(n):
        special_set=set()
        for j in range(i,n):
            special_set.add(arr[j])
            distinct_array.add(tuple(sorted(special_set)))
    return len(distinct_array)

n = int(input())
arr = list(map(int, input().split()))

result=CountDistinctarray(n,arr)
print(result)
"""


"""
# Function to calculate distinct sub-array
def countDistictSubarray(arr, n):
    # Count distinct elements in whole array
    vis = dict()
    for i in range(n):
        vis[arr[i]] = 1
    k = len(vis)
    print(k)

    # Reset the container by removing
    # all elements
    vid = dict()

    # Use sliding window concept to find
    # count of subarrays having k distinct
    # elements.
    ans = 0
    right = 0
    window = 0
    for left in range(n):

        while (right < n and window < k):

            if arr[right] in vid.keys():
                vid[arr[right]] += 1
            else:
                vid[arr[right]] = 1

            if (vid[arr[right]] == 1):
                window += 1

            right += 1

        # If window size equals to array distinct
        # element size, then update answer
        if (window == k):
            ans += (n - right + 1)

        # Decrease the frequency of previous
        # element for next sliding window
        vid[arr[left]] -= 1

        # If frequency is zero then decrease
        # the window size
        if (vid[arr[left]] == 0):
            window -= 1

    return ans


# Driver code
arr = [2, 1, 3, 2, 3]
n = len(arr)
print(f'length of arr {n}' )

print(countDistictSubarray(arr, n))
"""