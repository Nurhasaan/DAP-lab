#1. Python program to add two matrices:
def add_matrices(mat1, mat2):
    result = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return result

# Example usage:
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result_matrix = add_matrices(matrix1, matrix2)
print("Sum of matrices:")
for row in result_matrix:
    print(row)
#2. Python program to multiply two matrices:

def multiply_matrices(mat1, mat2):
    result = [[sum(a * b for a, b in zip(mat1_row, mat2_col)) for mat2_col in zip(*mat2)] for mat1_row in mat1]
    return result

# Example usage:
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result_matrix = multiply_matrices(matrix1, matrix2)
print("Product of matrices:")
for row in result_matrix:
    print(row)
#3. Python program for Matrix Product:
# Same as the multiplication example above (multiply_matrices).
# The concept of matrix product is the same as matrix multiplication.
#4. Adding and Subtracting Matrices in Python:
# Same as the addition and subtraction examples provided in the previous response.
# The concepts of adding and subtracting matrices are straightforward.
#5. Transpose a matrix in a single line in Python:

def transpose_matrix(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

# Example usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = transpose_matrix(matrix)
print("Original matrix:")
for row in matrix:
    print(row)
print("Transposed matrix:")
for row in transposed_matrix:
    print(row)
#6. Python | Matrix creation of n*n:

def create_matrix(n):
    return [[0] * n for _ in range(n)]

# Example usage:
n = 3
matrix = create_matrix(n)
print(f"{n}x{n} Matrix:")
for row in matrix:
    print(row)
#7. Python | Get Kth Column of Matrix:

def get_kth_column(mat, k):
    return [row[k] for row in mat]

# Example usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1
column_k = get_kth_column(matrix, k)
print(f"{k}th column of the matrix:", column_k)
#8. Python – Vertical Concatenation in Matrix:

def vertical_concatenation(mat1, mat2):
    return mat1 + mat2

# Example usage:
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
result_matrix = vertical_concatenation(matrix1, matrix2)
print("Vertically concatenated matrix:")
for row in result_matrix:
    print(row)