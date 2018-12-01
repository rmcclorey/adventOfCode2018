#usr/bin/python3

import part1 

#Super ugly, and time consuming. Learn about set() its supposed to be far faster
def firstCopy(fileName):
	nums = part1.getNums(fileName)
	counter = 0
	listSums = []
	while(True):
		for i in nums:
			counter += i
			if counter in listSums:
				return counter
			listSums.append(counter)

def main():
	print(firstCopy("input.txt"))


if __name__ == "__main__":
	main()

