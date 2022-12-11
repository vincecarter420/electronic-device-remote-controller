#### this file is for progression of all object ####
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


class Run:
    def ac_menu(self, ac):
        '''virtual menu of controlling AC like a function in one application'''
        while True:
            if getattr(ac, 'status') == 'close':
                yn = input(f'Now, {getattr(ac, "name")} is close, '
                           'Will you open the AC?(y/n): ')
                if yn == 'y':
                    ac.open_close('open')
                    print(f'the {getattr(ac, "name")} is now opening...')
                    time.sleep(1)
                    os.system('clear')
                else:
                    print(f'{getattr(ac, "name")} still close...')
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
            print(f'7. show status of {getattr(ac, "name")}')
            print('8. back')
            print('')
            print('ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ'
                  'ΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞΞ')
            choice_ac = int(input('Enter choice number: '))
            if choice_ac == 1:
                ac.open_close('close')
                print(f'the {getattr(ac, "name")} is now closing...')
                time.sleep(1)
                os.system('clear')
                break
            if choice_ac == 2:
                ac_fan = getattr(ac, 'fan')
                if ac_fan[1] == 'OFF':
                    ac_fan[1] = 'ON'
                    print(
                        f'fan swing of {getattr(ac, "name")} is now ON')
                elif ac_fan[1] == 'ON':
                    ac_fan[1] = 'OFF'
                    print(
                        f'fan swing of {getattr(ac, "name")} is now OFF')
                time.sleep(1.5)
                os.system('clear')
            if choice_ac == 3:
                ac_fan = getattr(ac, 'fan')
                cr_speed = ac_fan[0]
                print(f'Current speed is {cr_speed}.')
                speed = int(input('Enter a speed(1-5): '))
                ac.speed(speed)
                time.sleep(1.5)
                os.system('clear')
            if choice_ac == 4:
                if getattr(ac, 'mode') == 'Auto':
                    print(f'{getattr(ac, "name")} automatically '
                          f'adjusts a temperature.')
                    ac.auto()
                elif getattr(ac, 'mode') != 'Auto':
                    print(f'Current temperature is '
                          f'{getattr(ac, "temp")}°C')
                    temp = int(input('Enter the temperature(15-30): '))
                    ac.temperature(temp)
                    if 15 <= temp <= 30:
                        print(f'Now, temperature is {temp}°C')
                time.sleep(1.5)
                os.system('clear')
            if choice_ac == 5:
                data.write()
                ac.manully()
                print(f'{getattr(ac, "name")} adjusts proper '
                      f'temperature from given temperature and season.')
                time.sleep(1.5)
                os.system('clear')
            if choice_ac == 6:
                print('1. Auto mode')
                print('2. Cool mode')
                print('3. Dry mode')
                print('4. ECO mode')
                print('5. Heat mode')
                print('6. Fan mode')
                mode = int(input('Enter mode number(1-6): '))
                if mode == 1:
                    ac.adjust_mode(1)
                    ac.auto()
                    print('Current mode is Auto mode')
                else:
                    ac.adjust_mode(mode)
                    print(
                        f'Current mode is {getattr(ac, "mode")} mode')
                time.sleep(1.5)
                os.system('clear')
            if choice_ac == 7:
                print(ac)
                print("press 'Enter' to go back.")
                press = input('')
                if press == '':
                    os.system('clear')
            if choice_ac == 8:
                os.system('clear')
                break

    def fan_menu(self, fan):
        '''virtual menu of controlling Fan like a function in a application'''
        while True:
            if getattr(fan, 'status') == 'close':
                print(f"{getattr(fan, 'name')} is close. "
                      f"Pressing number '1-3' to open.")
                speed = int(
                    input('Enter a speed(1-3), Enter "0" to go back: '))
                if speed > 0:
                    fan.speed(speed)
                    print(f'Now, {getattr(fan, "name")} is open, '
                          f'Speed at {speed}.')
                    time.sleep(1.5)
                    os.system('clear')
                else:
                    print(f'{getattr(fan, "name")} still close...')
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
                    fan.speed(speed)
                    print(f'{getattr(fan, "name")} fan '
                          f'speed is at {speed}.')
                else:
                    print(f'Now, {getattr(fan, "name")} is close.')
                time.sleep(1.5)
                os.system('clear')
            if choice == 2:
                fan.swing()
                time.sleep(1.5)
                os.system('clear')
            if choice == 3:
                print('1. Normal mode')
                print('2. Cooling mode')
                num = int(input('Enter choice number: '))
                if num == 1:
                    Fan.mode(fan, 1)
                    print(f'Now, {getattr(fan, "name")} mode is normal')
                if num == 2:
                    Fan.mode(fan, 2)
                    print(f'Now, {getattr(fan, "name")} mode is cooling')
                time.sleep(1.5)
                os.system('clear')
            if choice == 4:
                print(fan)
                print("press 'Enter' to go back.")
                press = input('')
                if press == '':
                    os.system('clear')
            if choice == 5:
                os.system('clear')
                break

    def rt_menu(self, rt):
        '''
            virtual menu of controlling router like a function in a application
        '''
        while True:
            if getattr(rt, 'status') == 'close':
                yn = input(f'{getattr(rt, "name")} router is close, '
                           'Will you open it?(y/n): ')
                if yn == 'y':
                    rt.open_close('open')
                    print(f'Now, {getattr(rt, "name")} is opening...')
                    time.sleep(1.5)
                    os.system('clear')
                else:
                    print(f'{getattr(rt, "name")} still close...')
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
                rt.open_close('close')
                print(f'Now, {getattr(rt, "name")} is closing...')
                time.sleep(1.5)
                os.system('clear')
                break
            if choice == 2:
                i = 0
                while i != 3:
                    pw = input(
                        f'Enter {getattr(rt, "name")} router password: ')
                    if pw == getattr(rt1, 'password'):
                        new_user = input('Enter name: ')
                        rt.add_user(new_user)
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
                    pw = input(f'Enter {getattr(rt, "name")} '
                               f'router password: ')
                    if pw == getattr(rt, 'password'):
                        new_pw = input('Enter new password: ')
                        rt.change_pw(new_pw)
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
                    pw = input(f'Enter {getattr(rt, "name")} '
                               f'router password: ')
                    if pw == getattr(rt, 'password'):
                        print(rt)
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

    def home_menu(self, home):
        '''show all status of each device'''
        while True:
            home.show_status()
            print('')
            gb = input('Press Enter to go back.')
            if gb == '':
                os.system('clear')


if __name__ == '__main__':
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
            Run().ac_menu(ac1)
        if num == 2:
            Run().ac_menu(ac2)
        if num == 3:
            Run().ac_menu(ac3)
        if num == 4:
            Run().fan_menu(fan1)
        if num == 5:
            Run().fan_menu(fan2)
        if num == 6:
            Run().fan_menu(fan3)
        if num == 7:
            Run().rt_menu(rt1)
        if num == 8:
            Run().home_menu(virtual_home)
