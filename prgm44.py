import time
import datetime
print(&quot;current date and time:&quot;,datetime.datetime.now())
print(&quot;current year:&quot;,datetime.date.today().strftime(&quot;%Y&quot;))

print(&quot;month of year:&quot;,datetime.date.today().strftime(&quot;%B&quot;))
print(&quot;week number of the year&quot;,datetime.date.today().strftime(&quot;%W&quot;))
print(&quot;wednesday of the week:&quot;,datetime.date.today().strftime(&quot;%w&quot;))
print(&quot;day of year:&quot;,datetime.date.today().strftime(&quot;%j&quot;))
print(&quot;day of the month:&quot;,datetime.date.today().strftime(&quot;%d&quot;))
print(&quot;day of week&quot;,datetime.date.today().strftime(&quot;%A&quot;))
