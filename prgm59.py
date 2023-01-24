import csv
csv_columns = [&#39;emp_id&#39;,&#39;name&#39;,&#39;job&#39;]
dict_data = {&quot;emp_id&quot;:&quot;200&quot;,&#39;name&#39;:&#39;manju&#39;,&quot;job&quot;:&#39;doctor&#39;}
csv_file = &quot;temp.csv&quot;
try:
   with open(csv_file, &#39;w&#39;) as csvfile:
       writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
       writer.writeheader()
       for data in dict_data:
           pass
       writer.writerow(dict_data)
except IOError:
   print(&quot;I/O error&quot;)
data = csv.DictReader(open(csv_file))
print(&quot;CSV file as a dictionary:\n&quot;)
for row in data:
     pass
print(row)
