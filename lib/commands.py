from lib.basics import *

commands:dict[str, list[str]] = {
	"help": ["?%c",],
	"make": ["rule|test","?%s", "%s", "%b"],
	"run": ["%d|all"],
}

def CheckLine(line:str, verb=False) -> tuple[bool, str]:
	cmd = line.strip().split()
	c = CheckCommandVal(cmd)
	ret = line
	if verb:
		if c:
			ret = green
		else:
			ret = red
		ret += str(c)
		ret += nc
		return f'"{line}": '+ret
	return c, ret

def CheckCommandVal(cmd:list[str]) -> bool:
	if not len(cmd):return False
	cm = commands.get(cmd.pop(0), "")
	if type(cm) != list: return False
	for i in r(cmd):
		c = cm[i]
		cmmd = cmd[i]
		if c[0] == '?':
			if not len(cmd)-i: return True
			else:
				c = c[1:]
		c = c.split('|')

		# make % into list
		rt = []
		for p in c:
			if not ('%' in p):
				rt.append(p)
			else:
				if p == '%c':
					if cmmd in list(commands.keys()):
						rt.append(cmmd)
				if p == '%s':
					rt.append(cmmd)
					continue
				if p == '%b':
					rt+=['1', '0', 'true', 'false', 'True', 'False']
				if p == '%d':
					if cmmd.isdigit():
						rt.append(cmmd)
						continue

		if not cmmd in rt:return False
	# check if more options needed option
	if i < len(cm)-1:
		if cm[i+1][0] != '?':
			return False

	return True

def RunCommand(c, cmd:list[str]):pass

# c = context
def help(c, cmd:str): pass
