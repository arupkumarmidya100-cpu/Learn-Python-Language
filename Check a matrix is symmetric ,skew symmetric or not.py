n = int(input("Enter the order of matrix: "))

matrix = []

print("Enter the elements:")

for i in range(n):
    row = []
    for j in range(n):
        num = int(input(f"Enter element [{i}][{j}]: "))
        row.append(num)
    matrix.append(row)

symmetric = True
skew_symmetric = True

for i in range(n):
    for j in range(n):

        if matrix[i][j] != matrix[j][i]:
            symmetric = False

        if matrix[i][j] != -matrix[j][i]:
            skew_symmetric = False

if symmetric:
    print("The matrix is Symmetric.")

elif skew_symmetric:
    print("The matrix is Skew-Symmetric.")

else:
    print("The matrix is neither Symmetric nor Skew-Symmetric.")