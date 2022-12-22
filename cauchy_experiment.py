import math

from cauchy_problem_solving import cauchy, int_cauchy


def expected_fun(x):
	return 3 / 2 * math.e ** math.tan(x) - 1 / 2


def derivative(x, y):
	return (2 * y + 1) / (math.cos(2 * x) + 1)


def cauchy_experiment(n, left, right, st_tag, st_val, solving_function):
	tags, solution = solving_function(
		n, left, right, st_tag, st_val, derivative
	)

	return sum([
		abs(expected_fun(tags[i]) - solution[i]) for i in range(len(tags))
	])


tags_diff_parameter = 5
bounds = [1.4, 1.5, 1.55]
funcs = [cauchy.solve, int_cauchy.solve]
start = 0
value = 1

for bound in bounds:
	print(bound)
	for fun in funcs:
		print(cauchy_experiment(tags_diff_parameter, -bound, bound, start, value, fun))
