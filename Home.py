class Home:
    def __init__(self, devices: list):
        '''create devices value'''
        self.devices = devices

    def show_status(self):
        '''show all device status'''
        for device in self.devices:
            print('')
            print(device)
