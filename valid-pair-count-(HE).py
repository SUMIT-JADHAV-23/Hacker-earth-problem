'''
N=int(input())
print(N)
#splits the input into a list of strings based on whitespace
wealth=list(input().split())
print(wealth)
'''

'''
numbers = [1, 5, 2, 4]
result_set = set()
#we use set()function only allows unique elements (dont alloes duplicate) and gives output in order
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        pair_sum = numbers[i] + numbers[j]
        result_set.add(pair_sum)

result_list = list(result_set)
print(result_list)

'''

'''
numbers = [1, 5, 2, 4]
result_set = set()
#N is to decied the length of input list
N = len(numbers)  # Calculate the length of the list once
# then we need to add this num to each other we need to nasted loop concept
# i.e one loop inside another loop to perform repeted action within loop or combination of loop values
for i in range(N):
    for j in range(i + 1, N):
        pair_sum = numbers[i] + numbers[j]
# when the pair sum is found the it added in variable (result set) within the set () data type to avoid duplicates
        result_set.add(pair_sum)
# the reason behind this to perform well in furthur code we change it to list
# i.e set() dont support indexing and list make it in order
result_list = list(result_set)
print(result_list)
'''

'''
N=int(input())
#splits the input into a list of strings based on whitespace
wealth=list(input().split())
result_set = set()

for i in range(N):
    for j in range(i + 1, N):
        pair_sum = wealth[i] + wealth[j]
        result_set.add(pair_sum)

result_list = list(result_set)
print(result_list)
'''

'''
N=int(input())
# Use map to apply the int type  to each element in the list
wealth=list(map(int,input().split()))
result_set = set()

for i in range(N):
    for j in range(i + 1, N):
        pair_sum = wealth[i] + wealth[j]
        result_set.add(pair_sum)

result_list = list(result_set)
print(result_list)
'''

'''
def power_of_three(num):
# use of num<= 0 bcoz negative numbers and zero cannot be powers of 3.
    if num <= 0:
        return False
#
    while num % 3 == 0:
        num //= 3

    return num == 1
'''

'''
 # Initialize a counter for the number of elements that are powers of three
 count_power_of_three = 0

 # Iterate over elements in result_set
 for num in result_set:
     if power_of_three(num):
         count_power_of_three += 1
'''

'''
#This line initializes to keep track of the number of valid pairs.
# Initialize a counter for valid pairs
valid_pairs = 0
#to Check if Pair Sum is a Power of 3
 if power_of_three(pair_sum):
# If the pair sum is a power of 3, the valid_pairs counter is incremented by 1
# indicating that a valid pair has been found , also incremented in the older value
            valid_pairs += 1
'''

'''
def is_power_of_three(num):
    # Check if a number is a power of 3
    if num <= 0:
        return False

    while num % 3 == 0:
        num //= 3

    return num == 1

# Number of people
N = int(input())

# Use map to apply the int type to each element in the list
wealth = list(map(int, input().split()))

# Set to store unique pair sums
result_set = set()

# Count of valid pairs
valid_pairs_count = 0

# Iterate over all pairs of people
for i in range(N):
    for j in range(i + 1, N):
        pair_sum = wealth[i] + wealth[j]

        # Check if the pair sum is a power of 3
        if is_power_of_three(pair_sum):
            valid_pairs_count += 1
            result_set.add((wealth[i], wealth[j]))  # Optionally, store the pair

# Print the count of valid pairs and the pairs themselves
print(f"Number of valid pairs: {valid_pairs_count}")
print(f"Valid pairs: {result_set}")
'''