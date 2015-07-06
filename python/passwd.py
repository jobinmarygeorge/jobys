import base64
import os
f1 = open('user','w')
f2 = open('passwd','w')
f1.write(raw_input())
f2.write(raw_input())
f1.close()
f2.close()
os.system('clear')
print 'enter the input values\n'
username = raw_input()
passwd = raw_input()
f1 = open('user','r')
f2 = open('passwd','r')
if ((username == f1.read())and(passwd == f2.read())):
	print 'authnticated'
else:
	print 'authentication failed'
f1.close()
f2.close()

