import csv
with open(‘names.csv&#39;, &#39;r&#39;) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row[‘first_name’], row[‘job’])
