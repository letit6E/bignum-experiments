from fractions import Fraction
from random import uniform

from system_solving import gauss, int_gauss


def to_fraction(flt):
	exp = len(str(flt)) - str(flt).find('.') - 1
	return Fraction(int(str(flt).replace('.', '')), 10 ** exp)


def gauss_experiment(variables_count, equations_count, max_number, solving_function):
	coeffs = [
		[uniform(-max_number, max_number) for _ in range(variables_count)]
		for _ in range(equations_count)
	]
	right_values = [
		uniform(-max_number, max_number)
		for _ in range(equations_count)
	]

	solution = solving_function(
		coeffs,
		right_values,
		variables_count,
		equations_count
	)

	return float(sum([
		abs(
			sum([
				solution[i] * to_fraction(coeffs[j][i]) for i in range(len(solution))
			]) - to_fraction(right_values[j])
		)
		for j in range(equations_count)
	]))


sizes = [25, 50, 75]
funcs = [gauss.solve, int_gauss.solve]
experiments_count = 50

for size in sizes:
	print(size)
	for solving_fun in funcs:
		for _ in range(experiments_count):
			print(gauss_experiment(size, size, 1e15, solving_fun), end=' ')
		print()

