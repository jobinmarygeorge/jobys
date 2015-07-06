f = open('u.txt','w')
f.write(raw_input())
f.close()
fin = open('u.txt','r')
print fin.readline()
fin.close()
f1 = open('u.txt','a')
f1.write(raw_input())
f1.close()
fin = open('u.txt','r')
print fin.read()
fin.close()




