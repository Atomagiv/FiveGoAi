from copy import deepcopy as dp
from copy import copy
from random import *
from time import *
import math
class FiveGoAi():
	"""docstring for FiveGoAi"""
	#type == 1 black
	#type == 0 white
	#typr == -1 is null
	#n,m are map's size
	#map is map
	def __init__(self, goType , goMap):
		self.goType=goType
		self.n=len(goMap)
		self.m=len(goMap[0])
		self.goMap=goMap
		self.step=0

	def calNum(self, goType , dx, dy ,x ,y):
		'''calculate the go's value'''
		n=self.n
		m=self.m
		score=((n-x)*(m-y)*x*y//n+int(random()*2))
		x1=copy(x)
		y1=copy(y)
		num=0
		kong=0
		#right & down
		while (x<n and y<m and y>=0 and x>=0) :
			if (self.goMap[x][y]==goType) :
				num=num+1
			else :
				if self.goMap[x][y]==-1 :
					kong=kong+1
				break
			x=x+dx
			y=y+dy
		x=x1
		y=y1
		#left & up
		while (x>=0 and x<n and y>=0 and y<m) :
			if (self.goMap[x][y]==goType) :
				num=num+1
			else :
				if self.goMap[x][y]==-1 :
					kong=kong+1
				break
			x=x-dx
			y=y-dy
		num=num-1
		if num>=5 or (kong==2 and num>=4) :
			score=score+100000000
			return score
		if kong==1 and num>=4 :
			score=score+10000000
			return score
		if num>=5 :
			score=score+100000000
		else :
			if kong==0 :
				num=num-1
			if kong==2 :
				num=num+1
			score=score+5^num
		return score


	#For a map,give a scope of white or black
	def giveScore(self,goType):
		n=self.n
		m=self.m
		score=0
		i=0
		j=0
		while (i<n):
			j=0
			while (j<m):
				if (self.goMap[i][j]==goType) :
					x=copy(i)
					y=copy(j)
					score=score+self.calNum(goType,1,1,x,y)
					score=score+self.calNum(goType,0,1,x,y)
					score=score+self.calNum(goType,1,0,x,y)
					score=score+self.calNum(goType,-1,1,x,y)
				if (self.goMap[i][j]==1-goType) :
					x=copy(i)
					y=copy(j)
					score=score-self.calNum(1-goType,1,1,x,y)
					score=score-self.calNum(1-goType,0,1,x,y)
					score=score-self.calNum(1-goType,1,0,x,y)
					score=score-self.calNum(1-goType,-1,1,x,y)
				j=j+1
			i=i+1
		return score

	def search(self,x,y,level,goType,standord=-1000000000):
		n=self.n
		m=self.m
		if level==1 :
			return self.giveScore(goType)
		if goType==self.goType:
			score=-1000000000
		else :
			score=1000000000
		i=0
		while (i<n):
			j=0
			while (j<m):
				if (self.goMap[i][j]==-1) :
					self.goMap[i][j]=copy(goType)
					if goType==self.goType :
						score=max(score,self.search(i,j,level-1,not goType,score))
						if score>=standord :
							self.goMap[i][j]=-1
							return score
					else :
						score=min(score,self.search(i,j,level-1,not goType,score))
						if score<=standord :
							self.goMap[i][j]=-1
							return score
					self.goMap[i][j]=-1
				j=j+1
			i=i+1
		return score

	def decideTurn(self):
		n=self.n
		m=self.m
		goType=self.goType
		score=-1000000000
		i=0
		j=0
		while (i<n):
			j=0
			while (j<m):
				if (self.goMap[i][j]==-1) :
					self.goMap[i][j]=self.goType
					x=self.search(i,j,2,not self.goType,score)
					if score<x:
						self.step=(i,j)
						score=x
					self.goMap[i][j]=-1
				j=j+1
			i=i+1
		return self.step




