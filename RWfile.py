import csv


class RWfile:
    def __init__(self, filename: str):
        '''create filename value'''
        self.filename = filename

    def read(self):
        '''read a file'''
        try:
            with open(self.filename, 'r') as file:
                dict_read = csv.DictReader(file)
                data_list = [data for data in dict_read]
        except FileNotFoundError:
            print(f'{self.filename} file is not found')
        return data_list

    def write(self):
        '''write a file'''
        while True:
            season = input('Enter season in your area: ')
            temp = input('Enter temperature in your area: ')
            if season in ['winter', 'summer', 'rainy'] \
                    and temp in ['15', '16', '17', '18', '19',
                                 '20', '21', '22', '23', '24',
                                 '25', '26', '27', '28', '29',
                                 '30', '31', '32']:
                key = ['season', 'temp']
                try:
                    with open(self.filename, 'a') as file:
                        dict_write = csv.DictWriter(file, key)
                        dict_write.writerow({'season': season, 'temp': temp})
                        break
                except FileNotFoundError:
                    print(f'{self.filename} file is not found')
            else:
                print('Season must be a english character and '
                      'temp must be a number in range 15-32')
