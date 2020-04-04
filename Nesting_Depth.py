from sys import stdin, stdout
t = int(stdin.readline().strip())
res=[]
for i in range(t):
	str1 = stdin.readline().strip()
	ls=list(str1)
	new=[]
	for x in ls:
		if x == '1':
			new.append('(')
			new.append(x)
			new.append(')')
			continue
		elif x=='2':
		    for i in range(2):
		        new.append('(')
		    new.append(x)
		    for i in range(2):
		        new.append(')')
		    continue
		elif x=='3':
		    for i in range(3):
		        new.append('(')
		    new.append(x)
		    for i in range(3):
		        new.append(')')
		    continue
		elif x=='4':
		    for i in range(4):
		        new.append('(')
		    new.append(x)
		    for i in range(4):
		        new.append(')')
		    continue
		elif x=='5':
		    for i in range(5):
		        new.append('(')
		    new.append(x)
		    for i in range(5):
		        new.append(')')
		    continue
		elif x=='6':
		    for i in range(6):
		        new.append('(')
		    new.append(x)
		    for i in range(6):
		        new.append(')')
		    continue
		elif x=='7':
		    for i in range(7):
		        new.append('(')
		    new.append(x)
		    for i in range(7):
		        new.append(')')
		    continue
		elif x=='8':
		    for i in range(8):
		        new.append('(')
		    new.append(x)
		    for i in range(8):
		        new.append(')')
		    continue
		elif x=='9':
		    for i in range(9):
		        new.append('(')
		    new.append(x)
		    for i in range(9):
		        new.append(')')
		    continue
		new.append(x)
	str2= ''.join(new)
	while ')(' in str2:
	    list_snewl = str2.split(')(')
	    str2 = ''.join(list_snewl)
	res.append(str2)
for index in range(len(res)):
	print('Case #{}: {}'.format(index +1,res[index]))