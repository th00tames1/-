f=open('GWANCHUK_all.csv','r')
f1=open('stn_summer.csv','w')

for line in f:
    data=line.split(',')
    station=data[0]
    year=data[1]
    month=data[2]
    day=data[3]
    tavg=data[4]
    tmax=data[5]
    tmin=data[6]
    prep=data[7]

    if int(station)==101 or int(station)==108 or int(station)==143:
        if int(month) in range(5,11):
            f1.write(station+','+year+','+month+','+day+','+tavg+','+tmax+','+tmin+','+prep+','+'\n')
f1.close()
