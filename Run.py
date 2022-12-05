import os
import time
from AC import AC
from Fan import Fan
from Router import Router
from Home import Home
from RWfile import RWfile

'-----------------------------------------------------------------------------'

data = RWfile('database.csv')
ac1 = AC('bedroom AC', '-', '-', ['0', 'OFF'], 'close')
ac2 = AC('living room AC', '-', '-', ['0', 'OFF'], 'close')
ac3 = AC('dining room AC', '-', '-', ['0', 'OFF'], 'close')
fan1 = Fan('bedroom Fan', ['0', 'OFF'], '-', 'close')
fan2 = Fan('living room Fan', ['0', 'OFF'], '-', 'close')
fan3 = Fan('kitchen Fan', ['0', 'OFF'], '-', 'close')
rt1 = Router('DS136 Fiber', [], 'Ab12345678+', 'close')
virtual_home = Home([ac1, ac2, ac3, fan1, fan2, fan3, rt1])

'-----------------------------------------------------------------------------'
while True:
    print('ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ'
          'ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ')
    print('')
    print('1. bedroom AC')
    print('2. living room AC')
    print('3. working room AC')
    print('4. bedroom Fan')
    print('5. living room Fan')
    print('6. working room Fan')
    print('7. DS136 Fiber')
    print('8. show status')
    print('0. Exit')
    print('')
    print('ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ'
          'ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ')
    num = int(input('Enter device number: '))
    os.system('clear')
    if num == 0:
        break
    if num == 1:
        while True:
            if getattr(ac1, 'status') == 'close':
                yn = input(f'Now, {getattr(ac1, "name")} is close, '
                           'Will you open the AC?(y/n): ')
                if yn == 'y':
                    ac1.open_close('open')
                    print(f'the {getattr(ac1, "name")} is now opening...')
                    time.sleep(1)
                    os.system('clear')
                else:
                    print(f'{getattr(ac1, "name")} still close...')
                    time.sleep(1.5)
                    os.system('clear')
                    break
            print('ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ'
                  'ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ')
            print('')
            print('1. close the device')
            print('2. adjust a fan swing')
            print('3. adjust fan speed')
            print('4. adjust temperature')
            print('5. add temperature and season manually')
            print('6. adjust mode')
            print(f'7. show status of {getattr(ac1, "name")}')
            print('8. back')
            print('')
            print('ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ'
                  'ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ')
            choice_ac1 = int(input('Enter choice number: '))
            if choice_ac1 == 1:
                ac1.open_close('close')
                print(f'the {getattr(ac1, "name")} is now closing...')
                time.sleep(1)
                os.system('clear')
                break
            if choice_ac1 == 2:
                ac1_fan = getattr(ac1, 'fan')
                if ac1_fan[1] == 'OFF':
                    ac1_fan[1] = 'ON'
                    print(
                        f'fan swing of {getattr(ac1, "name")} is now ON')
                elif ac1_fan[1] == 'ON':
                    ac1_fan[1] = 'OFF'
                    print(
                        f'fan swing of {getattr(ac1, "name")} is now OFF')
                time.sleep(1.5)
                os.system('clear')
            if choice_ac1 == 3:
                ac1_fan = getattr(ac1, 'fan')
                cr_speed = ac1_fan[0]
                print(f'Current speed is {cr_speed}.')
                speed = int(input('Enter a speed(1-5): '))
                ac1.speed(speed)
                print(f'Now, speed is {speed}.')
                time.sleep(1.5)
                os.system('clear')
            if choice_ac1 == 4:
                if getattr(ac1, 'mode') == 'Auto':
                    print(f'{getattr(ac1, "name")} automatically '
                          f'adjusts a temperature.')
                    ac1.auto()
                elif getattr(ac1, 'mode') != 'Auto':
                    print(f'Current temperature is '
                          f'{getattr(ac1, "temp")}°C')
                    temp = int(input('Enter the temperature(15-30): '))
                    ac1.temperature(temp)
                    if 15 <= temp <= 30:
                        print(f'Now, temperature is {temp}°C')
                time.sleep(1.5)
                os.system('clear')
            if choice_ac1 == 5:
                data.write()
                ac1.manully()
                print(f'{getattr(ac1, "name")} adjusts proper '
                      f'temperature from given temperature and season.')
                time.sleep(1.5)
                os.system('clear')
            if choice_ac1 == 6:
                print('1. Auto mode')
                print('2. Cool mode')
                print('3. Dry mode')
                print('4. ECO mode')
                print('5. Heat mode')
                print('6. Fan mode')
                mode = int(input('Enter mode number(1-6): '))
                if mode == 1:
                    AC.mode(ac1, 1)
                    ac1.auto()
                    print('Current mode is Auto mode')
                else:
                    AC.mode(ac1, mode)
                    print(
                        f'Current mode is {getattr(ac1, "mode")} mode')
                time.sleep(1.5)
                os.system('clear')
            if choice_ac1 == 7:
                print(ac1)
                print("press 'Enter' to go back.")
                press = input('')
                if press == '':
                    os.system('clear')
            if choice_ac1 == 8:
                os.system('clear')
                break
    if num == 2:
        while True:
            if getattr(ac2, 'status') == 'close':
                yn = input(f'Now, {getattr(ac2, "name")} is close, '
                           'Will you open the AC?(y/n): ')
                if yn == 'y':
                    ac2.open_close('open')
                    print(f'the {getattr(ac2, "name")} is now opening...')
                    time.sleep(1)
                    os.system('clear')
                else:
                    print(f'{getattr(ac2, "name")} still close...')
                    time.sleep(1.5)
                    os.system('clear')
                    break
            print('ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ'
                  'ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ')
            print('')
            print('1. close the device')
            print('2. adjust a fan swing')
            print('3. adjust fan speed')
            print('4. adjust temperature')
            print('5. add temperature and season manually')
            print('6. adjust mode')
            print(f'7. show status of {getattr(ac1, "name")}')
            print('8. back')
            print('')
            print('ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ'
                  'ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ')
            choice_ac2 = int(input('Enter choice number: '))
            if choice_ac2 == 1:
                ac2.open_close('close')
                print(f'the {getattr(ac2, "name")} is now closing...')
                time.sleep(1)
                os.system('clear')
                break
            if choice_ac2 == 2:
                ac2_fan = getattr(ac2, 'fan')
                if ac2_fan[1] == 'OFF':
                    ac2_fan[1] = 'ON'
                    print(
                        f'fan swing of {getattr(ac2, "name")} is now ON')
                elif ac2_fan[1] == 'ON':
                    ac2_fan[1] = 'OFF'
                    print(
                        f'fan swing of {getattr(ac2, "name")} is now OFF')
                time.sleep(1.5)
                os.system('clear')
            if choice_ac2 == 3:
                ac2_fan = getattr(ac2, 'fan')
                cr_speed = ac2_fan[0]
                print(f'Current speed is {cr_speed}.')
                speed = int(input('Enter a speed(1-5): '))
                ac2.speed(speed)
                print(f'Now, speed is {speed}.')
                time.sleep(1.5)
                os.system('clear')
            if choice_ac2 == 4:
                if getattr(ac2, 'mode') == 'Auto':
                    print(f'{getattr(ac2, "name")} automatically '
                          f'adjusts a temperature.')
                    ac2.auto()
                elif getattr(ac2, 'mode') != 'Auto':
                    print(f'Current temperature is '
                          f'{getattr(ac2, "temp")}°C')
                    temp = int(input('Enter the temperature(15-30): '))
                    ac2.temperature(temp)
                    if 15 <= temp <= 30:
                        print(f'Now, temperature is {temp}°C')
                time.sleep(1.5)
                os.system('clear')
            if choice_ac2 == 5:
                data.write()
                ac2.manully()
                print(f'{getattr(ac2, "name")} adjusts proper '
                      f'temperature from given temperature and season.')
            if choice_ac2 == 6:
                print('1. Auto mode')
                print('2. Cool mode')
                print('3. Dry mode')
                print('4. ECO mode')
                print('5. Heat mode')
                print('6. Fan mode')
                mode = int(input('Enter mode number(1-6): '))
                if mode == 1:
                    AC.mode(ac2, 1)
                    ac2.auto()
                    print('Current mode is Auto mode')
                else:
                    AC.mode(ac2, mode)
                    print(
                        f'Current mode is {getattr(ac2, "mode")} mode')
                time.sleep(1.5)
                os.system('clear')
            if choice_ac2 == 7:
                print(ac2)
                print("press 'Enter' to go back.")
                press = input('')
                if press == '':
                    os.system('clear')
            if choice_ac2 == 8:
                os.system('clear')
                break
    if num == 3:
        while True:
            if getattr(ac3, 'status') == 'close':
                yn = input(f'Now, {getattr(ac3, "name")} is close, '
                           'Will you open the AC?(y/n): ')
                if yn == 'y':
                    ac3.open_close('open')
                    print(f'the {getattr(ac3, "name")} is now opening...')
                    time.sleep(1)
                    os.system('clear')
                else:
                    print(f'{getattr(ac3, "name")} still close...')
                    time.sleep(1.5)
                    os.system('clear')
                    break
            print('ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ'
                  'ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ')
            print('')
            print('1. close the device')
            print('2. adjust a fan swing')
            print('3. adjust fan speed')
            print('4. adjust temperature')
            print('5. add temperature and season manually')
            print('6. adjust mode')
            print(f'7. show status of {getattr(ac1, "name")}')
            print('8. back')
            print('')
            print('ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ'
                  'ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ')
            choice_ac3 = int(input('Enter choice number: '))
            if choice_ac3 == 1:
                ac3.open_close('close')
                print(f'the {getattr(ac3, "name")} is now closing...')
                time.sleep(1)
                os.system('clear')
                break
            if choice_ac3 == 2:
                ac3_fan = getattr(ac3, 'fan')
                if ac3_fan[1] == 'OFF':
                    ac3_fan[1] = 'ON'
                    print(
                        f'fan swing of {getattr(ac3, "name")} is now ON')
                elif ac3_fan[1] == 'ON':
                    ac3_fan[1] = 'OFF'
                    print(
                        f'fan swing of {getattr(ac3, "name")} is now OFF')
                time.sleep(1.5)
                os.system('clear')
            if choice_ac3 == 3:
                ac3_fan = getattr(ac3, 'fan')
                cr_speed = ac3_fan[0]
                print(f'Current speed is {cr_speed}.')
                speed = int(input('Enter a speed(1-5): '))
                ac3.speed(speed)
                print(f'Now, speed is {speed}.')
                time.sleep(1.5)
                os.system('clear')
            if choice_ac3 == 4:
                if getattr(ac3, 'mode') == 'Auto':
                    print(f'{getattr(ac3, "name")} automatically '
                          f'adjusts a temperature.')
                    ac3.auto()
                elif getattr(ac3, 'mode') != 'Auto':
                    print(f'Current temperature is '
                          f'{getattr(ac3, "temp")}°C')
                    temp = int(input('Enter the temperature(15-30): '))
                    ac3.temperature(temp)
                    if 15 <= temp <= 30:
                        print(f'Now, temperature is {temp}°C')
                time.sleep(1.5)
                os.system('clear')
            if choice_ac2 == 5:
                data.write()
                ac2.manully()
                print(f'{getattr(ac2, "name")} adjusts proper '
                      f'temperature from given temperature and season...')
            if choice_ac3 == 6:
                print('1. Auto mode')
                print('2. Cool mode')
                print('3. Dry mode')
                print('4. ECO mode')
                print('5. Heat mode')
                print('6. Fan mode')
                mode = int(input('Enter mode number(1-6): '))
                if mode == 1:
                    AC.mode(ac3, 1)
                    ac3.auto()
                    print('Current mode is Auto mode')
                else:
                    AC.mode(ac3, mode)
                    print(
                        f'Current mode is {getattr(ac3, "mode")} mode')
                time.sleep(1.5)
                os.system('clear')
            if choice_ac3 == 7:
                print(ac3)
                print("press 'Enter' to go back.")
                press = input('')
                if press == '':
                    os.system('clear')
            if choice_ac3 == 8:
                os.system('clear')
                break
    if num == 4:
        while True:
            if getattr(fan1, 'status') == 'close':
                print(f"{getattr(fan1, 'name')} is close. "
                      f"Pressing number '1-3' to open.")
                speed = int(
                    input('Enter a speed(1-3), Enter "0" to go back: '))
                if speed > 0:
                    fan1.speed(speed)
                    print(f'Now, {getattr(fan1, "name")} is open, '
                          f'Speed at {speed}.')
                    time.sleep(1.5)
                    os.system('clear')
                else:
                    print(f'{getattr(fan1, "name")} still close...')
                    time.sleep(1.5)
                    os.system('clear')
                    break
            print('ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ'
                  'ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ')
            print('')
            print('1. adjust speed')
            print('2. swing the fan')
            print('3. adjust mode')
            print('4. show status')
            print('5. back')
            print('')
            print('ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ'
                  'ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ')
            choice = int(input('Enter choice number: '))
            if choice == 1:
                speed = int(input('Enter a speed(0-3): '))
                if speed > 0:
                    fan1.speed(speed)
                    print(f'{getattr(fan1, "name")} fan '
                          f'speed is at {speed}.')
                else:
                    print(f'Now, {getattr(fan1, "name")} is close.')
                time.sleep(1.5)
                os.system('clear')
            if choice == 2:
                fan1.swing()
                time.sleep(1.5)
                os.system('clear')
            if choice == 3:
                print('1. Normal mode')
                print('2. Cooling mode')
                num = int(input('Enter choice number: '))
                if num == 1:
                    Fan.mode(fan1, 1)
                    print(f'Now, {getattr(fan1, "name")} mode is normal')
                if num == 2:
                    Fan.mode(fan1, 2)
                    print(f'Now, {getattr(fan1, "name")} mode is cooling')
                time.sleep(1.5)
                os.system('clear')
            if choice == 4:
                print(fan1)
                print("press 'Enter' to go back.")
                press = input('')
                if press == '':
                    os.system('clear')
            if choice == 5:
                os.system('clear')
                break
    if num == 5:
        while True:
            if getattr(fan2, 'status') == 'close':
                print(f"{getattr(fan2, 'name')} is close. "
                      f"Pressing number '1-3' to open.")
                speed = int(
                    input('Enter a speed(1-3), Enter "0" to go back: '))
                if speed > 0:
                    fan2.speed(speed)
                    print(f'Now, {getattr(fan2, "name")} is open, '
                          f'Speed at {speed}.')
                    time.sleep(1.5)
                    os.system('clear')
                else:
                    print(f'{getattr(fan2, "name")} still close.')
                    time.sleep(1.5)
                    os.system('clear')
                    break
            print('ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ'
                  'ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ')
            print('')
            print('1. adjust speed')
            print('2. swing the fan')
            print('3. adjust mode')
            print('4. show status')
            print('5. back')
            print('')
            print('ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ'
                  'ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ')
            choice = int(input('Enter choice number: '))
            if choice == 1:
                speed = int(input('Enter a speed(0-3): '))
                if speed > 0:
                    fan2.speed(speed)
                    print(f'{getattr(fan2, "name")} fan '
                          f'speed is at {speed}.')
                else:
                    print(f'Now, {getattr(fan2, "name")} is close.')
                time.sleep(1.5)
                os.system('clear')
            if choice == 2:
                fan2.swing()
                time.sleep(1.5)
                os.system('clear')
            if choice == 3:
                print('1. Normal mode')
                print('2. Cooling mode')
                num = int(input('Enter choice number: '))
                if num == 1:
                    Fan.mode(fan2, 1)
                    print(f'Now, {getattr(fan2, "name")} mode is normal')
                if num == 2:
                    Fan.mode(fan2, 2)
                    print(f'Now, {getattr(fan2, "name")} mode is cooling')
                time.sleep(1.5)
                os.system('clear')
            if choice == 4:
                print(fan2)
                print("press 'Enter' to go back.")
                press = input('')
                if press == '':
                    os.system('clear')
            if choice == 5:
                os.system('clear')
                break
    if num == 6:
        while True:
            if getattr(fan3, 'status') == 'close':
                print(f"{getattr(fan3, 'name')} is close. "
                      f"Pressing number '1-3' to open.")
                speed = int(
                    input('Enter a speed(1-3), Enter "0" to go back: '))
                if speed > 0:
                    fan3.speed(speed)
                    print(f'Now, {getattr(fan3, "name")} is open, '
                          f'Speed at {speed}.')
                    time.sleep(1.5)
                    os.system('clear')
                else:
                    print(f'{getattr(fan3, "name")} still close.')
                    time.sleep(1.5)
                    os.system('clear')
                    break
            print('ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ'
                  'ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ')
            print('')
            print('1. adjust speed')
            print('2. swing the fan')
            print('3. adjust mode')
            print('4. show status')
            print('5. back')
            print('')
            print('ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ'
                  'ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ')
            choice = int(input('Enter choice number: '))
            if choice == 1:
                speed = int(input('Enter a speed(0-3): '))
                if speed > 0:
                    fan3.speed(speed)
                    print(f'{getattr(fan3, "name")} fan '
                          f'speed is at {speed}.')
                else:
                    print(f'Now, {getattr(fan3, "name")} is close.')
                time.sleep(1.5)
                os.system('clear')
            if choice == 2:
                fan3.swing()
                time.sleep(1.5)
                os.system('clear')
            if choice == 3:
                print('1. Normal mode')
                print('2. Cooling mode')
                num = int(input('Enter choice number: '))
                if num == 1:
                    Fan.mode(fan3, 1)
                    print(f'Now, {getattr(fan3, "name")} mode is normal')
                if num == 2:
                    Fan.mode(fan3, 2)
                    print(f'Now, {getattr(fan3, "name")} mode is cooling')
                time.sleep(1.5)
                os.system('clear')
            if choice == 4:
                print(fan3)
                print("press 'Enter' to go back.")
                press = input('')
                if press == '':
                    os.system('clear')
            if choice == 5:
                os.system('clear')
                break
    if num == 7:
        while True:
            if getattr(rt1, 'status') == 'close':
                yn = input(f'{getattr(rt1, "name")} router is close, '
                           'Will you open it?(y/n): ')
                if yn == 'y':
                    rt1.open_close('open')
                    print(f'Now, {getattr(rt1, "name")} is opening...')
                    time.sleep(1.5)
                    os.system('clear')
                else:
                    print(f'{getattr(rt1, "name")} still close...')
                    time.sleep(1.5)
                    os.system('clear')
                    break
            print('ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ'
                  'ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ')
            print('')
            print('1. close the device')
            print('2. add user')
            print('3. change Password')
            print('4. show status')
            print('5. back')
            print('')
            print('ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ'
                  'ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ')
            choice = int(input('Enter choice number: '))
            if choice == 1:
                rt1.open_close('close')
                print(f'Now, {getattr(rt1, "name")} is closing...')
                time.sleep(1.5)
                os.system('clear')
                break
            if choice == 2:
                i = 0
                while i != 3:
                    pw = input(
                        f'Enter {getattr(rt1, "name")} router password: ')
                    if pw == getattr(rt1, 'password'):
                        new_user = input('Enter name: ')
                        rt1.add_user(new_user)
                        print(f'{new_user} is added.')
                        time.sleep(1.25)
                        os.system('clear')
                        break
                    else:
                        i += 1
                        print(f'Wrong password, '
                              f'Please try again (attempt:{i})')
                time.sleep(0.5)
                os.system('clear')
            if choice == 3:
                i = 0
                while i != 3:
                    pw = input(f'Enter {getattr(rt1, "name")} '
                               f'router password: ')
                    if pw == getattr(rt1, 'password'):
                        new_pw = input('Enter new password: ')
                        rt1.change_pw(new_pw)
                        print('The password is changed!')
                        time.sleep(1.25)
                        os.system('clear')
                        break
                    else:
                        i += 1
                        print(f'Wrong password, '
                              f'Please try again (attempt:{i})')
                time.sleep(0.5)
                os.system('clear')
            if choice == 4:
                i = 0
                while i != 3:
                    pw = input(f'Enter {getattr(rt1, "name")} '
                               f'router password: ')
                    if pw == getattr(rt1, 'password'):
                        print(rt1)
                        gb = input('Press Enter to go back.')
                        if gb == '':
                            os.system('clear')
                            break
                    else:
                        i += 1
                        print(f'Wrong password, '
                              f'Please try again (attempt:{i})')
                time.sleep(0.5)
                os.system('clear')
            if choice == 5:
                os.system('clear')
                break
    if num == 8:
        while True:
            virtual_home.show_status()
            print('')
            gb = input('Press Enter to go back.')
            if gb == '':
                os.system('clear')
