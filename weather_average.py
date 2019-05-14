g=open('stn_spring.csv','r')
g1=open('weather_average.csv','w')

d={}
e={}
f={}
for line in g:
    data=line.split(',')
    station=int(data[0])
    year=int(data[1])
    month=int(data[2])
    day=int(data[3])
    if data[4]!='':
        tavg=float(data[4])
    if data[5]!='':
        tmax=float(data[5])
    if data[6]!='':
        tmin=float(data[6])
        
    if not station in d.keys():
        d[station]={year:{month:[tavg]}}
    elif not year in d[station].keys():
        d[station][year]={month:[tavg]}
    elif not month in d[station][year].keys():
        d[station][year][month]=[tavg]
    else:
        d[station][year][month].append(tavg)

    if not station in e.keys():
        e[station]={year:{month:[tmax]}}
    elif not year in e[station].keys():
        e[station][year]={month:[tmax]}
    elif not month in e[station][year].keys():
        e[station][year][month]=[tmax]
    else:
        e[station][year][month].append(tmax)

    if not station in f.keys():
        f[station]={year:{month:[tmin]}}
    elif not year in f[station].keys():
        f[station][year]={month:[tmin]}
    elif not month in f[station][year].keys():
        f[station][year][month]=[tmin]
    else:
        f[station][year][month].append(tmin)


st=d.keys()
st.sort()
st=e.keys()
st.sort()
st=f.keys()
st.sort()

for stn in st:
    for yr in d[stn].keys():
        avg_tavg=0
        avg_tmax=0
        avg_tmin=0
        for mon in d[stn][yr].keys(): 
            avg_tavg=avg_tavg+sum(d[stn][yr][mon])/len(d[stn][yr][mon])
            avg_tmax=avg_tmax+sum(e[stn][yr][mon])/len(e[stn][yr][mon])
            avg_tmin=avg_tmin+sum(f[stn][yr][mon])/len(f[stn][yr][mon])

        avg_tavg=round(avg_tavg/3,1)
        avg_tmax=round(avg_tmax/3,1)
        avg_tmin=round(avg_tmin/3,1)
        g1.write(str(stn)+','+str(yr)+','+str(avg_tavg)+','+str(avg_tmax)+','+str(avg_tmin)+','+'\n')

g1.close()
