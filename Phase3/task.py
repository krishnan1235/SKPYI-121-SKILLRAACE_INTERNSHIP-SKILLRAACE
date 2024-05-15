import time
def countdown_timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t-=1
    print("Time's up!")
ti= int(input("Enter a time to set(in seconds):"))
countdown_timer(ti)
