import collections
from datetime import datetime


def main():
    processed_data = collections.OrderedDict()

    with open('data/DischargeCypressCreek.csv') as data_file:
        for line in data_file:
            line = line.strip()
            if len(line) == 0:
                continue

            split_line = line.split(',')
            if len(split_line) <= 1 or split_line[2] == 'datetime':
                continue

            date = datetime.strptime(split_line[2].split(" ")[0], "%m/%d/%y")
            if date in processed_data:
                processed_data[date].append(float(split_line[4]))
            else:
                processed_data[date] = [float(split_line[4])]

    for date, list_discharge in processed_data.items():
        average_discharge = sum(list_discharge) / float(len(list_discharge))
        print("{},{}".format(date.strftime("%m/%d/%y"), average_discharge))


if __name__ == '__main__':
    main()
