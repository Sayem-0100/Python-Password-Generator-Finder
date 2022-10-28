import os

f=input("Enter file name :")
pas=input("Enter password :")

list=os.listdir()

for i in list:
	if(i==f+".txt"):
		x=open(i,"r")
		count=1
		lis=x.readlines()
		print("\nReading "+f+"…")
		for i in lis:
			if(i==pas+"\n"):
				os.system("cl")
				print("Password found!\nPosition of Password is "+str(count)+"\n")
				break;
			else:
				count=count+1
				if(count==lis.__len__()):
					print("Password not found!")
					break;
