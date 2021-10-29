import csv

with open("HeightAndWeight.csv",newline="") as f:
    reader=csv.reader(f)
    datalist=list(reader)

datalist.pop(0)
newData=[]

for i in range(len(datalist)):
    number=datalist[i][1]
    newData.append(float(number))

n=len(newData)
total=0

for x in newData:
    total+=x

mean=total/n
print(mean)