# import win32evtlog
# from datetime import datetime, timedelta

# def read_failed_logins(time_window_minutes=10):
#     server = 'localhost'
#     logtype = 'Security'
#     handle = win32evtlog.OpenEventLog(server, logtype)

#     flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

#     now = datetime.now()
#     cutoff = now - timedelta(minutes=time_window_minutes)

#     events_data = []

#     while True:
#         events = win32evtlog.ReadEventLog(handle, flags, 0)
#         if not events:
#             break

#         for event in events:
#             if event.EventID == 4625:
#                 event_time = event.TimeGenerated
#                 if event_time < cutoff:
#                     return events_data

#                 data = event.StringInserts or []

#                 events_data.append({
#                     "time": event_time.Format(),
#                     "username": data[5] if len(data) > 5 else "N/A",
#                     "ip": data[19] if len(data) > 19 else "N/A",
#                     "logon_type": data[10] if len(data) > 10 else "N/A",
#                 })

#     return events_data

# def read_failed_logins(limit=50):
#     events = []

#     return events[:limit]

import win32evtlog
from datetime import datetime, timedelta

def read_failed_logins(limit=50, time_window_minutes=10):
    server = 'localhost'
    logtype = 'Security'
    handle = win32evtlog.OpenEventLog(server, logtype)

    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

    now = datetime.now()
    cutoff = now - timedelta(minutes=time_window_minutes)

    events_data = []

    while True:
        events = win32evtlog.ReadEventLog(handle, flags, 0)
        if not events:
            break

        for event in events:
            if event.EventID == 4625:
                event_time = event.TimeGenerated
                if event_time < cutoff:
                    return events_data[:limit]

                data = event.StringInserts or []

                events_data.append({
                    "time": event_time.Format(),
                    "username": data[5] if len(data) > 5 else "UNKNOWN",
                    "ip": data[19] if len(data) > 19 else "LOCAL",
                    "logon_type": data[8] if len(data) > 8 else "N/A",
                })

                if len(events_data) >= limit:
                    return events_data

    return events_data
