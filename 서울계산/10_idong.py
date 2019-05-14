f=open('idong_total.txt','r')
f1=open('Weather_2001-2010.txt','w')

#==시작연도, 끝연도 입력==
yr1=2001
yr2=2010
#==시작연도, 끝연도 입력==

spcnt=0; smcnt=0; atcnt=0; wtcnt=0
sp=0; sm=0; at=0; wt=0; wtimsi=0

mth=0
dy=0

for line in f:
    data=line.split('\t')
    year=data[0]
    month=data[1]
    day=data[2]
    tavg=float(data[3])
    iavg=float(data[4])

    if(int(year) in range(yr1,yr2+1)):
        if(sp==0 and sm==0 and at==0 and wt==0):
            wtimsi+=1
            
        #Spring
        if(iavg>=5 and sp==0 and sm==0 and at==0 and wt==0):
            spcnt+=1
            if(spcnt==1):
                mth=month
                dy=day
            if(spcnt==5):
                sp+=1
                f1.write(str(yr1)+'-'+str(yr2)+" Spring"+'\t'+'\n')
                f1.write("Start Date"+'\t'+"Seasonal Length"+'\t'+'\n')
                f1.write(str(mth)+'-'+str(dy)+'\t')
        else:
            spcnt=0
        if(sp>0 and sm==0 and at==0 and wt==0):
            sp+=1

        #Summer
        if(iavg>=20 and sp>0 and sm==0 and at==0 and wt==0):
            smcnt+=1
            if(smcnt==1):
                mth=month
                dy=day
            if(smcnt==5):
                sm+=1
                f1.write(str(sp-2)+'\t'+'\n'+'\n')
                f1.write(str(yr1)+'-'+str(yr2)+" Summer"+'\t'+'\n')
                f1.write("Start Date"+'\t'+"Seasonal Length"+'\t'+'\n')
                f1.write(str(mth)+'-'+str(dy)+'\t')
        else:
            smcnt=0
        if(sp>0 and sm>0 and at==0 and wt==0):
            sm+=1

        #Autumm
        if(iavg<20 and sp>0 and sm>0 and at==0 and wt==0):
            atcnt+=1
            if(atcnt==1):
                mth=month
                dy=day
            if(atcnt==5):
                at+=1
                f1.write(str(sm-2)+'\t'+'\n'+'\n')
                f1.write(str(yr1)+'-'+str(yr2)+" Autumm"+'\t'+'\n')
                f1.write("Start Date"+'\t'+"Seasonal Length"+'\t'+'\n')
                f1.write(str(mth)+'-'+str(dy)+'\t')
        else:
            atcnt=0
        if(sp>0 and sm>0 and at>0 and wt==0):
            at+=1

        #Winter
        if(iavg<5 and sp>0 and sm>0 and at>0 and wt==0):
            wtcnt+=1
            if(wtcnt==1):
                mth=month
                dy=day
            if(wtcnt==5):
                wt=wtimsi
                wt+=1
                f1.write(str(at-2)+'\t'+'\n'+'\n')
                f1.write(str(yr1)+'-'+str(yr2)+" Winter"+'\t'+'\n')
                f1.write("Start Date"+'\t'+"Seasonal Length"+'\t'+'\n')
                f1.write(str(mth)+'-'+str(dy)+'\t')
        else:
            wtcnt=0
        if(sp>0 and sm>0 and at>0 and wt>0):
            wt+=1

f1.write(str(wt-2)+'\t'+'\n'+'\n')

f1.close()
