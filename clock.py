from flask import app
from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request

sched = BlockingScheduler()

## 利用clock.py call回自己app的url來叫醒app
@sched.scheduled_job('cron', day_of_week='mon-thu', hour='7,17',minute='15')
def scheduled_job():
    url = " https://chichunbot.herokuapp.com/"
    conn = urllib.request.urlopen(url)
        
    for key, value in conn.getheaders():
        print(key, value)
def job_task(): 
    url2 = " https://chichunbot.herokuapp.com/card"
    conn2 = urllib.request.urlopen(url2)
        
    for key, value in conn2.getheaders():
        print(key, value)

sched.add_job(job_task, 'interval', minute=1)


sched.start()