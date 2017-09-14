import os
import time
proc=open("/proc/stat","r")
a=proc.readlines()
proc.close()
i=0
cpuSum=[]
total=[]
cpuSum2=[]
total2=[]
parse=a[i].split(' ')
while(parse[0]!='intr'):
   parse=a[i].split()
   cpuSum.append(int(parse[1])+int(parse[2])+int(parse[3])+int(parse[5])+int(parse[6])+int(parse[7])+int(parse[8])+int(parse[9]))
   
   total.append(int(parse[4])+cpuSum[i])
   i+=1
i=0
time.sleep(5)
proc=open("/proc/stat","r")
a=proc.readlines()
proc.close()
parse=a[0].split(' ')
while(parse[0]!='intr'):
   parse=a[i].split()
   cpuSum2.append(int(parse[1])+int(parse[2])+int(parse[3])+int(parse[5])+int(parse[6])+int(parse[7])+int(parse[8])+int(parse[9]))
   total2.append(int(parse[4])+cpuSum2[i])
   i+=1
for t in range(i-1):
   print(100.0*(cpuSum2[t]-cpuSum[t])/(total2[t]-total[t]))
