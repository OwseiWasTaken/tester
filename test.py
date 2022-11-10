#! /usr/local/bin/python3.11
#imports
from sys import exit


#main
def Main() -> int:
	x = input("")
	if x == "don't":
		print(x)
		print(x+"hi")
		return 0
	return 1

#start
if __name__ == '__main__':
	exit(Main())
