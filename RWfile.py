import csv


class RWfile:
    def __init__(self, filename=''):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename, 'r') as file:
                dict_read = csv.DictReader(file)
                data_list = [data for data in dict_read]
        except FileNotFoundError:
            print(f'{self.filename} file is not found')
        return data_list

    def write(self):
        season = input('Enter season in your area: ')
        temp = input('Enter temperature in your area: ')
        key = ['season', 'temp']
        try:
            with open(self.filename, 'a') as file:
                dict_write = csv.DictWriter(file, key)
                dict_write.writerow({'season': season, 'temp': temp})
        except FileNotFoundError:
            print(f'{self.filename} file is not found')
