f=open('daysort.txt','r')
f0=open('30_avg_2021-2040.txt','w')
f1=open('30_avg_2041-2070.txt','w')
f2=open('30_avg_2071-2100.txt','w')
"""
f3=open('10_avg_2031-2040.txt','w')
f4=open('10_avg_2041-2050.txt','w')
f5=open('10_avg_2051-2060.txt','w')
f6=open('10_avg_2061-2070.txt','w')
f7=open('10_avg_2071-2080.txt','w')
f8=open('10_avg_2081-2090.txt','w')
f9=open('10_avg_2091-2100.txt','w')
"""
fjun=open('30_avg_total.txt','w')

tavg0=0
tavg1=0
tavg2=0
tavg3=0
tavg4=0
tavg5=0
tavg6=0
tavg7=0
tavg8=0
tavg9=0
tcnt0=0
tcnt1=0
tcnt2=0
tcnt3=0
tcnt4=0
tcnt5=0
tcnt6=0
tcnt7=0
tcnt8=0
tcnt9=0

for line in f:
    data=line.split('\t')
    year=data[0]
    month=data[1]
    day=data[2]
    tavg=float(data[3])

    if(int(year) in range(2021,2041)):
        tavg0=tavg0+tavg
        tcnt0+=1
        if(tcnt0==20):
            f0.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg0/tcnt0,1))+'\t'+'\n')
            fjun.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg0/tcnt0,1))+'\t'+'\n')
            tcnt0=0
            tavg0=0
            
            """
    if(int(year) in range(2041,2071)):
        tavg1=tavg1+tavg
        tcnt1+=1
        if(tcnt1==30):
            f1.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg1/tcnt1,1))+'\t'+'\n')
            fjun.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg1/tcnt1,1))+'\t'+'\n')
            tcnt1=0
            tavg1=0
    if(int(year) in range(2071,2101)):
        tavg2=tavg2+tavg
        tcnt2+=1
        if(tcnt2==30):
            f2.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg2/tcnt2,1))+'\t'+'\n')
            fjun.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg2/tcnt2,1))+'\t'+'\n')
            tcnt2=0
            tavg2=0
            
    if(int(year) in range(2031,2041)):
        tavg3=tavg3+tavg
        tcnt3+=1
        if(tcnt3==10):
            f3.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg3/tcnt3,1))+'\t'+'\n')
            fjun.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg3/tcnt3,1))+'\t'+'\n')
            tcnt3=0
            tavg3=0
    if(int(year) in range(2041,2051)):
        tavg4=tavg4+tavg
        tcnt4+=1
        if(tcnt4==10):
            f4.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg4/tcnt4,1))+'\t'+'\n')
            fjun.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg4/tcnt4,1))+'\t'+'\n')
            tcnt4=0
            tavg4=0
    if(int(year) in range(2051,2061)):
        tavg5=tavg5+tavg
        tcnt5+=1
        if(tcnt5==10):
            f5.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg5/tcnt5,1))+'\t'+'\n')
            fjun.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg5/tcnt5,1))+'\t'+'\n')
            tcnt5=0
            tavg5=0
    if(int(year) in range(2061,2071)):
        tavg6=tavg6+tavg
        tcnt6+=1
        if(tcnt6==10):
            f6.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg6/tcnt6,1))+'\t'+'\n')
            fjun.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg6/tcnt6,1))+'\t'+'\n')
            tcnt6=0
            tavg6=0
    if(int(year) in range(2071,2081)):
        tavg7=tavg7+tavg
        tcnt7+=1
        if(tcnt7==10):
            f7.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg7/tcnt7,1))+'\t'+'\n')
            fjun.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg7/tcnt7,1))+'\t'+'\n')
            tcnt7=0
            tavg7=0
    if(int(year) in range(2081,2091)):
        tavg8=tavg8+tavg
        tcnt8+=1
        if(tcnt8==10):
            f8.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg8/tcnt8,1))+'\t'+'\n')
            fjun.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg8/tcnt8,1))+'\t'+'\n')
            tcnt8=0
            tavg8=0
    if(int(year) in range(2091,2101)):
        tavg9=tavg9+tavg
        tcnt9+=1
        if(tcnt9==10):
            f9.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg9/tcnt9,1))+'\t'+'\n')
            fjun.write(year+'\t'+month+'\t'+day+'\t'+str(round(tavg9/tcnt9,1))+'\t'+'\n')
            tcnt9=0
            tavg9=0
            """

f0.close()
"""
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()
"""
fjun.close()

