from util import *

red = RGB(255,0,0)
green = RGB(0,255,0)
lgreen = RGB(30,255,60)
cyan = RGB(0,255,255)
nc = RGB(255,255,255)
mx, my = GetTerminalSize()

@dataclass
class Rule:
	def __init__(this, name, input=[], output=[], ExitCode=0, UseArgsNotInput=False):
		this.name=name
		this.input='\n'.join(input)
		this.output='\n'.join(output)
		this.UseArgsNotInput=UseArgsNotInput
		this.ExitCode=ExitCode

class Tester:
	pass

