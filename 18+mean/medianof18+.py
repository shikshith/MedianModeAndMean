import csv 

with open("HeightAndWeight.csv",newline="") as f:
    reader=csv.reader(f)
    data=list(reader)

data.pop(0)
newAndImprovedData=[]

for i in range(len(data)):
    num=data[i][1]
    newAndImprovedData.append(float(num))

n=len(newAndImprovedData)
newAndImprovedData.sort()

if n % 2 == 0:
    medean1=float(newAndImprovedData[n//2])
    medean2=float(newAndImprovedData[n//2 -1])
    
    medean=(medean1+medean2)/2

else:
    medean=newAndImprovedData[n//2]

print(medean)
