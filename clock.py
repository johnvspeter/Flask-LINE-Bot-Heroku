from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', minute='*/1')
def scheduled_job():
    url = " https://chichunbot.herokuapp.com/"
    conn = urllib.request.urlopen(url)
        
    for key, value in conn.getheaders():
        print(key, value)

sched.start()