class time:
     __hour=0
     __min=0
     __sec=0
     def __init__(self,hr,minute,sec):
         self.__hour=hr
         self.__min=minute
         self.__sec=sec
     def gethour(self):
         return self.__hour
     def getmin(self):
         return self.__min
     def getsec(self):
         return self.__sec
     def __add__(self,t):
         self.__hour=self.__hour+t.gethour()
         self.__min=self.__min+t.getmin()
         self.__sec=self.__sec+t.getsec()
         print(&quot;HH:MM:SS={}:{}:{}&quot;.format(self.__hour,self.__min,self.__sec))
def main():
    print(&quot;Enter a time(hh:mm:ss)&quot;)
    hr=int(input(&quot;Hour:&quot;))
    minute=int(input(&quot;Minute:&quot;))
    sec=int(input(&quot;Seconds:&quot;))
    obj1=time(hr,minute,sec)
    print(&quot;Enter a diferent time(hh:mm:ss)&quot;)
    hr=int(input(&quot;Hour:&quot;))
    minute=int(input(&quot;Minute:&quot;))
    sec=int(input(&quot;Seconds:&quot;))

    obj2=time(hr,minute,sec)
    print(obj1+obj2)
main()
