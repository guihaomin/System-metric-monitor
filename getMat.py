import linux_metrics as lm
import time
sample_duration=1
def stdPrint():
    f=open("data.txt","w")
    f.write(time.asctime( time.localtime(time.time()) )+"\n")
    f.write("metric Unit Tool/Source Monitoring_Interval(sec) is_Cumulative Priority Transformation Desception\n")
    writeCPU(f)
    writeProcess(f)
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
    f.write("300")
    f.write("\nRun_Queue_Length ")
    f.write(set[3][0:set[3].find('/')]+" ")
    f.write("cnt ")
    f.write("build_in ")
    f.write("NIL")
def writeProcess(f):
    f.write("\nTotal#Process ")     # it is the number of process since boot
    f.write(str(lm.cpu_stat.procs_all())+" ")
    f.write("cnt ")
    f.write("add ")
    f.write("NIL")
    f.write("\nRuning#Process ")
    f.write(str(lm.cpu_stat.procs_running())+" ")
    f.write("cnt ")
    f.write("cgoldberg ")
    f.write("NIL")
    f.write("\nSleeping#Process ")
    f.write(str(lm.cpu_stat.sleepingNum())+" ")
    f.write("cnt ")
    f.write("add ")
    f.write("NIL")
    f.write("\n#Threads ")
    f.write(str(lm.cpu_stat.threadsNum())+" ")
    f.write("cnt ")
    f.write("add ")
    f.write("NIL")
    f.write("\nBlocked#Process ")
    f.write(str(lm.cpu_stat.procs_blocked())+" ")
    f.write("cnt ")
    f.write("cgoldberg ")
    f.write("NIL")
stdPrint()
    
    
    
