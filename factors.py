import sys
import math

def factors(n):
	for x in range(2, int(math.sqrt(n)) + 1):
		if n % x == 0:
			return x, n // x
		return 1, n
	
def main():
	with open(sys.argv[1], 'r') as f:
		for line in f:
			n = int(line)
			p, q = factors(n)
			print(f"{n} = {p} * {q}")

if __name__ == '__main__':
	main()
