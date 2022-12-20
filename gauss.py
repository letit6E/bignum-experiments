def bring_triangular_form(matrix, n, m):
	result = [row.copy() for row in matrix]

	for i in range(n - 2):
		for j in range(i + 1, m):
			if result[j][i] == 0.0:
				continue

			coefficient = result[i][i] / result[j][i]
			for k in range(i, n):
				result[j][k] = result[i][k] - coefficient * result[j][k]

	return result


def solve(coeffs, right_values, variables_count, equations_count):
	matrix = [row.copy() for row in coeffs]

	for i in range(equations_count):
		matrix[i] = matrix[i] + [right_values[i]]

	triangular_form = bring_triangular_form(matrix, variables_count + 1, equations_count)

	ans = []
	for row in triangular_form[::-1]:
		ans.append(
			(row[-1] - sum(ans[i] * row[-i - 2] for i in range(len(ans)))) / row[-len(ans) - 2]
		)

	return ans[::-1]
