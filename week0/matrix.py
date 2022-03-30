def matrix():
  matrix = []
  for i  in range (1):
    matrix.append([])
    for j in range (1,4):
      matrix [i].append(j)
  matrix2 = []
  for i in range (1):
    matrix2.append([])
    for k in range (4,7):
      matrix2 [i].append(k)
  matrix3 = []
  for i in range (1):
    matrix3.append ([])
    for g in range (7,10):
      matrix3 [i].append(g)
  print(matrix)
  print(matrix2)
  print(matrix3)
def print_matrix1(matrix):
  print("lol")
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      print(matrix[i][j], end=" ")
    print()