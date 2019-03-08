from random import random

def printintro():
	print("Please input A,B between 0 and 1")

def getinputs():
	a=eval(input("A:"))
	b=eval(input("B:"))
	n=eval(input("N:"))
	return a,b,n

def printsum(winsA,winsB):
	n=winsA+winsB
	print("sum={}".format(n))
	print("A wins {} times, which takes up{:.1%}".format(winsA,winsA/n))
	print("B wins {} times, which takes up{:.1%}".format(winsB,winsB/n))

def gameover(scoreA,scoreB):
	return (scoreA==15 or scoreB==15)

def simone(probA,probB):
	scoreA,scoreB=0,0
	serving='A'
	while not gameover(scoreA,scoreB):
		if serving=='A':
			if random()<probA:
				scoreA+=1
			else:
				serving='B'
		else:
			if random()<probB:
				scoreB+=1
			else:
				serving='A'
	return scoreA,scoreB
	
def simNgames(n,probA,probB):
	winsA,winsB=0,0
	for i in range(n):
		scoreA,scoreB=simone(probA,probB)
		if scoreA>scoreB:
			winsA+=1
		else:
			winsB+=1
	return winsA,winsB

def main():
	printintro()
	probA,probB,n=getinputs()
	winsA,winsB=simNgames(n,probA,probB)
	printsum(winsA,winsB)

main()