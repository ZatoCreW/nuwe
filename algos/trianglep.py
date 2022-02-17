#!/usr/bin/env python3

result = 0
current_solution = 0

for p in range(2, 1001, 2):
	num_of_solutions = 0
	for a in range(2, p//3):
		if p*(p-2*a) % (2*(p-a)) == 0:
			num_of_solutions += 1
		if num_of_solutions > current_solution:
			current_solution = num_of_solutions
			result = p
print(result)