#/usr/bin/python3

def getNums(fileName):
	nums = []
	with open(fileName) as f:
		for line in f:
			nums.append(int(line))
	return nums


def addNums(fileName):
	nums = getNums(fileName)
	counter = 0
	for i in nums:
		counter += i
	return counter

def main():
	print(addNums("input.txt"))

if __name__ == "__main__":
	main()
