import sys

with open(sys.argv[1],'r') as f:
	matrix_A = [list(map(int, line.strip().split())) for line in f]
    
with open(sys.argv[2],'r') as f:
	matrix_B = [list(map(int, line.strip().split())) for line in f]
for i in range(len(matrix_A)):
	for j in range(len(matrix_B[0])):
		for k in range(len(matrix_B)):
			print(f"{i}, {j}\t {matrix_A[i][k]}, {matrix_B[k][j]}")
