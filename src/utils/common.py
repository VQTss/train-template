from datetime import datetime


def get_now_string():
    time_now = datetime.now()
    return time_now.strftime("%Y%m%d_%H%M%S")