counts =[3, 15, 247, 8, 103, 1]

def rate_threat(count):
	if count > 100: 
        	return 'HIGH'
	elif count > 10: 
        	return 'MEDIUM'
	else:  
        	return 'LOW'
for count in counts:
	rating = rate_threat(count)
	print(f'{count} attempts: {rating}')

