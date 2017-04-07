import csv


number_of_rows = 10000


with open('test.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',')
    csv_writer.writerow(['id', 'value', 'thing'])
    for row in range(number_of_rows):
   		csv_writer.writerow([row, 'Lovely Spam', 'Wonderful Spam'])