#! /usr/local/bin/python3.11
#imports
from lib.basics import *
from lib.keys import GetKey as gtk
from lib.commands import CheckLine

# sets


def _scheck(c, e):
	# make files to diff
	with open("tmp1", 'w') as f:
		f.write(c)
	with open("tmp2", 'w') as f:
		f.write(e)
	# get diff output (and remove last \n)
	sbp = ''.join(list(map(chr, subprocess.run(("diff", "tmp1", "tmp2"), capture_output=True).stdout)))[:-1]
	ss("rm tmp1")
	ss("rm tmp2")
	if sbp:
		return (
			cyan+'{\n'+nc+sbp+cyan+'\n}'+nc
		)
	return (
		f"{green}"
		f"got correct output"
		f"{nc}"
	)

def _rcheck(c, e):
	if c == e:
		return (
			f"{green}"
			f"expected and got {c}"
			f"{nc}"
		)
	return (
		f"{red}"
		f"expected {e}, got {c}"
		f"{nc}"
	)

@dataclass
class Rule:
	def __init__(this, name, input=[], output=[], ExitCode=0, UseArgsNotInput=False):
		this.name=name
		this.input='\n'.join(input)
		this.output='\n'.join(output)
		this.UseArgsNotInput=UseArgsNotInput
		this.ExitCode=ExitCode

class Tester:
	def __init__(this, name:str, program:str, *rules:Iterable[Rule]):
		this.name = name
		this.program = program
		this.rules = list(rules)

	def AddRule(this, rule):
		this.rules.append(rule)

	def run(this):
		checks = []
		outs = []
		print("running programs")
		for rule in this.rules:
			outs.append(cmd(this.program, text = True, input = rule.input, capture_output=True))
		print(f"\nrunning test schedule {this.name}")
		for i in r(this.rules):
			rule = this.rules[i]
			c = outs[i]
			scheck = _scheck(c.stdout, rule.output)
			rcheck = _rcheck(c.returncode, rule.ExitCode)
			checks.append(
				f"Rule \"{rule.name}\" {i+1}:\n"
				f"return: {rcheck}\n"
				f"stdout: {scheck}\n"
			)
		return checks

def GetLine(y) -> str:
	line = ""
	x = 0
	stdout.write(f"\x1B[{y+1};1H>")
	while True:
		stdout.flush()
		k = gtk()
		if len(k) == 1:
			line = line[:x] + k + line[x:]
			x+=1
		else:
			match (k):
				case ("space"):
					line = line[:x] + ' ' + line[x:]
					x+=1
				case ("backspace"):
					if line and x:
						line = line[:x-1] + line[x:]
						x-=1
					ClearLine(y)
				case ("left"):
					if x:
						x-=1
				case ("right"):
					if x < len(line):
						x+=1
				case ("enter"):
					break
		stdout.write(f"\x1B[{y+1};1H>")
		stdout.write(line)
		stdout.write(f"\x1B[{y+1};{2+x}H")
	return line

def  Interactive() -> int:
	return 0

#main
def Main() -> int:
	ss("clear")
	print(CheckLine("run 3"     , 1))
	print(CheckLine("run all"   , 1))
	print(CheckLine("help run"  , 1))
	print(CheckLine("make test" , 1))
	print(CheckLine("make test" , 1))

	#x = GetLine(0)
	#x2 = GetLine(1)
	#print()
	#print(x, x2)

	#r1 = Rule("exitcode", ["nothing"], [""], 1)
	#r2 = Rule("don't", ["don't"], ["don't\n"])
	#t = Tester("main", "./test.py", r1, r2)
	#for t in t.run():
	#	print(t)

	return 0


#start
if __name__ == '__main__':
	exit(Main())
