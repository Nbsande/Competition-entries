import numpy as np
#Get book scores
with open("d_tough_choices.txt") as f:
	In=f.readline()
	In=In.strip().split(" ")
	totBooks=int(In[0])
	# Books=np.array(arrange(int(In[0])))
	done=[True for x in np.arange(int(In[0]))]
	totLibs=int(In[1])
	totDays=int(In[2])
	scores=np.array([int(x) for x in f.readline().strip().split(" ")])
	In=f.read().splitlines()

booksIn={str(k):[] for k in np.arange(totBooks)}
currLine=0
temp=In[currLine].split(" ")
numBooks=temp[0]
signupPeriod=temp[1]
booksPd=temp[2]
booksPresent=In[currLine+1].split(" ")

class Library:
	def __init__(self, signupPeriod,booksPd,bookList,numBooks,selfID,score=0):
		self.signupPeriod = int(signupPeriod)
		self.booksPd = int(booksPd)
		self.bookList=bookList
		self.score=0
		self.numBooks=int(numBooks)
		self.selfID=selfID
		for x in self.bookList:
			self.score+=scores[int(x)]
			booksIn[x].append(selfID)


	def updateScore(self):
		for x in self.bookList:
			if not done[x]:
				self.score-=scores[x]
		return score
	def getScore(self):
		return self.score
	def scoreSub(self,sub):
		self.score-=sub
	def rmBook(self,book):
		self.bookList=[value for value in self.bookList if value != str(book)]
		self.score-=scores[int(book)]

def CreateLibs():
	self_id=0
	libs=[]
	libScores=np.array([])
	currLine=0
	try:
		while(1):
			temp=In[currLine].split(" ")
			currBookNum=temp[0]
			signupPeriod=temp[1]
			booksPd=temp[2]
			booksPresent=In[currLine+1].split(" ")
			libs.append(Library(signupPeriod,booksPd,booksPresent,currBookNum,self_id))
			libScores=np.append(libScores,libs[-1].getScore())
			self_id+=1
			currLine+=2
	except IndexError:
		# print("error")
		pass
	return libs,libScores

def FindMaxScore(libs,libScores):
	i=max(libScores)
	if(i==0):
		return -1
	return np.where(libScores==i)[0][0]

def Bookorder(libs,libScores,index,maxNum):
	bks=libs[index].bookList.copy()
	scrs=np.array([scores[int(x)] for x in bks])
	out=""
	count=0
	while(len(scrs)>0 and count<maxNum):
		i=np.where(scrs==max(scrs))[0][0]
		out+=str(bks[i])+" "
		scrs=np.delete(scrs,i)
		del bks[i]
		count+=1
	return libs[index].bookList,out,count
def updateScores(libs):
	return np.array([x.score for x in libs])

def main():
	out=""
	libs,libScores=CreateLibs()
	currentDays=totDays

	c=0
	while(1):
		c+=1
		maxIndex=FindMaxScore(libs,libScores)

		if(maxIndex==-1):
			break

		currentDays-=libs[maxIndex].signupPeriod
		if(currentDays<0):
			break
		maxBooks=currentDays*libs[maxIndex].booksPd

		currBookList,currOut,count=Bookorder(libs,libScores,maxIndex,maxBooks)
		out+=str(maxIndex)+" "+str(count)+"\n"+currOut+"\n"

		libScores[maxIndex]=0

		for x in currBookList.copy():
			for ix in range(len(booksIn[x])):
				if(ix!=-1):

					libs[booksIn[x][ix]].rmBook(x)
				booksIn[x][ix]=-1

		libScores=updateScores(libs)
		# break
	out=str(c-1)+"\n"+out
	print(out)

main()
