counter = 0


def move(num, a, b, c):
	global counter
	if num == 1:
		counter += 1
		
		if counter <= 200:
			print('step '+str(counter)+': move number '+str(num)+' plate from '+a+' to '+c)
		else:
			if counter % 1000000 == 0:
				print('step '+str(counter)+': move number '+str(num)+' plate from '+a+' to '+c)
	else:
		move(num-1, a, c, b)
		counter += 1
		if counter <= 200:
			print('step '+str(counter)+': move number '+str(num)+' plate from '+a+' to '+c)
		else:
			if counter % 1000000 == 0:
				print('step '+str(counter)+': move number '+str(num)+' plate from '+a+' to '+c)
		move(num-1, b, a, c)
		


'''
Simplified version
'''
def move_s(num, a, b, c):
	global counter
	if num == 1:
		counter += 1
	else:
		move_s(num - 1, a, c, b)
		counter += 1
		move_s(num - 1, b, a, c)

'''
therefore the Ultrally Simplified version
'''
def move_u(num, a, b, c):
	if num > 1:
		move_u(num - 1, a, c, b)
		move_u(num - 1, b, a, c)
		
		
def main():
	global counter
	n = int(input('please input the number of plates (more than 0):'))
	
	move(n, 'A', 'B', 'C')
	print('Total number of steps is '+str(counter))
	counter = 0
	n = int(input('please input the number of plates (more than 0):'))
	move_s(n, 'A', 'B', 'C')
	print('Total number of steps is '+str(counter))
	counter = 0
	n = int(input('please input the number of plates (more than 0):'))
	move_u(n, 'A', 'B', 'C')
	print('Total number of steps is '+str(counter))
	counter = 0
	
if __name__ == "__main__":
	main()
