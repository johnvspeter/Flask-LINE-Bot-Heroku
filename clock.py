from flask import app
from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request

sched = BlockingScheduler()


##@sched.scheduled_job('cron', day_of_week='mon-thu', hour='7,17',minute='15')
@sched.scheduled_job('cron', day_of_week='mon-thu',minute='*/3')
def scheduled_job():
    url = " https://chichunbot.herokuapp.com/card"
    conn = urllib.request.urlopen(url)
        
    for key, value in conn.getheaders():
        print(key, value)

## 利用clock.py call回自己app的url來叫醒app
@sched.scheduled_job('cron', day_of_week='mon-thu',minute='*/1')
def scheduled_job2():
    url2 = " https://chichunbot.herokuapp.com/"
    conn2 = urllib.request.urlopen(url2)
        
    for key, value in conn2.getheaders():
        print(key, value)

sched.start()