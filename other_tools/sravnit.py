# Imports
import sys
# Data

# Functions
def sravnit (original, modified):
	with open (original, 'r') as f:
		lines_a = set(f.readlines())

	with open (modified, 'r') as g:
		lines_b = set(g.readlines())
	    	

	difference = []

	for line in lines_a:	
		if line not in lines_b:
			difference.append(line)

	print ("Deleted Lines:")
	for line in difference:	
    		print(line)

# Run

if len(sys.argv) < 3:
	print("Usage: sravnit <original> <modified>")
else:
	sravnit(sys.argv[1], sys.argv[2])




