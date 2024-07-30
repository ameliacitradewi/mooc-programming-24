# Write your solution here
# Get the number of layers from the user
layers = int(input("Layers: "))

# Calculate the size of the square
size = 2 * layers - 1

# Create an empty matrix to hold the letters
matrix = [[''] * size for _ in range(size)]

# Fill the matrix with the appropriate letters
for i in range(layers):
  letter = chr(ord('A') + layers - 1 - i)
  for j in range(i, size - i):
      matrix[i][j] = letter
      matrix[size - 1 - i][j] = letter
      matrix[j][i] = letter
      matrix[j][size - 1 - i] = letter

# Print the matrix
for row in matrix:
  print(''.join(row))