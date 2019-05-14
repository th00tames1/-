f=open('day_seoul.txt','r')
f1=open('day_seoul_29.txt','w')

for line in f:
    data=line.split('\t')
    year=data[0]
    month=data[1]
    day=data[2]
    tavg=data[3]

    if( int(month)==2 and int(day) in range(29,30)):
        f1.write('')
    else:
        f1.write(year+'\t'+month+'\t'+day+'\t'+tavg+'\t'+'\n')
f1.close()
