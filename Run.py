from AC import AC
from Fan import Fan
from Router import Router
from Home import Home

ac1 = AC('bedroom AC', '-', '-', ['0', 'OFF'], 'close')
ac2 = AC('living room AC', '-', '-', ['0', 'OFF'], 'close')
ac3 = AC('working room AC', '-', '-', ['0', 'OFF'], 'close')
fan1 = Fan('bedroom Fan', ['0', 'OFF'], '-', 'close')
fan2 = Fan('living room Fan', ['0', 'OFF'], '-', 'close')
fan3 = Fan('working room Fan', ['0', 'OFF'], '-', 'close')
rt1 = Router('DS136 Fiber', 'Ab12345678+')

while True:
    print('1. bedroom AC')
    print('2. living room AC')
    print('3. working room AC')
    print('4. bedroom Fan')
    print('5. living room Fan')
    print('6. working room Fan')
    print('7. DS136 Fiber')
    num = int(input('Enter device number: '))
    # if 1 <= num <= 3:
