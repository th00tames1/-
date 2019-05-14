f=open('idong_total.txt','r')
f1=open('Weather_2001-2010_mod.csv','w')

#==시작연도, 끝연도 입력==
yr1=2001
yr2=2010
#==시작연도, 끝연도 입력==

spcnt=0; smcnt=0; atcnt=0; wtcnt=0; wtcnt2=0; wtcnt3=0
sp=0; sm=0; at=0; wt=0; wt2=0; wt3=0
wtimsi=0

amth=0; mth=0; mth2=0; mth3=0
ady=0; dy=0; dy2=0; dy3=0

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
                f1.write(str(yr1)+'-'+str(yr2)+" Spring"+','+'\n')
                f1.write("Start Date"+','+"Seasonal Length"+','+'\n')
                f1.write(str(mth)+'-'+str(dy)+',')
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
                f1.write(str(sp-2)+','+'\n'+'\n')
                f1.write(str(yr1)+'-'+str(yr2)+" Summer"+','+'\n')
                f1.write("Start Date"+','+"Seasonal Length"+','+'\n')
                f1.write(str(mth)+'-'+str(dy)+',')
        else:
            smcnt=0
        if(sp>0 and sm>0 and at==0 and wt==0):
            sm+=1

        #Autumm
        if(iavg<20 and sp>0 and sm>0 and at==0 and wt==0):
            atcnt+=1
            if(atcnt==1):
                amth=month
                ady=day
            if(atcnt==5):
                at+=1
        else:
            atcnt=0
        if(sp>0 and sm>0 and at>0 and wt==0):
            at+=1

        #Winter
        if(iavg<5 and sp>0 and sm>0 and at>0 and wt==0 and wt2==0 and wt3==0):
            wtcnt+=1
            if(wtcnt==1):
                mth=month
                dy=day
            if(wtcnt==5):
                wt+=1

        else:
            wtcnt=0
        if(sp>0 and sm>0 and at>0 and wt>0 and wt2==0 and wt3==0):
            wt+=1


        if(iavg>=5 and sp>0 and sm>0 and at>0 and wt>0 and wt2==0 and wt3==0): #중간에 5도이상이 개입했을 경우
            wtcnt2+=1
            if(wtcnt2==1):
                mth2=month
                dy2=day
            if(wtcnt2==2):
                wt2+=1
        else:
            wtcnt2=0
        if(sp>0 and sm>0 and at>0 and wt>0 and wt2>0 and wt3==0):
            wt2+=1

        if(iavg<5 and sp>0 and sm>0 and at>0 and wt>0 and wt2>0 and wt3==0): #다시 5도 미만이 등장
            mth3=month
            dy3=day
            wt3+=1
        if(sp>0 and sm>0 and at>0 and wt>0 and wt2>0 and wt3>0):
            wt3+=1
            
        
f1.write(str(sm-2)+','+'\n'+'\n')
f1.write(str(yr1)+'-'+str(yr2)+" Autumm"+','+'\n')
f1.write("Start Date"+','+"Seasonal Length"+','+'\n')
f1.write(str(amth)+'-'+str(ady)+',')

if(wt2<wt):
    f1.write(str(at-2)+','+'\n'+'\n')
    f1.write(str(yr1)+'-'+str(yr2)+" Winter"+','+'\n')
    f1.write("Start Date"+','+"Seasonal Length"+','+'\n')
    f1.write(str(mth)+'-'+str(dy)+','+str(wt+wt2-2+wtimsi)+','+'\n'+'\n')
    print("f"+str(wt)+'  '+str(wt2)+'  '+str(wt3)+'  '+str(wtimsi))
elif(wt2>wt):
    f1.write(str(at-2+wt+wt2)+','+'\n'+'\n')
    f1.write(str(yr1)+'-'+str(yr2)+" Winter"+','+'\n')
    f1.write("Start Date"+','+"Seasonal Length"+','+'\n')
    f1.write(str(mth3)+'-'+str(dy3)+','+str(wt3+wtimsi-6)+','+'\n'+'\n')
    print("s"+str(wt)+'  '+str(wt2)+'  '+str(wt3)+'  '+str(wtimsi))
elif(wt2==wt):
    if(wt>=wt3):
        f1.write(str(at-2)+','+'\n'+'\n')
        f1.write(str(yr1)+'-'+str(yr2)+" Winter"+','+'\n')
        f1.write("Start Date"+','+"Seasonal Length"+','+'\n')
        f1.write(str(mth)+'-'+str(dy)+','+str(wt+wt2-2+wtimsi)+','+'\n'+'\n')
    else:
        f1.write(str(at-2+wt+wt2)+','+'\n'+'\n')
        f1.write(str(yr1)+'-'+str(yr2)+" Winter"+','+'\n')
        f1.write("Start Date"+','+"Seasonal Length"+','+'\n')
        f1.write(str(mth)+'-'+str(dy3)+','+str(wt3+wtimsi-6)+','+'\n'+'\n')

f1.close()
