import numpy as np

# 1. Creating Matrices
# Initials: JNL => [10, 14, 12]
# Second letters: OEL => [15, 5, 12]
first_matrix = np.array([[10, 14, 12], [15, 5, 12]])
print("First Matrix:\n", first_matrix)

# Student number: 202458 => [2, 0, 2], [4, 5, 8]
second_matrix = np.array([[2, 0, 2], [4, 5, 8]])
print("\nSecond Matrix:\n", second_matrix)

# 2. Matrix Addition
third_matrix = first_matrix + second_matrix
print("\nThird Matrix (Addition):\n", third_matrix)

# 3. Scalar Multiplication
fourth_matrix = first_matrix * 2
print("\nFourth Matrix (Scalar Multiplication):\n", fourth_matrix)

# 4. Matrix Transpose
fifth_matrix = second_matrix.T
print("\nFifth Matrix (Transpose of Matrix 2):\n", fifth_matrix)

# 5. Matrix Multiplication
sixth_matrix = np.dot(third_matrix, fifth_matrix)
print("\nSixth Matrix (Matrix Multiplication):\n", sixth_matrix)

# 6. Sum of all elements in Matrix 3
sum_third_matrix = np.sum(third_matrix)
print("\nSum of all elements in Third Matrix:", sum_third_matrix)

# 7. Zero Matrix
seventh_matrix = np.zeros((2, 3))
print("\nSeventh Matrix (Zero Matrix):\n", seventh_matrix)
