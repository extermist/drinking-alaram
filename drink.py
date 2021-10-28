from win10toast import ToastNotifier
import datetime
  
  
def getTimeInput():
    hour = int(input("hours of interval :"))
    minutes = int(input("Mins of interval :"))
    seconds = int(input("Secs of interval :"))
    time_interval = seconds+(minutes*60)+(hour*3600)
    return time_interval
  
  
def log():
    now = datetime.datetime.now()
    start_time = now.strftime("%H:%M:%S")
    with open("log.txt", 'a') as f:
       
    return 0
