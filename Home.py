class Home:
    def __init__(self, devices):
        self.devices = devices

    def show_status(self):
        for device in self.devices:
            print('')
            print(device)
