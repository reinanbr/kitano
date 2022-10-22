from kitano.termux import ShellRun

sr = ShellRun()

sr.prt = True

print('android' in sr.resLine('uname -a'))
sr.runLine('''apt upgrade 
apt list''')

