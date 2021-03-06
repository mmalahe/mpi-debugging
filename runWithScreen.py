import os
from subprocess import *
import time

# Control
continueImmediately = False

# Other parameters
np = 2
mainScreenName = "debugging"
executable = "main"
waitArg = "-gdbwait"
dontAttachPrefix = "mpirun"
gdbReadyToContinueArgs = ["-x","gdbSetReadyToContinue.txt"]

# Get dictionary from process id to the call string that invoked the process
def getPIDToProcstringDict():
	"""
	Approach taken from http://stackoverflow.com/questions/2703640/process-list-on-linux-via-python
	"""
	pids = {str(pid):'' for pid in os.listdir('/proc') if pid.isdigit()}
	for pid in pids.keys():
		try:
			procString = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
			pids[pid] = procString
		except IOError:
			continue
	return pids

# Create main screen
call(["screen","-AmdS",mainScreenName])

# Create screen for mpirun command
call(["screen", "-S", mainScreenName, "-X", "screen", "mpirun", "-np", str(np), executable, waitArg])

# Pause briefly to allow MPI to launch
time.sleep(0.25)

# Find all the spawned processes and attach to them
allProcs = getPIDToProcstringDict()
waitingProcs = {a:allProcs[a] for a in allProcs.keys() if waitArg in allProcs[a]}
procsToAttachTo = {a:waitingProcs[a] for a in waitingProcs.keys() if not waitingProcs[a].startswith(dontAttachPrefix)}
for pid in procsToAttachTo.keys():
	processWindowName = "debugging-pid="+pid
	screenArgs = ["screen","-S",mainScreenName,"-X","screen","-t",processWindowName]
	gdbArgs = ["gdb"]
	gdbArgs.extend(gdbReadyToContinueArgs)
	if continueImmediately:
		gdbArgs.extend(["-ex","c"])
	gdbArgs.extend([executable, pid])
	fullArgs = screenArgs + gdbArgs
	call(fullArgs)
call(["screen","-r",mainScreenName,"-p","mpirun"])
