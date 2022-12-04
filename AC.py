import random
from RWfile import RWfile

data = RWfile('database.csv').read()
randomrange = random.randrange(0, len(data))


class AC:

    def __init__(self, name='', temp='', mode='',
                 fan=['0', 'OFF'], status='close'):
        self.name = name
        self.temp = temp
        self.mode = mode
        self.fan = fan
        self.status = status

    def open_close(self, oc):
        if oc == 'open':
            self.status = oc
        if oc == 'close':
            self.status = oc
            self.temp = ''
            self.mode = ''
            self.fan[0] = '0'
            self.fan[1] = ''

    def swing(self, swing):
        if swing == 'ON' or swing == 'OFF':
            self.fan[1] = swing

    def speed(self, speed):
        if 1 <= speed <= 5:
            self.fan[0] = str(speed)
        else:
            print('speed must be greater than 0 and less than 6.')

    def mode(self, index):
        ac_mode = ['auto', 'cool', 'eco', 'heat', 'fan']
        self.mode = ac_mode[index - 1]

    def temperature(self, temper):
        if self.status == 'open' and self.temp != 'auto':
            if 15 <= temper <= 30:
                self.temp = str(temper)
            else:
                print('temperature must be greater than 14 and less than 31.')

    def auto(self):
        if self.status == 'open' and self.mode == 'auto':
            if data[randomrange]['season'] == 'summer':
                if 28 <= int(data[randomrange]['temp']) <= 32:
                    self.temp = '22'
                if int(data[randomrange]['temp']) > 32:
                    self.temp = '20'
            if data[randomrange]['season'] == 'rainy':
                if 20 <= int(data[randomrange]['temp']) <= 24:
                    self.temp = '26'
                if int(data[randomrange]['temp']) > 24:
                    self.temp = '24'
            if data[randomrange]['season'] == 'winter':
                if 15 <= int(data[randomrange]['temp']) <= 23:
                    self.temp = '27'
                if int(data[randomrange]['temp']) > 23:
                    self.temp = '26'

    def __str__(self):
        return f'{self.name}-Status:{self.status} Temperature:{self.temp}C ' \
               f'Mode:{self.mode} Speed:{self.fan[0]} Swing:{self.fan[1]}'