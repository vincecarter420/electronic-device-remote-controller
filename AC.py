import random
from RWfile import RWfile

data = RWfile('database.csv').read()  # read a data from database.csv file
randomrange = random.randrange(0, len(data))  # random a situation from data


class AC:

    def __init__(self, name:str, temp:str, mode:str, fan:list,
                 status:str):
        '''create name, temperature, mode, fan, and status values'''
        self.__name = name
        self.temp = temp
        self.mode = mode
        self.fan = fan
        self.status = status

    @property
    def name(self):
        '''getter'''
        return self.__name

    def open_close(self, oc):
        '''this function is for opening and closing the AC
            if user would like to open then a status will be open,
            temperature will originate at 25 celsius,
            mode will be a cool mode and fan speed will originate at 1.
            if user would like to close then a status will be close,
            temperature will be a '-' and mode also, fan speed will be a '0'
            fan swing will be 'OFF' '''
        if oc == 'open':
            self.status = oc
            self.temp = '25'
            self.mode = 'Cool'
            self.fan[0] = '1'
        if oc == 'close':
            self.status = oc
            self.temp = '-'
            self.mode = '-'
            self.fan[0] = '0'
            self.fan[1] = 'OFF'

    def swing(self, swing):
        '''this function is for turning on or turning off  a fan swing on AC
        following by user command'''
        if swing == 'ON' or swing == 'OFF':
            self.fan[1] = swing

    def speed(self, speed):
        '''this function is for increasing and decreasing a fan speed following
         by user command.
         the least speed is at 1 and the most speed is at 5'''
        if 1 <= speed <= 5:
            self.fan[0] = str(speed)
            print('Now, speed is ', format(speed))
        else:
            print('speed must be greater than 0 and less than 6.')

    def temperature(self, temper):
        '''this function is for changing a AC temperature.
        range of temperature is between 15 to 30 celsuis. if user inputs a value
        that out of given range then print 'temperature must be greater than 14 and less than 31.' '''
        if self.mode != 'Auto':
            if 15 <= temper <= 30:
                self.temp = str(temper)
            else:
                print('temperature must be greater than 14 and less than 31.')

    def adjust_mode(self, index):
        '''this function is for changing the AC mode.
        AC modes are auto, cool, dry, eco, heat and fan mode.'''
        ac_mode = ['Auto', 'Cool', 'Dry', 'Eco', 'Heat', 'Fan']
        self.mode = ac_mode[index - 1]

    def auto(self):
        '''this function is a specific function that using when a user would
        like to use auto mode then this function is used and adjust the proper
        temperature by random situation
        the conditon:
                    if mode is auto then if season is summer
                then if outside temp is in a range of 28 to 32 then AC temp is
                22 but if outside temp is greater than 32 then AC temp is 20.
                if season is rainy then if outside temp is in range of 20 to 24
                then AC temp is 26 but if outside temp is greater than 24 then
                AC temp is 24. if season is winter then if outside temo is in
                range of 15 to 23 the AC temp is 27 but if outside temp is
                greater than 2 then AC temp is 26'''
        if self.mode == 'Auto':
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

    def manully(self):
        '''this function is manually input the season and temp in user's area.
        the condition is similar to auto function above'''
        if data[-1]['season'] == 'summer':
            if 25 <= int(data[-1]['temp']) <= 32:
                self.temp = '22'
            if int(data[-1]['temp']) > 32:
                self.temp = '20'
        if data[-1]['season'] == 'rainy':
            if 20 <= int(data[-1]['temp']) <= 24:
                self.temp = '26'
            if int(data[-1]['temp']) > 24:
                self.temp = '24'
        if data[-1]['season'] == 'winter':
            if 15 <= int(data[-1]['temp']) <= 23:
                self.temp = '27'
            if int(data[-1]['temp']) > 23:
                self.temp = '26'

    def __str__(self):
        '''print out the status of the AC
        example: AC1-Status:open Temperature:24°C Mode:Cool Speed:2 Swing:OFF'''
        return f'{self.__name}-Status:{self.status} Temperature:{self.temp}°C ' \
               f'Mode:{self.mode} Speed:{self.fan[0]} Swing:{self.fan[1]}'
