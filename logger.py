import logging
import sys
from . import integrated
def assemble(name,value,unit,interval,isCumulative,Transform,Desception="NIL"):
    return "%s %f %s %d %s %s %s"
    
logger=logging.getLogger()
formatter=logging.Formatter('%(asctime)s %(message)s')
file_handler=logging.FileHandler("metric.log")
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
met=metric(1,'sda')
met.reset()
logger.info(str(met.free_mem))
