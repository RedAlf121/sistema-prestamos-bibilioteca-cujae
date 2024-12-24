from scheduler import TIME_DEFAULT,LOG_PATH,LOG_FORMAT
import schedule
from datetime import datetime
import pickle
import time

def start(job):
    if not is_notified():
        if not is_later_default():
            job_wrapper(job)
        test_schedule(lambda:job_wrapper(job))
        while True:
            schedule.run_pending()
            time.sleep(1)

def schedule_process(job):
    schedule.every().days.at(TIME_DEFAULT).do(job)

def test_schedule(job):
    schedule.every().minutes.do(job)

def is_later_default():
    format = '%H:%M'
    now = datetime.now().strftime(format)
    time_now = datetime.now().strptime(now,format)
    default = datetime.now().strptime(TIME_DEFAULT,format)
    return time_now>default

def job_wrapper(job):
    now = datetime.now().strftime(LOG_FORMAT)
    job()
    
    with open(LOG_PATH,'wb') as f:
        pickle.dump(now,f)

def is_notified():
    try:
        with open(LOG_PATH,'rb') as f:
            date = pickle.load(f)
            now = datetime.now().strftime(LOG_FORMAT)
        return date==now
    except EOFError:
        return False 


