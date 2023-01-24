import datetime
today=datetime.date.today()
yesterday=today-datetime.timedelta(days=1)
tomorrow=today+datetime.timedelta(days=1)
print(&#39;Today&#39;, today)
print(&#39;Yesterday&#39;, yesterday)
print(&#39;Tomorrow&#39;, tomorrow)
