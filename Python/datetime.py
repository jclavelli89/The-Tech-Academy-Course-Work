import time
import datetime
from datetime import timedelta, tzinfo, datetime, date  
import pytz
from pytz import timezone

now_portland = datetime.now(timezone('America/Los_Angeles'))

def london_branch():
    if now_portland.hour < 1:
        print("London Branch is closed")
    elif now_portland.hour > 13:
        print("London Branch is closed")
    else:
        print("London Branch is open")

def nyc_branch():
    if now_portland.hour < 6:
        print("NYC Branch is closed")
    elif now_portland.hour > 18:
        print("NYC Branch is closed")
    else:
        print("NYC Branch is open")

london_branch()
nyc_branch()
