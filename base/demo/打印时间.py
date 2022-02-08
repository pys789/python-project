import time,datetime

for i in range(3):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    time.sleep(1)

print(datetime.date.today().strftime('%Y-%m-%d'))
