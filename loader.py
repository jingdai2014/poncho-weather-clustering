__author__ = 'daijing'
import csv
import logging
from collections import defaultdict

logging.basicConfig(filename='loader.log', level = logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class Weather(object):
    def __init__(self):
        self.info = {}
        self.wid = None

def load_info(filename, rows):
    header = True
    headers = {}
    check_len = None
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if header:
                for i, key in enumerate(row):
                    headers[i] = key
                header= False
                check_len = len(row)
            elif check_len == len(row):
                id = int(row[0])
                rows[id].wid = id
                for i, value in enumerate(row):
                    code = headers[i]
                    rows[id].info[code] = value
            else:
                logging.exception("length check failed: " + str(row))
    logging.info("number of rows: " + str(len(rows)))


def load_weather(filename):
    rows = defaultdict(Weather)
    load_info(filename, rows)
    return rows

if __name__ == '__main__':
    file = 'NY_State_Historical_Weather_Clusters.csv'
    rows = load_weather(file)
    print rows[7052].info, rows[7052].wid



