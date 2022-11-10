#! /usr/local/bin/python3.11
#imports
from util import *

@dataclass
class Rule:
	def __init__(this, name, input=[], output=[], ExitCode=0, UseArgsNotInput=False):
		this.name=name
		this.input='\n'.join(input)
		this.output='\n'.join(output)
		this.UseArgsNotInput=UseArgsNotInput
		this.ExitCode=ExitCode

red = RGB(255,0,0)
green = RGB(0,255,0)
cyan = RGB(0,255,255)
nc = RGB(255,255,255)

def _scheck(c, e):
	with open("tmp1", 'w') as f:
		f.write(c)
	with open("tmp2", 'w') as f:
		f.write(e)
	sbp = ''.join(list(map(chr, subprocess.run(("diff", "tmp1", "tmp2"), capture_output=True).stdout)))[:-1]
	ss("rm tmp1")
	ss("rm tmp2")
	if sbp:
		return sbp
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

class Tester:
	def __init__(this, program:str, *rules:Iterable[Rule]):
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
		print("\nrunning tests")
		for i in r(this.rules):
			rule = this.rules[i]
			c = outs[i]
			scheck = _scheck(c.stdout, rule.output)
			rcheck = _rcheck(c.returncode, rule.ExitCode)
			checks.append(
				f"Rule \"{rule.name}\" {i+1}:\n"
				f"return: {rcheck}\n"
				f"stdout: {cyan}"'{'f" {nc}{scheck}\n"
				f"{cyan}"'}'f"{nc}\n"
			)
		return checks

#main
def Main() -> int:
	r1 = Rule("exitcode", ["nothing"], [""], 1)
	r2 = Rule("don't", ["don't"], ["don't\n"])
	t = Tester("./test.py", r1, r2)
	for t in t.run():
		print(t)

	return 0





#start
if __name__ == '__main__':
	exit(Main())
