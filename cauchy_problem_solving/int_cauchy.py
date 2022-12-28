from fractions import Fraction

from cauchy import get_tags

# approximation constant
N = 20


def solve(tags_diff_parameter, left_bound, right_bound, start_tag, start_value, derivative):
	tags = get_tags(tags_diff_parameter, left_bound, right_bound, start_tag)
	values = [0] * len(tags)
	start_index = tags.index(Fraction(start_tag).limit_denominator())
	values[start_index] = int(start_value * 10 ** (N + tags_diff_parameter))

	for i in range(start_index, len(tags) - 1):
		values[i + 1] = \
			values[i] + int(derivative(tags[i], values[i] / 10 ** (N + tags_diff_parameter)) * 10 ** N)

	for i in range(start_index, 0, -1):
		values[i - 1] = \
			values[i] - int(derivative(tags[i], values[i] / 10 ** (N + tags_diff_parameter)) * 10 ** N)

	return (
		tags,
		list(
			map(
				lambda x: x / 10 ** (N + tags_diff_parameter),
				values
			)
		)
	)
