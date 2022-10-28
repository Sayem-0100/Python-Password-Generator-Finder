import os
from random import randint
from time import sleep

f=input("Enter file name :")
paslen=int(input("Enter maxmimum langth of your password should be in "+f+"(default starts from 1000) : "))
len=int(input("how many password you want (int) :"))

fl=open(f+".txt","w+")
lis=list()

while(len>=0):
	lis.append(randint(10000,paslen))
	sleep(.070)
	print(len)
	len=len-1
	if(len==0):
		for i in lis:
			fl.write(str(i)+"\n")
		break;

