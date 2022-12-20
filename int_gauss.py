from fractions import Fraction

# approximation constant
N = 30


# bring the matrix with elements to the triangular form
def int_bring_triangular_form(matrix):
	n = len(matrix[0])
	m = len(matrix)
	# change indexing from i = 0...m-1, j = 0...n-1 to i = 1...m, j = 1...n
	result = [[0] * (n + 1)] + [[0] + row.copy() for row in matrix]

	# save main diagonal of the matrix for applying Sylvester theorem
	diagonal_size = min(n, m)
	main_diagonal = [1] * (diagonal_size + 1)

	for k in range(1, n - 1):
		new_main_diagonal = [result[i][i] for i in range(diagonal_size + 1)]

		# step of bringing to the triangular form
		for i in range(k + 1, m + 1):
			coefficient = result[i][k]
			for j in range(k, n + 1):
				result[i][j] = (result[i][j] * result[k][k] - result[k][j] * coefficient) // main_diagonal[k - 1]

		main_diagonal = new_main_diagonal.copy()

	# back indexing to original
	return [[result[i][j] for j in range(1, n + 1)] for i in range(1, m + 1)]


# solve the system of equations by the Gaussian method
def solve(coeffs, right_values, variables_count, equations_count):
	matrix = [row.copy() for row in coeffs]

	# applying approximation of coefficients
	for i in range(equations_count):
		matrix[i] = list(map(lambda x: int(x * 10 ** N), matrix[i] + [right_values[i]]))

	triangular_form = int_bring_triangular_form(matrix)

	# reverse move of Gaussian method
	ans = []
	for row in triangular_form[::-1]:
		ans.append(
			Fraction(
				row[-1] - sum(ans[i] * row[-i - 2] for i in range(len(ans))),
				row[-len(ans) - 2]
			)
		)

	return ans[::-1]
