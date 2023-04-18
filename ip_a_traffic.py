import csv

fio=[]
ip=[]
int_traffic=[]
with open('ip_a_traffic.csv') as f:
    reader=csv.reader(f,delimiter=';')
    next(reader)
    for i in reader:
        fio.append(i[0])
        ip.append(i[1])
        traffic=i[2:]
        da=[int(x) for x in traffic]
        int_traffic.append(sum(da))