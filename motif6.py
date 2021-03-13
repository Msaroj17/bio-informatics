import random
from Bio.Seq import Seq
from Bio import SeqUtils
I=int(input("enter the length of motif:-"))
file=open("h1n1.txt","r")
r=file.read()
print("sequence:\n",r)
size=len(r)
print("size of the sequence:",size)
pos=random.randint(0,len(r)-I)
print("position",pos)
motif=r[pos:pos+I]
print("motif",motif)
results=SeqUtils.nt_search(str(r),motif)
print("Match motif:",results)

i=pos+1
while(i<size-1):
    if(motif==r[i:i+I]):
        str1=r[i:i+I]
        print("match motif:",str1)
        file1=open("motoutput.txt","a")
        file1.write(str1+"")
    i+=1




#method-2(by taking pattern from the user)

#from Bio.Seq import Seq
#from Bio import SeqUtils

#to take input pattern sequence from user
#pattern=Seq(input("Enter the sequence pattern:"))

#TO OPEN THE FASTA FILE IN READING MODE
#file=open("h1n1.txt","r")

#THE READ DATA WILL STORE IN THIS VARIABLE
#r=Seq(file.read())
#print("sequence:\n",r)

#THIS WILL PRINT THE SIZE OF NUCLEOTIDE SEQUENCE
#size=len(r)

#print("size of the sequence:",size)
#results=SeqUtils.nt_search(str(r),pattern)
#print("Match motif:",results)

