    from datetime import datetime
from plyer import notification
import time

while True:
    current = datetime.now()
    min=current.minute
    sec=current.second
    #exercise every hour
    if min==0 and sec<20:
        notification.notify(
            title="Exercise and juggle Now!!",
            message="You have frequent back pain--> so exercise.\nJuggling is good for the brain--> so juggle.",
            timeout=10,
            app_icon=r"E:\pythonCourse\code\notification_app\icon1.ico"
        )
        notification.notify(
            title="Drink Water Now!!",
            message="Unless you want to die of dehydration",
            timeout=10,
            app_icon=r"E:\pythonCourse\code\notification_app\water.ico"
        )

    #drink water every 30 mins
    if min==30 and sec<20:
        notification.notify(
            title="Drink Water Now!!",
            message="Unless you want to die of dehydration",
            timeout=10,
            app_icon=r"E:\pythonCourse\code\notification_app\water.ico"
        )

    time.sleep(20)
