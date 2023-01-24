import armstrong
l=int(input(&quot;Enter the lower limit:&quot;))
u=int(input(&quot;Enter the upper limit:&quot;))
ls=[i for i in range(l,u) if armstrong.armstrong(i)]
print(&quot;Armstrong number between {}-{}:&quot;.format(l,u),ls)
armstrong.py
def armstrong(i):
     l=len(str(i))
     arm=sum(map(lambda i:int(i)**l,str(i)))
     return i==arm
