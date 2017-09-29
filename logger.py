import logging
import sys
import time
import linux_metrics as lm
def assemble(name,value,unit,interval,isCumulative,transform,description="NIL"):
    return "%s %f %s %d %s %s %s" % (name,value,unit,interval,isCumulative,transform,description)
refresh_interval=1
interval=5
logger=logging.getLogger()
formatter=logging.Formatter('%(asctime)s %(message)s')
file_handler=logging.FileHandler("metric.log")
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
met=lm.integrated.metric(interval,'sda',"wlp2s0")
while True:
    print("sleeping...")
    time.sleep(refresh_interval)
    print("logging...")
    met.reset()
    system_CPU=assemble("system_cpu_usage",met.cpu_times["system"],"%",interval,"Yes","mean")
    logger.info(system_CPU)
    user_CPU=assemble("user_cpu_usage",met.cpu_times["user"],"%",interval,"Yes","mean")
    logger.info(user_CPU)
    load_avg=assemble("load_avg",met.load_avgs[1],"count",5,"no","mean")
    logger.info(load_avg)
    run_queue_length=assemble("run_queue_length",met.run_queue,"count",0,"No","-")
    logger.info(run_queue_length)
    total_process=assemble("total#process",met.total_process,"count",0,"No","-")
    logger.info(total_process)
    running_process=assemble("#running_process",met.running_process,"count",0,"No","-")
    logger.info(running_process)
    sleeping_process=assemble("#sleeping_process",met.sleeping_process,"count",0,"No","-")
    logger.info(sleeping_process)
    threads=assemble("#threads",met.threads,"count",0,"No","-")
    logger.info(threads)
    blocked_process=assemble("#blocked_process",met.blocked_process,"count",0,"No","-")
    logger.info(blocked_process)
    used_mem=assemble("used_physical_memory",met.used_mem,"%",0,"No","-")
    logger.info(used_mem)
    freed_mem=assemble("unused_physical_memory",met.free_mem,"%",0,"No","-")
    logger.info(freed_mem)
    swap_in=assemble("swap-in",met.swap_in,"count",interval,"Yes","total")
    logger.info(swap_in)
    swap_out=assemble("swap-out",met.swap_out,"count",interval,"Yes","total")
    logger.info(swap_out)
    page_in=assemble("page-in",met.page_in,"count",interval,"Yes","total")
    logger.info(page_in)
    page_out=assemble("page-out",met.page_out,"count",interval,"Yes","total")
    logger.info(page_out)
    swap_total=assemble("swap-allocated",met.swap_total,"",0,"No","-")
    logger.info(swap_total)
    disk_read=assemble("#physical_disk_read",met.reads_per_sec,"count",interval,"Yes","mean")
    logger.info(disk_read)
    disk_write=assemble("#physical_disk_write",met.writes_per_sec,"count",interval,"Yes","mean")
    logger.info(disk_write)
    amount_read=assemble("amount_physical_disk_read",met.read_amount,"bytes",interval,"Yes","mean")
    logger.info(amount_read)
    amount_write=assemble("amount_physical_disk_write",met.write_amount,"bytes",interval,"Yes","mean")
    logger.info(amount_write)
    disk_busy=assemble("disk_busy_time",met.disk_busy,"%",interval,"Yes","mean")
    logger.info(disk_busy)
    incoming_package=assemble("total#incoming_packages",met.recieve_packages,"count",interval,"Yes","mean")
    logger.info(incoming_package)
    outgoing_package=assemble("total#outgoing_packages",met.transmit_packages,"count",interval,"Yes","mean")
    logger.info(outgoing_package)
    recieve_bytes=assemble("size_of_incoming_packages",met.recieve_bytes,"bytes",interval,"Yes","mean")
    logger.info(recieve_bytes)
    transmit_bytes=assemble("size_of_outgoing_packages",met.transmit_bytes,"bytes",interval,"Yes","mean")
    logger.info(transmit_bytes)
    connections=assemble("#connections",met.connections,"count",0,"No","-")
    logger.info(connections)
