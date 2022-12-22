from fractions import Fraction
from math import floor


def get_tags(tags_diff_parameter, left_bound, right_bound, start_tag):
	left_index = 0
	while start_tag + Fraction(left_index - 1, 10 ** tags_diff_parameter) >= left_bound:
		left_index -= 1
	right_index = 0
	while start_tag + Fraction(right_index, 10 ** tags_diff_parameter) <= right_bound:
		right_index += 1

	return [start_tag + Fraction(i, 10 ** tags_diff_parameter) for i in range(left_index, right_index)]


def solve(tags_diff_parameter, left_bound, right_bound, start_tag, start_value, derivative):
	tags = get_tags(tags_diff_parameter, left_bound, right_bound, start_tag)
	values = [start_value] * len(tags)
	start_index = tags.index(Fraction(start_tag).limit_denominator())
	for i in range(start_index, len(tags) - 1):
		values[i + 1] = \
			values[i] + derivative(tags[i], values[i]) / 10 ** tags_diff_parameter
	for i in range(start_index, 0, -1):
		values[i - 1] = \
			values[i] - derivative(tags[i], values[i]) / 10 ** tags_diff_parameter

	return tags, values
