import csv
def read_records(file_name):
    records = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            records.append(row)
    return records


def create_record(file_name, record):
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(record)


data = read_records('data.csv')
for record in data:
    print(record)

data_to_insert = ['John', 'Doe', 'john.doe@example.com']
create_record('data.csv', data_to_insert)
