

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import urllib.request
# 输出时间
def job():
    url = " https://chichunbot.herokuapp.com/"
    conn = urllib.request.urlopen(url)
        
    for key, value in conn.getheaders():
        print(key, value)

def job2():
    url2 = " https://chichunbot.herokuapp.com/card"
    conn2 = urllib.request.urlopen(url2)
        
    for key, value in conn2.getheaders():
        print(key, value)
# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', day_of_week='1-5',minute=1)
scheduler.add_job(job2, 'cron', day_of_week='1-5',minute=1)

scheduler.start()