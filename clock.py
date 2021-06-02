from flask import app
from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request

sched = BlockingScheduler()

## 利用clock.py 每二十分鐘call回自己app的url來叫醒app
@sched.scheduled_job('cron', day_of_week='mon-thu', minute='*/20')
def scheduled_job():
    url = " https://chichunbot.herokuapp.com/"
    conn = urllib.request.urlopen(url)
        
    for key, value in conn.getheaders():
        print(key, value)

## 利用clock.py 每天傳送打卡訊息
@sched.scheduled_job('cron', day_of_week='mon-thu', hour='7,17',minute='15')
def scheduled_job2():
    url = " https://chichunbot.herokuapp.com/card"
    conn = urllib.request.urlopen(url)
        
    for key, value in conn.getheaders():
        print(key, value)

sched.start()