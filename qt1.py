from random import *
from time import *
from termcolor import *
from copy import deepcopy as dp
import ai
import cProfile
goMap=[]
n=9
m=9
for i in range(0,n):
	x=[]
	for j in range(0,m):
		print("-+--",end='')
		x.append(-1)
	print(" "+str(i+1)+" ")
	goMap.append(x)
	for j in range(0,m):
		print(" |  ",end='')
	print()
for i in range(1,m+1):
	print(str(i)+"   ",end='')

def check():
	'''check if the game is over '''
	for i in range(0,n):
		for j in range(0,m):
			goType=goMap[i][j]
			if goType==-1 :
				continue
			num=0
			x=dp(i)
			y=dp(j)
			while (x>=0 and x<n and y>=0 and y<m) :
				if (goMap[x][y]==goType) :
					num=num+1
				else :
					break
				x=x+1
			if (num>=5) :
				return True

			num=0
			x=dp(i)
			y=dp(j)
			while (x>=0 and x<n and y>=0 and y<m) :
				if (goMap[x][y]==goType) :
					num=num+1
				else :
					break
				y=y+1
			if (num>=5) :
				return True

			num=0
			x=dp(i)
			y=dp(j)
			while (x>=0 and x<n and y>=0 and y<m) :
				if (goMap[x][y]==goType) :
					num=num+1
				else :
					break
				x=x+1
				y=y+1
			if (num>=5) :
				return True

			num=0
			x=dp(i)
			y=dp(j)
			while (x>=0 and x<n and y>=0 and y<m) :
				if (goMap[x][y]==goType) :
					num=num+1
				else :
					break
				x=x-1
				y=y+1
			if (num>=5) :
				return True
	return False

print()
ai1=ai.FiveGoAi(1,goMap)
ai2=ai.FiveGoAi(0,goMap)

turn=1


while (not check()):
	step=0
	if (turn==1) : 
		# step=input()
		# step=step.split(' ')
		# step=(eval(step[0])-1,eval(step[1])-1)
		# while (goMap[step[0]][step[1]]!=-1):
		# 	print("e....There has been something")
		# 	step=input()
		# 	step=step.split(' ')
		# 	step=(eval(step[0])-1,eval(step[1])-1)
		step=ai1.decideTurn()
		turn=0
	else :
		step=ai2.decideTurn()
		turn=1


	goMap[step[0]][step[1]]=not turn
	ai1.goMap[step[0]][step[1]]=not turn
	ai2.goMap[step[0]][step[1]]=not turn
	for i in range(0,n):
		for j in range(0,m):
			if (goMap[i][j]!=-1) :
				if (goMap[i][j] == 1) :
					print("-",end='')
					cprint("&",'red', 'on_red',end='')
					print("--",end='')
				else :
					print("-",end='')
					cprint("&",'blue', 'on_blue',end='')
					print("--",end='')
			else :
				print("-+--",end='')
		print("  "+str(i+1))
		for j in range(0,m):
			print(" |  ",end='')
		print()
	for i in range(1,m+1):
		print(str(i)+"   ",end='')
	print()
	print(step[0]+1,step[1]+1)
	print("-------------------------------------------")




