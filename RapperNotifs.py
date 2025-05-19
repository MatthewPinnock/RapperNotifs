#Rapper Notifs
import time
from plyer import notification as noti # type: ignore

def showNoti(title, message):
    noti.notify(
        title=title,
        message=message,
        timeout=10,
        app_icon='C:/Users/matth/Projects/RapperNotifs/images/Earl.ico',
    )

if __name__ == '__main__':
    showNoti("Earl", """State to state for the profit""")