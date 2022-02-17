#!/usr/bin/env python3

result = 0
for i in range(1, 1001):
	if str(i)[-1] == 0 or str(i)[-1] == 5:
		result += i
	else:
		digit_sum = sum([int(x) for x in str(i)])
		if digit_sum % 3 == 0:
			result += digit_sum
print(result)
