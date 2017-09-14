import os
import time
proc=open("/proc/stat","r")
mem=open("/proc/meminfo","r")
memInfo=mem.readlines()
a=proc.readlines()
proc.close()
mem.close()
i=0
swapTotal=0
swapFree=0
memTotal=0
memFree=0
cpuSum=[]
total=[]
cpuSum2=[]
total2=[]
parse=a[i].split()
for p in range(len(memInfo)):
   procM=memInfo[p].split()
   if procM[0]=="MemTotal:":
      memTotal+=int(procM[1])
   if procM[0]=="MemFree:":
      memFree+=int(procM[1])
   if procM[0]=="SwapTotal:":
      swapTotal+=int(procM[1])
   if procM[0]=="SwapFree:":
      swapFree+=int(procM[1])
while(parse[0]!='intr'): #get initial info
   parse=a[i].split()
   cpuSum.append(int(parse[1])+int(parse[2])+int(parse[3])+int(parse[5])+int(parse[6])+int(parse[7])+int(parse[8])+int(parse[9]))
   
   total.append(int(parse[4])+cpuSum[i])
   i+=1
i=0
time.sleep(5)
proc=open("/proc/stat","r")
a=proc.readlines()
proc.close()
parse=a[0].split()
while(parse[0]!='intr'): #get info after 5s to compute change
   parse=a[i].split()
   cpuSum2.append(int(parse[1])+int(parse[2])+int(parse[3])+int(parse[5])+int(parse[6])+int(parse[7])+int(parse[8])+int(parse[9]))
   total2.append(int(parse[4])+cpuSum2[i])
   i+=1
print("Number of cores is %d" % (i-2))
print("first is overall usage then usage of core")
for t in range(i-1):#first is overall usage then usage of cores
   print(100.0*(cpuSum2[t]-cpuSum[t])/(total2[t]-total[t]))
print("Memory usage: %f" % (100.0*(memTotal-memFree)/memTotal))
if swapFree!=swapTotal:
   print("Swapfile usage: %f" % (100.0*(swapTotal-swapFree)/swapTotal))
