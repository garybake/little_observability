from datetime import datetime

def unix_to_datetime_string(ts):
    ts = int(ts)
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
