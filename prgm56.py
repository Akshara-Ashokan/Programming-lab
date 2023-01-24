fn = open(&quot;files.txt&quot;,&quot;r&quot;)
fn1 = open(&quot;files2.txt&quot;,&quot;w&quot;)
cont = fn.readlines()
type(cont)
for i in range(0,len(cont)):
    if(i%2=0):
        fn1.write(cont [i])
else:
pass
fn1.close()
fn1=open(‘files2.txt’, ‘r’)



cont1=fn1.read()
fn.close()
fn1.close()

