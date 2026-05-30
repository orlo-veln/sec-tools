# Imports (none)
# Data
oldfile = '/home/manjushri/scripts/test_data/wtmp.txt'

newfile = '/home/manjushri/scripts/test_data/wtmp_mod.txt'

# Functions
def stravnit (original, modified):
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

stravnit(oldfile, newfile)



