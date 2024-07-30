import csv

newlist = set()
with open ('dataset/sorted.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        newlist.add(row['before'])
        newlist.add(row['after'])

ordered = sorted(newlist)

with open ('namelist.txt', 'w') as f:
    for i in ordered:
        f.write(i)
        f.write('\n')
