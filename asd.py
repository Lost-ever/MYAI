import csv

file = open(r"D:\AIproject\QAp.csv" , "w" , newline="")
file1  = open(r"D:\AIproject\QAp1.csv" , "r")
reader = list(csv.reader(file1)) 
writer = csv.writer(file)
for i in reader:
    writer.writerow(i)
print("complete")
file.close()
file1.close()
