import csv
import json
import random
import sys
import namesLib


def generate():
    lines_to_generate = int(input("How many advocates to generate? Should be integer, after 3200 street name will be duplicated with different number :"))

    if lines_to_generate <= 0:
        sys.exit('Exiting. Correct positive integer is expected')

    source_filename = "addresses.json"
    filename = "/output/randomAddresses.csv"
    fields = ['streetNumber', 'streetName', 'zipcode', 'state', 'name', 'email', 'phone']

    rows_data = []

    with open(source_filename) as f:
        data_source = json.load(f)

    source_size = len(data_source['addresses'])

    for i in range(lines_to_generate):
        address_pointer = i

        if i >= source_size:
            address_pointer = i - source_size

        address_split = data_source['addresses'][address_pointer]['address1'].split(' ', 1)

        if lines_to_generate > source_size:
            address_split[0] = random.randint(50, 9999)

        email_name = random_name_email_generator()
        rows_data.append([address_split[0], address_split[1], data_source['addresses'][address_pointer]['postalCode'], data_source['addresses'][address_pointer]['state'], email_name[0], email_name[1], random_phone_num_generator()])

    with open(filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(fields)
        csv_writer.writerows(rows_data)

    return


def random_phone_num_generator():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return first+second+last


def random_name_email_generator():
    f_name = random.choice(namesLib.names)
    l_name = random.choice(namesLib.names)

    email = f_name[:4].lower() + '_' + l_name[:5].lower() + str(random.randint(0, 99)) + '@' + random.choice(namesLib.domains)
    return [f_name + ' ' + l_name, email]


generate()


