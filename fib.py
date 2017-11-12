import sys


def fib(n):
	fib_nums = [1, 1]
	for i in range(2, n):
		fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
	return fib_nums[-1]


print(fib(int(sys.argv[1])))
