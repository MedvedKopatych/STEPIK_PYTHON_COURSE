import csv
import collections
crimes = []
c = collections.Counter
with open("Crimes.csv", "r") as f:
    reader = csv.DictReader(f)
    for rows in reader:
        crime = rows['Primary Type']
        crimes.append(crime)
most_often = c(crimes).most_common(1)
print(most_often)



