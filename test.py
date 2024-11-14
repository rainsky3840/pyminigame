import random, csv

with open('data.csv', 'r', encoding='utf-8') as file:
  csv_reader = csv.DictReader(file)
  # next(csv_reader) #skip first row
  for row in csv_reader:
    print(row['수감자'], row['소속'], row['분류'], row['점수'])
    # print(row)