import csv
with open(&#39;t3.csv&#39;, &#39;r&#39;) as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
