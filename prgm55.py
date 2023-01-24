file = open(&quot;f1.txt&quot;,&quot;r&quot;)
lines=[]
for line in file:
lines.append(line)
print(lines)
file.close()
