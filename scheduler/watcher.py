import scheduler.schedule_process as schedule_process

def hallo():
    print("I'm working")

def start_watching():
    schedule_process.start(hallo)
