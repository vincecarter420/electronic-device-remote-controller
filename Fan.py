class Fan:
    def __init__(self, name='', fan=['0', 'OFF'], mode='',
                 status='close'):
        self.name = name
        self.fan = fan
        self.mode = mode
        self.status = status

    def speed(self, speed):
        if 0 <= int(speed) <= 3:
            if int(speed) == 0:
                self.fan[0] = speed
                self.fan[1] = 'OFF'
                self.status = 'close'
            else:
                self.fan[0] = speed
                self.status = 'open'
        else:
            print('Speed must be greater equal to 0 and less than 4')

    def swing(self):
        if self.status == 'open':
            if self.fan[1] == 'OFF':
                self.fan[1] = 'ON'
                print(f'Fan swing is now ON')
            elif self.fan[1] == 'ON':
                self.fan[1] = 'OFF'
                print(f'Fan swing is now OFF')
        else:
            print("Status must be 'ON'")

    def mode(self, index):
        fan_mode = ['Normal', 'Cooling']
        self.mode = str(fan_mode[int(index) - 1])

    def __str__(self):
        return f'{self.name}-Status:{self.status} Mode:{self.mode}' \
               f' Speed:{self.fan[0]} Swing:{self.fan[1]}'
