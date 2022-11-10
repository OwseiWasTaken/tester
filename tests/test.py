#! /usr/local/bin/python3.11
#imports
from sys import exit

#simple in-out-return tests

#in
# don't
#out
# don't
# don't hi
#return
# 0

#in
# ?
#out
# uwu
#return
# 1

#main
def Main() -> int:
	x = input("")
	if x == "don't":
		print(x)
		print(x+" hi")
		return 0
	print("uwu")
	return 1

#start
if __name__ == '__main__':
	exit(Main())
