import csv

with open("test.csv", newline='') as file:
    reader = csv.DictReader(file)
    sorted_rows = sorted(reader, key = lambda row: row['after'] )

with open("sorted.csv", 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(sorted_rows)
