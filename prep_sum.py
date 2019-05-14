f=open('stn_summer.csv','r')
f1=open('prep_sum.csv','w')

d={}

for line in f:
    data=line.split(',')
    station=int(data[0])
    year=int(data[1])
    month=int(data[2])
    day=int(data[3])
    if data[7]!='':
        prep=float(data[7])
    else:
        prep=0

    if not station in d.keys():
        d[station]={year:{month:[prep]}}
    elif not year in d[station].keys():
        d[station][year]={month:[prep]}
    elif not month in d[station][year].keys():
        d[station][year][month]=[prep]
    else:
        d[station][year][month].append(prep)


st=d.keys()
st.sort()

for stn in st:
    for yr in d[stn].keys():
        sum_prep=0
        for mon in d[stn][yr].keys(): 
            sum_prep=sum_prep+sum(d[stn][yr][mon])

        f1.write(str(stn)+','+str(yr)+','+str(sum_prep)+','+'\n')

f1.close()
