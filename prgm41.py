terms=10
result=list(map(lambda x:2**x,range(terms)))
print(&quot;The total terms are&quot;,terms)
for i in range(terms):
    print(&quot;2 ^&quot;,i,&quot;is&quot;,result[i])
