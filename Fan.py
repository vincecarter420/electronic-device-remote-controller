class Fan:
    def __init__(self, name: str, fan: list, mode: str,
                 status: str):
        '''create name, fan, mode and status values'''
        self.name = name
        self.fan = fan
        self.mode = mode
        self.status = status

    def speed(self, speed):
        '''this function is for selecting the fan speed and including open and
        close function
            if user selects '0' then the device close, if user select number
            between 1 and 3 the device will open and speed is at user selected
            speed'''
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
        '''this function is for adjusting fan swing
            the device must be open if not user cannot access this function
            if user turn on print 'Fan swing is now ON',
            if user turn off print 'Fan swing is now OFF' '''
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
        '''this function is for changing the Fan mode.
            Fan modes are normal and cooling mode.'''
        fan_mode = ['Normal', 'Cooling']
        self.mode = str(fan_mode[int(index) - 1])

    def __str__(self):
        '''print out the status of this device
            example: Fan1-Status:open Mode:normal Speed:2 Swing:ON'''
        return f'{self.name}-Status:{self.status} Mode:{self.mode}' \
               f' Speed:{self.fan[0]} Swing:{self.fan[1]}'
