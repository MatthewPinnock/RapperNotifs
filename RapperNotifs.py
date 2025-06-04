#Rapper Notifs
import time
from win10toast_click import ToastNotifier

def on_click():
    print("Notification clicked")

t = ToastNotifier()

def showNoti():
    while True:
        t.show_toast(
            title="Earl",
            msg="State to state for the profit",
            icon_path=r"C:/Users/matth/Projects/RapperNotifs/images/Earl2.ico",
            duration=10,
            callback_on_click=on_click,
            threaded=False,
        )




if __name__ == '__main__':
    showNoti()
