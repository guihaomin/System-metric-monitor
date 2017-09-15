import linux_metrics as lm
import time
sample_duration=1
def stdPrint():
    f=open("data.txt","w")
    f.write(time.asctime( time.localtime(time.time()) )+"\n")
    writeCPU(f)
    f.close()

def writeCPU(f):
    
    f.write("System_CPU_Usage ")
    cpu_stat = lm.cpu_stat.cpu_percents(sample_duration)
    sysUtil=cpu_stat['system']
    f.write(str(sysUtil)+" ")
    f.write("% ")
    f.write("cgoldberg ")
    f.write(str(sample_duration))
    f.write("\nUser_CPU_Usage ")
    userUtil=cpu_stat['user']
    f.write(str(userUtil)+" ")
    f.write("% ")
    f.write("cgoldberg ")
    f.write(str(sample_duration))
    f.write("\nLoad_Avg ")
    f2=open("/proc/loadavg")
    set=f2.readline().split()
    f2.close()
    f.write(set[1]+" ")
    f.write("cnt ")
    f.write("build_in ")
    f.write("5min")
    f.write("\nRun_Queue_Length ")
    f.write(set[3][0:set[3].find('/')]+" ")
    f.write("cnt ")
    f.write("build_in ")
    f.write("5min")
stdPrint()
    
    
    
