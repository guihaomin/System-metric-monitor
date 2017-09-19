import os
import time
from subprocess import Popen, PIPE
class metric:
    def __init__(self,sample_duration,device):
        self.reads_per_sec=0
        self.writes_per_sec=0
        self.write_amount=0
        self.read_amount=0
        self.total_process=0
        self.sleeping_process=0
        self.running_process=0
        self.threads=0
        self.blocked_process=0
        self.sample_duration=sample_duration
        self.device=device
        self.deltas=[]
        self.cpu_times={}
        self.run_queue=0
        self.load_avgs=0
        self.disk_busy=0
        self.total_process=0
        self.blocked_process=0
        self.used_mem=0
        self.free_mem=0
        self.swap_total=0
        self.swap_in=0
        self.swap_out=0
        self.page_in=0
        self.page_out=0
    def mem_stats(self):
        with open('/proc/meminfo') as f:
            for line in f:
                if line.startswith('MemTotal:'):
                    mem_total = int(line.split()[1]) * 1024
                elif line.startswith('Active: '):
                    mem_active = int(line.split()[1]) * 1024
                elif line.startswith('MemFree:'):
                    mem_free = (int(line.split()[1]) * 1024)
                elif line.startswith('Cached:'):
                    mem_cached = (int(line.split()[1]) * 1024)
                elif line.startswith('SwapTotal: '):
                    swap_total = (int(line.split()[1]) * 1024)
                elif line.startswith('SwapFree: '):
                    swap_free = (int(line.split()[1]) * 1024)
        with open('/proc/vmstat') as f:
            for line in f:
                if line.startswith('pgpgin'):
                    self.page_in=int(line.split()[1])
                elif line.startswith('pgpgout'):
                    self.page_out=int(line.split()[1])
                elif line.startswith('pswpin'):
                    self.swap_in=int(line.split()[1])
                elif line.startswith('pswpout'):
                    self.swap_out=int(line.split()[1])
        self.used_mem=(mem_total-mem_free)/float(mem_total)
        self.free_mem=mem_free/mem_total
        self.swap_total=swap_total

    def disk_busy(self):
        with open('/proc/diskstats') as f1:
            with open('/proc/diskstats') as f2:
                content1 = f1.read()
                time.sleep(self.sample_duration)
                content2 = f2.read()
        sep = '%s ' % self.device
        found = False
        for line in content1.splitlines():
            if sep in line:
                found = True
                io_ms1 = line.strip().split(sep)[1].split()[9]
                break
        if not found:
            raise DiskError('device not found: %r' % device)
        for line in content2.splitlines():
            if sep in line:
                io_ms2 = line.strip().split(sep)[1].split()[9]
                break            
        delta = int(io_ms2) - int(io_ms1)
        total = sample_duration * 1000
        return 100 * (float(delta) / total)
    def cpu_percents(self):
    
        
        total = sum(self.deltas)
        percents = [100 - (100 * (float(total - x) / total)) for x in self.deltas]

        self.cpu_times={
            'user': percents[0],
            'nice': percents[1],
            'system': percents[2],
            'idle': percents[3],
            'iowait': percents[4],
            'irq': percents[5],
            'softirq': percents[6],
        }
    def disk_reads_writes_info(self):
        """Return number of disk (reads, writes) per sec during the sample_duration."""
        readSum1=self.readSum()
        writeSum1=self.writeSum()
        with open('/proc/diskstats') as f1:
            with open('/proc/diskstats') as f2:
                f3=open('/proc/stat')
                f4=open('/proc/stat')
                line1=f3.readline()
                content1 = f1.read()
                time.sleep(float(self.sample_duration))
                content2 = f2.read()
                
                line2=f4.readline()
                f3.close()
                f4.close()
        self.deltas = [int(b) - int(a) for a, b in zip(line1.split()[1:], line2.split()[1:])]
        readSum2=self.readSum()
        writeSum2=self.writeSum()
        sep = '%s ' % self.device
        found = False
        for line in content1.splitlines():
            if sep in line:
                found = True
                fields = line.strip().split(sep)[1].split()
                num_reads1 = int(fields[0])
                num_writes1 = int(fields[4])
                break
        if not found:
            raise DiskError('device not found: %r' % device)
        for line in content2.splitlines():
            if sep in line:
                fields = line.strip().split(sep)[1].split()
                num_reads2 = int(fields[0])
                num_writes2 = int(fields[4])
                break            
        reads_per_sec = (num_reads2 - num_reads1) / float(self.sample_duration)
        writes_per_sec = (num_writes2 - num_writes1) / float(self.sample_duration)
        self.reads_per_sec=reads_per_sec
        self.writes_per_sec=writes_per_sec
        self.read_amount=readSum2-readSum1
        self.write_amount=writeSum2-writeSum1
        sep = '%s ' % self.device
        found = False
        for line in content1.splitlines():
            if sep in line:
                found = True
                io_ms1 = line.strip().split(sep)[1].split()[9]
                break
        if not found:
            raise DiskError('device not found: %r' % device)
        for line in content2.splitlines():
            if sep in line:
                io_ms2 = line.strip().split(sep)[1].split()[9]
                break            
        delta = int(io_ms2) - int(io_ms1)
        total = int(self.sample_duration) * 1000
        self.disk_busy=100 * (float(delta) / total)
    def parseDirD(self):
        list=[]
        self.total_process=0
        files=os.listdir("/proc")
        for file in files:
            m=os.path.join("/proc",file)
            if(os.path.isdir(m) and file.isdigit()):
                list.append(os.path.join(m,"io"))
                self.total_process+=1
        return list
    def readSum(self):
        total=0
        pids=self.parseDirD()
        for process in pids:
            total+=int(self.__pid_stat("read_bytes:",process))/1000.0
        return total
    def writeSum(self):
        total=0
        pids=self.parseDirD()
        for process in pids:
            total+=float(self.__pid_stat("write_bytes:",process))/1000.0
        return total
    def __pid_stat(self,stat,dir="/proc/stat"):
        with open(dir) as f:
            for line in f:
                if line.startswith(stat):
                    return line.split()[1]
    def parseDir(self):
        list=[]
        self.total_process=0
        files=os.listdir("/proc")
        for file in files:
            m=os.path.join("/proc",file)
            if(os.path.isdir(m) and file.isdigit()):
                self.total_process+=1
                list.append(os.path.join(m,"status"))
        return list
    def procs_blocked(self):
        self.blocked_process=int(__proc_stat('procs_blocked'))
    def sleepingNum(self):
        count=0
        pids=self.parseDir()
        for process in pids:
            if self.__pid_stat("State:",process)=='S':
                count+=1
        self.sleeping_process=count
    def threadsNum(self):
        count=0
        pids=self.parseDir()
        for process in pids:
            count+=int(self.__pid_stat("Threads:",process))
        self.threads=count
    def run_queue_length(self):
        f=open("/proc/loadavg")
        set=f.readline().split()
        self.run_queue=int(set[3][0:set[3].find('/')])
    def load_avg(self):
        with open('/proc/loadavg') as f:
            line = f.readline()
    
        self.load_avgs = [float(x) for x in line.split()[:3]]

a=metric("5","sda")
a.disk_reads_writes_info()
#a.cpu_percents()
a.threadsNum()
a.sleepingNum()
a.run_queue_length()
a.load_avg()
print a.run_queue
print a.load_avgs
print a.disk_busy
print a.total_process
