import csv
from datetime import datetime
from main.models import Database
import pytz

tz = pytz.timezone('Asia/Singapore')

with open('positions.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        # 2018-11-23 06:36:13:112583
        #tz.localize(d, is_dst=None)
        tm = tz.localize(datetime.strptime(list(row.values())[0], '%Y-%m-%d %H:%M:%S:%f'), is_dst=None)
        account = list(row.values())[1]
        symbol = list(row.values())[2]
        position = list(row.values())[3]

        new_db = Database(tm=tm, account=account, symbol=symbol, position=position)
        new_db.save()
