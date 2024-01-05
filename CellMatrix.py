"""You are given an integer N denoting an NXN matrix. Initially, each cell of the matrix is empty. You are given k tasks.
In each task, you are given a cell(i,j) where cell (i,j) represents the i row and j column of the given matrix.

You have to perform each task sequentially in the given order. Each task is described in cell(i,j).
For each task, you have to place X  in each cell of row i and each cell column j
. After you complete each task, you are required to print the number of empty cells in the matrix.

Input format
The first line contains two space-separated integers N  and K  where N is the number of rows and
columns in the given matrix and K is the number of tasks respectively.
Next K lines contain two space-separated integers i and j.
Output format
Print k space-separated integers denoting the number of empty cells in the matrix.
"""


def cells_sol(N, K, task):
 # Write your code here
 matrix = [[0] * N for _ in range(N)]
 result = []

 for task in tasks:
  i, j = task
  for x in range(N):
   matrix[i - 1][x] += 1  # Mark cells in the i-th row
   matrix[x][j - 1] += 1  # Mark cells in the j-th column

  empty_cells = sum(row.count(0) for row in matrix)
  result.append(empty_cells)

 return result
 # return # dummy return


N, K = map(int, input().split())
task = []
for _ in range(K):
 i, j = map(int, input().split())
 X = i, j
 task.append(X)

out_ = cells_sol(N, K, task)
for elements in out_:
 print(elements, end=' ')
print()








def perform_tasks(N, K, tasks):
 matrix = [[0] * N for _ in range(N)]
 result = []

 for task in tasks:
  i, j = task
  for x in range(N):
   matrix[i - 1][x] += 1  # Mark cells in the i-th row
   matrix[x][j - 1] += 1  # Mark cells in the j-th column

  empty_cells = sum(row.count(0) for row in matrix)
  result.append(empty_cells)

 return result


# Input
N, K = map(int, input().split())
tasks = [tuple(map(int, input().split())) for _ in range(K)]

# Output
result = perform_tasks(N, K, tasks)
print(*result)







n, k = map(int, input().split())

row = [i for i in range(1, n+1)]
col = [i for i in range(1, n+1)]

for _ in range(k):
    i, j = map(int, input().split())

    if i in row:
        row.remove(i)

    if j in col:
        col.remove(j)

    print(len(row) * len(col), end=" ")






n, k = map(int, input().split(" "))

inp = []

rows = []

columns = []

left = n * n

for _ in range(k):
    j, k = map(int, input().split(" "))

    if j not in rows:
        rows.append(j)
        left = left - n + len(columns)

    if k not in columns:
        columns.append(k)
        left = left - n + len(rows)

    print(left, end=" ")
