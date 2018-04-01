import collections
from datetime import datetime


def process_precipitation_data():
    dates = set()

    with open('data/original/DailyPrecip.csv') as data_file:
        for line in data_file:
            line = line.strip()
            if len(line) == 0:
                continue

            split_line = line.split(',')
            if len(split_line) <= 1 or split_line[0] == 'ï»¿Da0e':
                continue

            date = datetime.strptime(split_line[0], "%m/%d/%y").strftime("%m/%d/%y")
            dates.add(date)

            precipitation = 0.0
            try:
                precipitation = float(split_line[1])
            except Exception:
                pass

            print("{},{}".format(date, precipitation))

    return dates


def process_discharge_data():
    dates = set()
    processed_data = collections.OrderedDict()

    with open('data/original/DischargeCypressCreek.csv') as data_file:
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
        dates.add(date.strftime("%m/%d/%y"))

    return dates


if __name__ == '__main__':
    dates1 = process_discharge_data()
    dates2 = process_precipitation_data()

    print(dates2 - dates1)
