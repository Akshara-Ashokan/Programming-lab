import calendar
year=int(input(&quot;Enter the year:&quot;))
leap_year=calendar.isleap(year)
if leap_year:
    print(&quot;The given year is a leap year&quot;)
else:
    print(&quot;The given year is a non leap year&quot;)
