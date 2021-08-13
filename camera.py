import os
import datetime

date = datetime.datetime.now()
file = str(date).replace(" ", "--").replace(":", "-")[:-7]

cmd = 'raspistill -o %s.jpg' % file

os.system(cmd)
