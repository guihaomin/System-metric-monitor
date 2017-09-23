import logging
import sys
import linux_metrics as lm
def assemble(name,value,unit,interval,isCumulative,transform,description="NIL"):
    return "%s %f %s %d %s %s %s" % (name,value,unit,interval,isCumulative,transform,description)
    
logger=logging.getLogger()
formatter=logging.Formatter('%(asctime)s %(message)s')
file_handler=logging.FileHandler("metric.log")
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
met=lm.integrated.metric(1,'sda')
met.reset()
system_CPU=assemble("system_cpu_usage",met.cpu_times["system"],"%",1,"Yes","mean")
logger.info(system_CPU)
user_CPU=assemble("user_cpu_usage",met.cpu_times["user"],"%",1,"Yes","mean")
logger.info(user_CPU)
load_avg=assemble("load_avg",met.load_avgs[1],"count",5,"no","mean")

