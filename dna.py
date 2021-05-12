import sys
import csv


if len(sys.argv)!=3 :
    print("python dna.py data.csv sequence.txt")
    sys.exit(1)

file =open(sys.argv[1],'r')
strands=[]
people={}

for ind, row in enumerate(file):
    if ind==0:
        strands=[strand for strand in row.strip().split(",")[1:]]
        
    else:
        curr_row=row.strip().split(',')
        people[curr_row[0]]=[int(x) for x in curr_row[1:]]
   
dna_strand=open(sys.argv[2],"r").read()
final_strand=[]
for strand in strands:
    i=0
    max_strand=-1
    curr_max=0
    while i<len(dna_strand):
        found_strand =dna_strand[i:i+len(strand)]
        
        if found_strand==strand:
            curr_max+=1
            max_strand=max(max_strand,curr_max)
            i+=len(strand)
        else:
            curr_max=0
            i+=1
    final_strand.append(max_strand)


for name,data in people.items():
   
    if data==final_strand :
        print(name)
        sys.exit(0)
        

print("not found")











#https://github.com/kish-an/cs50/blob/master/pset6/dna/dna.py