import csv
file=open('patients.csv','r')
records=list(csv.reader(file))
file.close()
print(records)

for x in records:
    print(x)