"""
This script is just here to test attaching the VS Code debugger.
Run it from the command line, then connect to it from VSCode.
Set a breakpoint inside the loop and it should stop there.
Step through (F10) the loop a few times.
When you are done you could set loop to False in the debugger
to see it exit the loop and terminate.
"""
import time
import debugpy
debugpy.listen(5678)

tock = 1
loop = True # Set this to False in the debugger to end the program.

while loop :
    print("Tick", tock)
    tock += 1
    time.sleep(1)

print("We're done here.")
